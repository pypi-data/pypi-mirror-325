from .base import Surrogate

import numpy as np
import torch

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
torch.set_default_device(DEVICE)


class DGP(Surrogate):
    def __init__(self, **kwargs):
        super(DGP, self).__init__()

        self.name        = 'DGP'
        self.model       = kwargs['model'] if 'model' in kwargs else None
        self.hidden_size = kwargs['hidden_size'] if 'hidden_size' in kwargs else 64
        self.n_epochs    = kwargs['n_epochs'] if 'n_epochs' in kwargs else 100
        self.lr          = kwargs['lr'] if 'lr' in kwargs else 1e-3
        self.batch_size  = kwargs['batch_size'] if 'batch_size' in kwargs else 16
        self.verbose     = kwargs['verbose'] if 'verbose' in kwargs else 1
    
    def fit(self, X, y):

        if self.model is None:
            self.model = DistributionalDGP(X.shape[-1], y.shape[-1],
                                           n_epochs=self.n_epochs, hidden_size=self.hidden_size,
                                           lr = self.lr, batch_size=self.batch_size, verbose=self.verbose)
        
        self.model.fit(X, y)
    
    def predict(self, X):
        # print("predict in DGP(Surrogate): ", torch.tensor(X).dtype)

        f, std = self.model.predict(torch.tensor(X))

        return f, np.sqrt(std)


import torch
from torch.utils.data import TensorDataset, DataLoader
# from wgpot import Wasserstein_GP
from tqdm import tqdm
import gpytorch
from gpytorch.means import ConstantMean, LinearMean
from gpytorch.kernels import RBFKernel, ScaleKernel
from gpytorch.variational import VariationalStrategy, CholeskyVariationalDistribution
from gpytorch.distributions import MultivariateNormal
from gpytorch.mlls import VariationalELBO
from gpytorch.likelihoods import GaussianLikelihood

from gpytorch.models.deep_gps import DeepGPLayer, DeepGP
from gpytorch.mlls import DeepApproximateMLL
import gpytorch.mlls
import numpy as np
    

num_hidden_dims = 2

class ToyDeepGPHiddenLayer2(DeepGPLayer):
    def __init__(self, input_dims, output_dims, num_inducing=128, mean_type='constant'):
        if output_dims is None:
            inducing_points = torch.randn(num_inducing, input_dims)
            batch_shape = torch.Size([])
        else:
            inducing_points = torch.randn(output_dims, num_inducing, input_dims)
            batch_shape = torch.Size([output_dims])

        variational_distribution = CholeskyVariationalDistribution(
            num_inducing_points=num_inducing,
            batch_shape=batch_shape
        )

        variational_strategy = VariationalStrategy(
            self,
            inducing_points,
            variational_distribution,
            learn_inducing_locations=True
        )

        super(ToyDeepGPHiddenLayer2, self).__init__(variational_strategy, input_dims, output_dims)

        if mean_type == 'constant':
            self.mean_module = ConstantMean(batch_shape=batch_shape)
        else:
            self.mean_module = LinearMean(input_dims)
        self.covar_module = ScaleKernel(
            RBFKernel(batch_shape=batch_shape, ard_num_dims=input_dims),
            batch_shape=batch_shape, ard_num_dims=None
        )

    def forward(self, x):
        mean_x = self.mean_module(x.float())
        covar_x = self.covar_module(x)
        return MultivariateNormal(mean_x, covar_x)

    def __call__(self, x, *other_inputs, **kwargs):
        """
        Overriding __call__ isn't strictly necessary, but it lets us add concatenation based skip connections
        easily. For example, hidden_layer2(hidden_layer1_outputs, inputs) will pass the concatenation of the first
        hidden layer's outputs and the input data to hidden_layer2.
        """
        # if len(other_inputs):
        #     if isinstance(x, gpytorch.distributions.MultitaskMultivariateNormal):
        #         x = x.rsample()

        #     processed_inputs = [
        #         inp.unsqueeze(0).expand(gpytorch.settings.num_likelihood_samples.value(), *inp.shape)
        #         for inp in other_inputs
        #     ]

        #     x = torch.cat([x] + processed_inputs, dim=-1)

        return super().__call__(x)


class DistributionalDGP(DeepGP):
    def __init__(self, input_dim, out_dim, **kwargs):
        super().__init__()
        hidden_layer = ToyDeepGPHiddenLayer2(
            input_dims=input_dim,
            output_dims=kwargs.get('hidden_size', 16),
            mean_type='linear',
        )

        last_layer = ToyDeepGPHiddenLayer2(
            input_dims=hidden_layer.output_dims,
            output_dims=None,
            mean_type='linear', # TODO LINEAR
        )

        self.hidden_layer = hidden_layer
        self.last_layer = last_layer
        self.likelihood = GaussianLikelihood()
        self.n_epochs = kwargs.get('n_epochs', 100)
        self.num_samples = kwargs.get('num_samples', 100)
        self.lr = kwargs.get('lr', 1e-3)
        self.batch_size = kwargs.get('batch_size', 8)
        self.verbose = kwargs.get('verbose', 1)

    def fit(self, X, y):
      
      self.loss_history = []
      self.predictions_history = []

      optimizer = torch.optim.Adam([{'params': self.parameters()},], lr=self.lr)
      mll = DeepApproximateMLL(VariationalELBO(self.likelihood, self, 500))


      epochs_iter = tqdm(range(self.n_epochs), desc="Epoch") if self.verbose > 1 else range(self.n_epochs)

    #   print("Fit in class Distributional GP: ", X.dtype)  
      for _ in epochs_iter:
        closs = 0
        with gpytorch.settings.num_likelihood_samples(self.num_samples):
            generator = torch.Generator(device=DEVICE)
            dataset  = TensorDataset(torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.float32))
            dataloader = DataLoader(dataset, batch_size=self.batch_size, generator=generator, shuffle=True)
            for x_batch, y_batch in dataloader: 
                output = self(x_batch)
                loss = -mll(output, y_batch)
                loss.backward(retain_graph=True)
                closs += loss.item()
                optimizer.step()

                optimizer.zero_grad()
        
        if self.verbose > 1:
            epochs_iter.set_description(f"Loss: {closs:.3f}")
        self.loss_history.append(loss)

        # with torch.no_grad():
        #     self.predictions_history.append(self.forward(train_mean_x))
      return self.loss_history

    def forward(self, x):
        with gpytorch.settings.num_likelihood_samples(1):
            hidden_rep1 = self.hidden_layer(x)
            output = self.last_layer(hidden_rep1)
        # mean_x = self.mean_module(output)
        # covar_x = self.covar_module(x)
        return output
    
    def predict(self, x):
        with torch.no_grad():
            mus = []
            variances = []
            # lls = []
            # for x_batch, y_batch in test_loader:
            # print("Distributional DGP predict; ", x.float().dtype)
            preds = self.likelihood(self(x.float()))
            mus.append(preds.mean)
            variances.append(preds.variance)
            # lls.append(self.likelihood.log_marginal(y, self(x)))

        return torch.cat(mus, dim=-1).cpu(), torch.cat(variances, dim=-1).cpu()
    
    def __call__(self, x, *other_inputs, **kwargs):
        """
        Overriding __call__ isn't strictly necessary, but it lets us add concatenation based skip connections
        easily. For example, hidden_layer2(hidden_layer1_outputs, inputs) will pass the concatenation of the first
        hidden layer's outputs and the input data to hidden_layer2.
        """
        with gpytorch.settings.num_likelihood_samples(self.num_samples):
            if len(other_inputs):
                if isinstance(x, gpytorch.distributions.MultitaskMultivariateNormal):
                    x = x.rsample()

                processed_inputs = [
                    inp.unsqueeze(0).expand(gpytorch.settings.num_likelihood_samples.value(), *inp.shape)
                    for inp in other_inputs
                ]

                x = torch.cat([x] + processed_inputs, dim=-1)

            # Метод call идет из базового класса Module, по умолчанию передает содержимое в forward, затем проверяет, чтобы тип выходной переменной был один из этих - (Distribution, torch.Tensor, LinearOperator)
            # Принимает значения размерности от двух
        return super().__call__(x)
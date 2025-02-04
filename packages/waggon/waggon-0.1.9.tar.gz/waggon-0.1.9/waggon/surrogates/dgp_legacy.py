from .base import Surrogate

import gc
import GPy
import torch
import deepgp
import numpy as np


DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
torch.set_default_device(DEVICE)


class DGPL(Surrogate):
    def __init__(self, **kwargs):
        super(DGPL, self).__init__()

        self.name        = 'DGPL'
        self.model       = kwargs['model'] if 'model' in kwargs else None
        self.hidden_size = kwargs['hidden_size'] if 'hidden_size' in kwargs else 64
        self.n_epochs    = kwargs['n_epochs'] if 'n_epochs' in kwargs else 100
        self.lr          = kwargs['lr'] if 'lr' in kwargs else 1e-3
        self.batch_size  = kwargs['batch_size'] if 'batch_size' in kwargs else 16
        self.verbose     = kwargs['verbose'] if 'verbose' in kwargs else 1
        self.n_iter      = 0
    
    def fit(self, X, y):

        if self.n_iter != 0:
            del self.model
            gc.collect()
        self.n_iter += 1
            
        self.model = deepgp.DeepGP([y.shape[1], self.hidden_size, X.shape[1]], Y=y, X=X,
                                    kernels=[GPy.kern.RBF(self.hidden_size, variance=1e-1), GPy.kern.RBF(X.shape[1], variance=1e-1)],
                                    num_inducing=self.n_epochs, back_constraint=False)
        
        self.model.optimize(messages=True, max_iters=self.n_epochs)
    
    def predict(self, X):

        f, std = self.model.predict(X)

        return f, np.sqrt(std)
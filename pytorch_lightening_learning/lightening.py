import torch
from torch import nn
import pytorch_lightning as pl
from torch.utils.data import DataLoader, random_split
from torchvision.datasets import MNIST
import os
from torchvision import datasets, transforms
from torch.nn import functional as F


class LightningMNISTClassifier(pl.LightningModule):

  def __init__(self):
    super(LightningMNISTClassifier, self).__init__()

    # mnist images are (1, 28, 28) (channels, width, height) 
    self.layer_1 = torch.nn.Linear(28 * 28, 128)
    self.layer_2 = torch.nn.Linear(128, 256)
    self.layer_3 = torch.nn.Linear(256, 10)

  def forward(self, x):
    batch_size, channels, width, height = x.siz()

    # (b, 1, 28, 28) -> (b, 1*28*28)
    x = x.view(batch_size, -1)

    # layer 1
    x = self.layer_1(x)
    x = torch.relu(x)

    # layer 2
    x = self.layer_2(x)
    x = torch.relu(x)

    # layer 3
    x = self.layer_3(x)

    # probability distribution over labels
    x = torch.log_softmax(x, dim=1)

    return x

# DATA

class MNISTDataModule(pl.LightningDataModule):

  def setup(self, stage):
    # transforms for images
    transform=transforms.Compose([transforms.ToTensor(), 
                                  transforms.Normalize((0.1307,), (0.3081,))])
      
    # prepare transforms standard to MNIST
    mnist_train = MNIST(os.getcwd(), train=True, download=True, transform=transform)
    mnist_test = MNIST(os.getcwd(), train=False, download=True, transform=transform)
    
    self.mnist_train, self.mnist_val = random_split(mnist_train, [55000, 5000])

  def train_dataloader(self):
    return DataLoader(self.mnist_train, batch_size=64)

  def val_dataloader(self):
    return DataLoader(self.mnist_val, batch_size=64)

  def test_dataloader(self):
    return DataLoader(self.mnist_test, batch_size=64)

# OPTIMISER


class LightningMNISTClassifier(pl.LightningModule):

    def configure_optimizers(self):
      optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
      return optimizer
  
class LightningMNISTClassifier(pl.LightningModule):

  def cross_entropy_loss(self, logits, labels):
    return F.nll_loss(logits, labels)

# TRAINING

class LightningMNISTClassifier(pl.LightningModule):

    def training_step(self, batch, batch_idx):
        x, y = train_batch
        logits = self.forward(x)   # we already defined forward and loss in the lightning module. We'll show the full code next
        loss = self.cross_entropy_loss(logits, y)
        self.log('train_loss', loss)
        return loss

Trainer(precision=16)

# VALIDATION 

class LightningMNISTClassifier(pl.LightningModule):

    def validation_step(self, batch, batch_idx):
        x, y = train_batch
        logits = self.forward(x)
        loss = self.cross_entropy_loss(logits, y)
        self.log('val_loss', loss)
        
# ****************************TOTAL***********************

class LightningMNISTClassifier(pl.LightningModule):

    def __init__(self):
        super(LightningMNISTClassifier, self).__init__()

        # mnist images are (1, 28, 28) (channels, width, height) 
        self.layer_1 = torch.nn.Linear(28 * 28, 128)
        self.layer_2 = torch.nn.Linear(128, 256)
        self.layer_3 = torch.nn.Linear(256, 10)

    def forward(self, x):
        batch_size, channels, width, height = x.size()

        # (b, 1, 28, 28) -> (b, 1*28*28)
        x = x.view(batch_size, -1)

        # layer 1 (b, 1*28*28) -> (b, 128)
        x = self.layer_1(x)
        x = torch.relu(x)

        # layer 2 (b, 128) -> (b, 256)
        x = self.layer_2(x)
        x = torch.relu(x)

        # layer 3 (b, 256) -> (b, 10)
        x = self.layer_3(x)

        # probability distribution over labels
        x = torch.log_softmax(x, dim=1)

        return x

    def cross_entropy_loss(self, logits, labels):
        return F.nll_loss(logits, labels)

    def training_step(self, batch, batch_idx):
        x, y = train_batch
        logits = self.forward(x)   # we already defined forward and loss in the lightning module. We'll show the full code next
        loss = self.cross_entropy_loss(logits, y)
        self.log('train_loss', loss)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = train_batch
        logits = self.forward(x)
        loss = self.cross_entropy_loss(logits, y)
        self.log('val_loss', loss)

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        return optimizer

# train
model = LightningMNISTClassifier()
trainer = pl.Trainer()

trainer.fit(model)

# ABSTRACTED

import torch
from torch import nn
import pytorch_lightning as pl
from torch.utils.data import DataLoader, random_split
from torch.nn import functional as F
from torchvision.datasets import MNIST
from torchvision import datasets, transforms
import os

class Backbone(nn.Module):

    def __init__(self):
        super().__init__()

        # mnist images are (1, 28, 28) (channels, width, height) 
        self.layer_1 = torch.nn.Linear(28 * 28, 128)
        self.layer_2 = torch.nn.Linear(128, 256)
        self.layer_3 = torch.nn.Linear(256, 10)

    def forward(self, x):
        batch_size, channels, width, height = x.size()

        # (b, 1, 28, 28) -> (b, 1*28*28)
        x = x.view(batch_size, -1)

        # layer 1 (b, 1*28*28) -> (b, 128)
        x = self.layer_1(x)
        x = torch.relu(x)

        # layer 2 (b, 128) -> (b, 256)
        x = self.layer_2(x)
        x = torch.relu(x)

        # layer 3 (b, 256) -> (b, 10)
        x = self.layer_3(x)

        return x

class LightningClassifier(pl.LightningModule):

    def __init__(self, backbone):
        super().__init__()
        self.backbone = backbone    

    def cross_entropy_loss(self, logits, labels):
        return F.nll_loss(logits, labels)

    def training_step(self, batch, batch_idx):
        x, y = train_batch
        logits = self.backbone(x)
        
        # probability distribution over labels
        x = torch.log_softmax(x, dim=1)

        loss = self.cross_entropy_loss(logits, y)
        self.log('train_loss', loss)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = train_batch

        # probability distribution over labels
        logits = self.backbone(x)
        x = torch.log_softmax(x, dim=1)
        
        loss = self.cross_entropy_loss(logits, y)
        self.log('val_loss', loss)

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        return optimizer

# train
model = Backbone()
classifier = LightningClassifier(model)
trainer = pl.Trainer()

trainer.fit(classifier)


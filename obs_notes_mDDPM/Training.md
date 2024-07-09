Training:

- Training is initiated in `run.py` with:
    
    python
    
    Copy
    
    `trainer.fit(model, datamodule=datamodule)`
    
- The training loop is defined in `src/models/DDPM_2D.py`, specifically in the `training_step` method.
- It uses the `forward` method of `GaussianDiffusion` to compute losses.
- The ResNet50 encoder (`self.encoder` in `DDPM_2D`) provides conditioning information.
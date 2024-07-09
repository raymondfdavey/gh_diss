Model instantiation:

- The DDPM_2D model is defined in `src/models/DDPM_2D.py`.
- It's instantiated in `run.py` using:
    
    python
    
    Copy
    
    `model: LightningModule = hydra.utils.instantiate(cfg.model)`
    
- The model includes:
    - A UNetModel from `src/models/LDM/modules/openaimodel.py`.
    - A GaussianDiffusion process from `src/models/modules/cond_DDPM.py`.
    - An encoder (ResNet50) from `src/models/modules/DDPM_encoder.py`.
- It uses configurations like `unet_dim`, `dim_mults`, and `test_timesteps` from `configs/model/DDPM_2D.yaml`.
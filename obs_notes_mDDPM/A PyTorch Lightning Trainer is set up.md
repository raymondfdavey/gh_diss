Trainer setup:

- The PyTorch Lightning Trainer is set up in `run.py`:
    
    python
    
    Copy
    
    `trainer: Trainer = hydra.utils.instantiate(cfg.trainer, callbacks=callbacks, logger=logger, _convert_="partial")`
    
- It uses configurations from `configs/trainer/default.yaml`, including `max_epochs`, `gpus`, and `precision`.
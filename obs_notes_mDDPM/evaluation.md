Evaluation:

- Evaluation is triggered in `run.py` with:
    
    `trainer.test(model, datamodule=datamodule)`
    
- The test loop is defined in `src/models/DDPM_2D.py`, specifically in the `test_step` method.
- It uses functions from `src/utils/utils_eval.py` for metrics calculation.
- Results are logged using WandB and CSV loggers, as specified in `configs/logger/wandb.yaml` and `configs/logger/csv.yaml`.
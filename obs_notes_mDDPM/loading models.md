Based on the configuration files provided, models are saved in the following location:

1. In the `checkpoint.yaml` file, there is a ModelCheckpoint callback configured with:

```yaml
model_checkpoint:
    _target_: pytorch_lightning.callbacks.model_checkpoint.ModelCheckpoint
    dirpath: "checkpoints/"
    filename: "epoch-{epoch}_step-{step}_loss-{val/Loss_comb:.2f}"
```

This indicates that checkpoints will be saved in a directory called "checkpoints/" relative to the working directory.

2. In the `config.yaml` file, there is a variable defined:

```yaml
log_dir:  ${oc.env:LOG_DIR}
```

This suggests that the actual log directory (which likely includes the checkpoints) is set via an environment variable called LOG_DIR.

3. The `run.py` file likely uses these configurations to determine the final save location.

So in summary:

- Checkpoints are saved in a "checkpoints/" subdirectory
- The parent directory for this is likely specified by the LOG_DIR environment variable
- The full path would be something like: $LOG_DIR/checkpoints/

The exact filename of each checkpoint will follow the pattern:
"epoch-{epoch}_step-{step}_loss-{val/Loss_comb:.2f}"

To find the exact location on your system, you would need to check:
1. The value of the LOG_DIR environment variable
2. Any modifications made in the run.py file that might alter this path

If you need the exact absolute path, you may need to check the logs of a training run or inspect the running code to see how these configurations are applied.

***
You're right to question that - I should have been more precise in my explanation. Let me clarify:

A model checkpoint is not the model itself, but rather a saved state of the model at a particular point during training. Here's a more accurate breakdown:

1. Model Checkpoints:
   - These are saved snapshots of the model's state, including weights, optimizer state, and other training metadata.
   - They allow you to resume training from a specific point or load a model for inference.
   - In the configuration, these are handled by the ModelCheckpoint callback in PyTorch Lightning.

2. The Actual Model:
   - The model itself is defined in the code, typically in a separate Python file.
   - In this project, it seems the models are defined in files like `DDPM_2D.py`, `DDPM_2D_patched.py`, or `Spark_2D.py` in the `src/models/` directory.

3. Saving the Model:
   - PyTorch Lightning, which this project uses, typically saves the entire `LightningModule` in the checkpoint.
   - This includes the model architecture, current state, and other related components.

4. Loading the Model:
   - When you want to use the model, you would typically:
     1. Instantiate the model class
     2. Load the state from a checkpoint

So, to directly answer your question: No, a model checkpoint is not the model itself, but rather a saved state of the model that can be used to reconstruct the model at a specific point in its training.

The actual model definition and architecture would be in the Python code, likely in one of the files in the `src/models/` directory, depending on which specific model configuration is being used.
***
Based on the configuration files provided, models are saved in the following location:

1. In the `checkpoint.yaml` file, there is a ModelCheckpoint callback configured with:

```yaml
model_checkpoint:
    _target_: pytorch_lightning.callbacks.model_checkpoint.ModelCheckpoint
    dirpath: "checkpoints/"
    filename: "epoch-{epoch}_step-{step}_loss-{val/Loss_comb:.2f}"
```

This indicates that checkpoints will be saved in a directory called "checkpoints/" relative to the working directory.

2. In the `config.yaml` file, there is a variable defined:

```yaml
log_dir:  ${oc.env:LOG_DIR}
```

This suggests that the actual log directory (which likely includes the checkpoints) is set via an environment variable called LOG_DIR.

3. The `run.py` file likely uses these configurations to determine the final save location.

So in summary:

- Checkpoints are saved in a "checkpoints/" subdirectory
- The parent directory for this is likely specified by the LOG_DIR environment variable
- The full path would be something like: $LOG_DIR/checkpoints/

The exact filename of each checkpoint will follow the pattern:
"epoch-{epoch}_step-{step}_loss-{val/Loss_comb:.2f}"

To find the exact location on your system, you would need to check:
1. The value of the LOG_DIR environment variable
2. Any modifications made in the run.py file that might alter this path

If you need the exact absolute path, you may need to check the logs of a training run or inspect the running code to see how these configurations are applied.
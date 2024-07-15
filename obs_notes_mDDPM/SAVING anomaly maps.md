Certainly! I'll explain how you can use a trained model to generate anomaly maps for new, unseen data. This process typically involves loading the trained model, running inference on new data, and then generating the anomaly maps from the model's output. Here's a step-by-step guide:

1. Load the trained model:
   You'll need to load the best checkpoint saved during training. This is typically done using PyTorch Lightning's `load_from_checkpoint` method.

2. Preprocess your new data:
   Ensure your new data is preprocessed in the same way as the training data. This includes resizing, normalization, etc.

3. Run inference:
   Pass your preprocessed data through the model.

4. Generate anomaly maps:
   The anomaly map is typically the difference between the input image and the model's reconstruction.

5. Post-process and analyze the anomaly maps.

Here's a rough outline of how you might implement this:

```python
import torch
from pytorch_lightning import LightningModule
from src.models.DDPM_2D import DDPM_2D  # Adjust import path as needed
from src.datamodules.create_dataset import Eval  # Adjust import path as needed

# 1. Load the trained model
model_path = "path/to/your/best_checkpoint.ckpt"
model = DDPM_2D.load_from_checkpoint(model_path)
model.eval()  # Set the model to evaluation mode

# 2. Preprocess your new data
# Assuming you have a function to load and preprocess your data
new_data = load_and_preprocess_data("path/to/new/data")

# 3 & 4. Run inference and generate anomaly maps
anomaly_maps = []
with torch.no_grad():
    for batch in new_data:
        # Assuming your model's forward method returns the reconstruction
        reconstruction = model(batch)
        
        # Generate anomaly map (absolute difference between input and reconstruction)
        anomaly_map = torch.abs(batch - reconstruction)
        anomaly_maps.append(anomaly_map)

# 5. Post-process and analyze anomaly maps
# This step depends on your specific requirements, but might include:
# - Applying a threshold to binarize the anomaly map
# - Calculating statistics on the anomaly maps
# - Visualizing the anomaly maps
```

Regarding storage and viewing of anomaly maps:

1. Storage: Anomaly maps are typically not stored during training. They are generated during the evaluation or inference phase. However, you can save them during this process if needed.

2. Viewing: The code you shared includes a `log_images` function in the `utils_eval.py` file. This function is used to visualize input images, reconstructions, and anomaly maps. It's called in the `test_step` method if `self.cfg['saveOutputImages']` is True:

```python
if self.cfg['saveOutputImages']:
    log_images(self,diff_volume, data_orig, data_seg, data_mask, final_volume, ID)
```

To view anomaly maps for your new data, you could adapt this `log_images` function or create a similar visualization function.

To implement this in your existing codebase:

1. Create a new script (e.g., `generate_anomaly_maps.py`) that loads your trained model and new data.
2. Use the `Eval` class from `create_dataset.py` to preprocess your new data in the same way as during training/evaluation.
3. Implement the inference and anomaly map generation process as outlined above.
4. Use the `log_images` function or a similar visualization method to save or display the anomaly maps.

Remember to ensure that your new data is preprocessed identically to how the training data was processed, including any normalization, resizing, or other transformations. This is crucial for the model to perform correctly on the new data.
***

I apologize for the confusion. You're right, and I'll provide a more detailed explanation based on the code in your project. Let's walk through this process step by step, using the existing code structure.

1. Loading the trained model:

In the `train.py` file, there's a section for loading checkpoints:

```python
if cfg.get('load_checkpoint') and (cfg.get('onlyEval',False) or cfg.get('resume_train',False)):
    wandbID, checkpoints = utils.get_checkpoint(cfg, cfg.get('load_checkpoint'))
```

You would use this to load your trained model. Make sure `cfg.load_checkpoint` points to your saved model.

2. Preparing new data:

You'll need to create a new datamodule for your new data. Look at the `Datamodules_eval.py` file. You can create a new class similar to `Brats21` or `MSLUB`:

```python
class NewDataset(LightningDataModule):
    def __init__(self, cfg, fold=None):
        super(NewDataset, self).__init__()
        self.cfg = cfg
        # Setup paths and CSV files for your new dataset

    def setup(self, stage: Optional[str] = None):
        if not hasattr(self,'val_eval'):
            self.val_eval = create_dataset.Eval(self.csv['val'], self.cfg)
            self.test_eval = create_dataset.Eval(self.csv['test'], self.cfg)

    def val_dataloader(self):
        return DataLoader(self.val_eval, batch_size=1, num_workers=self.cfg.num_workers, pin_memory=True, shuffle=False)

    def test_dataloader(self):
        return DataLoader(self.test_eval, batch_size=1, num_workers=self.cfg.num_workers, pin_memory=True, shuffle=False)
```

3. Running inference and generating anomaly maps:

The `test_step` method in `DDPM_2D.py` already handles this. Here's the relevant part:

```python
def test_step(self, batch: Any, batch_idx: int):
    # ... (earlier code)
    
    loss_diff, reco = self.diffusion(input, input, t=self.test_timesteps-1, noise=noise)
    
    # ... (more code)
    
    final_volume = reco.clone().squeeze()
    final_volume = final_volume.permute(1,2,0) # to HxWxD
    
    # ... (more code)
    
    _test_step(self, final_volume, data_orig, data_seg, data_mask, batch_idx, ID, label)
```

The `_test_step` function in `utils_eval.py` generates the anomaly maps:

```python
def _test_step(self, final_volume, data_orig, data_seg, data_mask, batch_idx, ID, label_vol):
    # ... (earlier code)
    
    if self.cfg.get('residualmode','l1'): # l1 or l2 residual
        diff_volume = torch.abs((data_orig-final_volume))
    else:
        diff_volume = (data_orig-final_volume)**2
    
    # ... (more code)
```

4. Storing, inspecting, and analyzing anomaly maps:

The anomaly maps (stored in `diff_volume`) are processed and various metrics are calculated in the `_test_step` function. Results are stored in `self.eval_dict`:

```python
self.eval_dict['DiceScorePerVol'].append(diceScore)
self.eval_dict['AUCPerVol'].append(AUC)
self.eval_dict['AUPRCPerVol'].append(AUPRC)
# ... (more metrics)
```

For visualization, the `log_images` function is called if `saveOutputImages` is True:

```python
if self.cfg['saveOutputImages']:
    log_images(self,diff_volume, data_orig, data_seg, data_mask, final_volume, ID)
```

This function saves images to disk and logs them to wandb.

To use this existing structure with new data:

1. Create a new configuration file for your dataset in the `configs/datamodule/` directory.
2. Create a new datamodule class in `Datamodules_eval.py` for your dataset.
3. Modify the `train.py` script to load your trained model and new dataset:

```python
model = DDPM_2D.load_from_checkpoint(checkpoint_path)
datamodule = NewDataset(cfg)

trainer.test(model=model, datamodule=datamodule)
```

4. Run the modified script. This will:
   - Load your trained model
   - Load and preprocess your new data
   - Generate anomaly maps
   - Calculate metrics
   - Save visualizations (if configured)

5. After running, you can analyze the results:
   - Check the `self.eval_dict` for quantitative metrics
   - Look at the saved images for qualitative analysis
   - Examine the wandb logs for an overview of results

Remember to ensure your new data is preprocessed identically to the training data. You may need to adjust the `create_dataset.py` file to handle any specifics of your new dataset.

This process uses the existing code structure to generate, store, and analyze anomaly maps for new data. You're leveraging the test phase of the training process, but applying it to your new dataset.

***
Certainly! I'll provide a step-by-step guide to generate and store anomaly maps for a new dataset using your existing codebase. Let's go through this process in detail:

1. Prepare Your New Dataset:
   - Organize your new dataset in a similar structure to the existing datasets (like BraTS21 or MSLUB).
   - Create a CSV file listing the paths to your images, similar to the ones used for other datasets.

2. Create a New Datamodule:
   - Open `src/datamodules/Datamodules_eval.py`.
   - Add a new class for your dataset, similar to the existing ones:

     ```python
     class NewDataset(LightningDataModule):
         def __init__(self, cfg, fold=None):
             super(NewDataset, self).__init__()
             self.cfg = cfg
             self.csvpath_test = "path/to/your/new_dataset_test.csv"
             self.csv = {}
             self.csv['test'] = pd.read_csv(self.csvpath_test)
             # Set up paths and other necessary configurations

         def setup(self, stage: Optional[str] = None):
             if not hasattr(self, 'test_eval'):
                 self.test_eval = create_dataset.Eval(self.csv['test'], self.cfg)

         def test_dataloader(self):
             return DataLoader(self.test_eval, batch_size=1, num_workers=self.cfg.num_workers, pin_memory=True, shuffle=False)
     ```

3. Create a Configuration File:
   - In the `configs/datamodule/` directory, create a new YAML file for your dataset (e.g., `new_dataset.yaml`).
   - Include necessary configurations, similar to existing ones like `IXI.yaml`.

4. Modify the Main Configuration:
   - Open `configs/config.yaml`.
   - Under the `defaults` section, add your new dataset:
     ```yaml
     defaults:
       - datamodule: new_dataset.yaml
     ```

5. Set `saveOutputImages` to True:
   - In your dataset's configuration file (e.g., `new_dataset.yaml`) or in the main `config.yaml`, add:
     ```yaml
     model:
       cfg:
         saveOutputImages: True
     ```

6. Create a Script to Run Inference:
   - Create a new Python script, e.g., `generate_anomaly_maps.py`:

     ```python
     import hydra
     from omegaconf import DictConfig
     from pytorch_lightning import Trainer
     from src.models.DDPM_2D import DDPM_2D
     from src.datamodules.Datamodules_eval import NewDataset

     @hydra.main(config_path="configs", config_name="config.yaml")
     def main(cfg: DictConfig):
         # Load the trained model
         model = DDPM_2D.load_from_checkpoint(cfg.checkpoint_path)
         
         # Initialize the datamodule for the new dataset
         datamodule = NewDataset(cfg)
         
         # Initialize trainer
         trainer = Trainer(gpus=1)  # Adjust as needed
         
         # Run inference
         trainer.test(model, datamodule=datamodule)

     if __name__ == "__main__":
         main()
     ```

7. Run the Script:
   - Execute the script:
     ```
     python generate_anomaly_maps.py checkpoint_path=/path/to/your/trained/model.ckpt
     ```

8. Analyze the Results:
   - The anomaly maps will be saved in the directory specified by `cfg.log_dir` (check your configuration files).
   - The `log_images` function in `utils_eval.py` saves the following for each sample:
     - Original image
     - Reconstructed image
     - Anomaly map (difference between original and reconstruction)
     - Segmentation mask (if available)
   - These images are saved as PNG files and also logged to WandB if you're using it.

9. Quantitative Analysis:
   - After running, check the `self.eval_dict` in the model. It contains various metrics like DICE scores, AUC, etc.
   - These metrics are also logged to WandB and saved in the experiment logs.

10. Further Analysis:
    - You can load the saved PNG files of the anomaly maps for further analysis or visualization.
    - If you need raw data of the anomaly maps, you might need to modify the `_test_step` function in `utils_eval.py` to save the `diff_volume` tensor directly, for example using `torch.save()`.

Remember to ensure that your new dataset is preprocessed in the same way as the training data. This typically involves normalization, resizing, and any other transformations applied during training.

This process utilizes your existing codebase to generate anomaly maps for a new dataset, saving both visual representations and quantitative metrics for analysis.
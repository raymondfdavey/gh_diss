Yes, this situation should be fine given the way the code is designed to handle different modalities. Here's why:

1. Dynamic Path Adjustment:
   The code in `Datamodules_eval.py` for BraTS21 includes this logic:

   ```python
   if cfg.mode != 't1':
       self.csv[state]['img_path'] = self.csv[state]['img_path'].str.replace('t1', cfg.mode).str.replace('FLAIR.nii.gz', f'{cfg.mode.lower()}.nii.gz')
   ```

2. How It Works:
   - When the system is set to use T2 images (i.e., `cfg.mode == 't2'`), it will automatically replace 't1' with 't2' in the file paths.
   - So, a path like `Test/Brats21/t1/BraTS2021_01171_t1.nii.gz` would be transformed to `Test/Brats21/t2/BraTS2021_01171_t2.nii.gz`.

3. Your Specific Case:
   - Even though you don't have the T1 file (`BraTS2021_01171_t1.nii.gz`), you do have the corresponding T2 file (`BraTS2021_01171_t2.nii.gz`).
   - When the system is configured to use T2 images, it will look for exactly this T2 file.

4. Implications:
   - This means the system should work correctly with your T2 images, even if some or all of the T1 images are missing.
   - The important thing is that the T2 images follow the expected naming convention and directory structure.

5. Potential Considerations:
   - Make sure that your configuration is set to use T2 images (`cfg.mode = 't2'` or equivalent).
   - Ensure that all the subjects you want to process have T2 images available.
   - If you're planning to use both T1 and T2 in different runs, you might need to adjust your dataset or configuration to account for the missing T1 images.

In conclusion, your setup with only T2 images present should work fine as long as:
1. The system is configured to use T2 images.
2. The T2 images are in the expected location with the correct naming convention.
3. You're not trying to run any processes that specifically require T1 images.

The flexibility of the code in handling different modalities is designed precisely for situations like this, where you might have data available in one modality but not another.
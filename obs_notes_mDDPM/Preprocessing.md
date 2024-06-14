Summary below, commentary on the actual [[proprocessing code and scripts]] is elsewhere.

They say:

We preprocess the data by resampling it to 1.0 mm, skull-stripping with HD-BET, registering it to the SRI Atlas, removing the black boarders, and correcting for N4 bias. 

You must clone and set up the [HD-BET](https://github.com/MIC-DKFZ/HD-BET) tool for skull-stripping in order to conduct the preprocessing.  

The preprocessing is carried out via a separate bash script for each data set in the [preprocessing](https://file+.vscode-resource.vscode-cdn.net/c:/Users/rd81/OneDrive%20-%20University%20of%20Sussex/Desktop/diss_git/mDDPM/preprocessing) directory. Go to the [preprocessing](https://file+.vscode-resource.vscode-cdn.net/c:/Users/rd81/OneDrive%20-%20University%20of%20Sussex/Desktop/diss_git/mDDPM/preprocessing) directory to preprocess the data.

This means

1. Resampling to 1.0 mm:
    - In medical imaging, data is acquired in a 3D grid of voxels (volumetric pixels). The size of these voxels can vary depending on the scanner and acquisition parameters.
    - Resampling to 1.0 mm means changing the size of the voxels so that each voxel represents a 1.0 mm × 1.0 mm × 1.0 mm cube of the brain.
    - This step standardizes the spatial resolution of all the images in the dataset, making them directly comparable and easier to work with in subsequent analysis steps.
2. Skull-stripping with HD-BET:
    - Skull-stripping is the process of removing non-brain tissue, such as the skull, scalp, and other surrounding structures, from the MRI scans.
    - HD-BET (Hybrid Deep Brain Extraction Tool) is a specific tool used for this purpose. It uses deep learning algorithms to accurately segment the brain tissue from the non-brain tissue.
    - Skull-stripping focuses the analysis on the brain region of interest and reduces the influence of non-brain structures on subsequent processing steps.
3. Registering to the SRI Atlas:
    - Registration is the process of aligning or spatially mapping one image to another. In this case, the skull-stripped brain images are aligned to a standard brain atlas called the SRI Atlas.
    - The SRI Atlas is a reference brain template that represents a standardized coordinate space. By registering individual brain scans to this atlas, all the images are brought into a common space.
    - Registration allows for direct comparison of brain structures across subjects and enables the use of atlas-based segmentation and analysis techniques.
4. Removing black borders:
    - During image acquisition or previous preprocessing steps, black borders (i.e., regions with zero intensity values) may be introduced around the brain image.
    - Removing these black borders helps to focus on the relevant brain regions and reduces the computational overhead of processing unnecessary background voxels.
5. N4 bias correction:
    - MRI scans can suffer from intensity inhomogeneities, also known as bias fields. These are smooth, low-frequency variations in image intensity across the brain.
    - N4 bias correction is an algorithm that estimates and corrects for these intensity inhomogeneities.
    - By applying N4 bias correction, the intensity values across the brain are normalized, making the images more consistent and improving the accuracy of subsequent analysis steps.

To perform this preprocessing pipeline, you need to set up the HD-BET tool by cloning its repository from GitHub. HD-BET is specifically used for the skull-stripping step.

The preprocessing scripts for each dataset are located in the "preprocessing" directory. To preprocess the data, you should navigate to that directory and execute the corresponding bash script for each dataset.

In summary, this preprocessing pipeline takes raw MRI scans and applies a series of steps to standardize the data, remove non-brain tissue, align the images to a common space, and correct for intensity inhomogeneities. These steps are crucial for ensuring data quality and comparability, enabling subsequent analysis and modeling tasks to be performed more effectively.

[[preprocess new data]] 


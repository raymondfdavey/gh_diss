Basically downloaded original data from - 
IXI: [https://brain-development.org/ixi-dataset/](https://brain-development.org/ixi-dataset/)
BraTS21: [http://braintumorsegmentation.org/](http://braintumorsegmentation.org/)
MSLUB: [https://lit.fe.uni-lj.si/en/research/resources/3D-MR-MS/](https://lit.fe.uni-lj.si/en/research/resources/3D-MR-MS/)
Then reorganised into the format they specified by scripts written here so in
├── IXI
│   ├── t2 
│   │   ├── IXI1.nii.gz
│   │   ├── IXI2.nii.gz
│   │   └── ... 
│   └── ...
├── MSLUB
│   ├── t2 
│   │   ├── MSLUB1.nii.gz
│   │   ├── MSLUB2.nii.gz
│   │   └── ...
│   ├── seg
│   │   ├── MSLUB1_seg.nii.gz
│   │   ├── MSLUB2_seg.nii.gz
│   │   └── ...
│   └── ...
├── Brats21
│   ├── t2 
│   │   ├── Brats1.nii.gz
│   │   ├── Brats2.nii.gz
│   │   └── ...
│   ├── seg
│   │   ├── Brats1_seg.nii.gz
│   │   ├── Brats2_seg.nii.gz
│   │   └── ...
│   └── ...
└── ...
Format
Checking if the original filenames work with my current processimg pipeline

if so to reply to Finn with it working!!!!

if not work on that 
fingers crossed
bit of gentle pytorch lightening introduction

RENAMING WORKS as long as files n this format:

<DATA_DIR> 
--IXI_clean 
----t2 
--------IXI012-HH-1211-T2.nii.gz 
--------IXI002-Guys-0828-T2.nii.gz 

--BraTS21_clean 
----t2 
--------BraTS-GLI-00000-000-t2w.nii.gz 
--------BraTS-GLI-00002-000-t2w.nii.gz 

----seg 
--------BraTS-GLI-00000-000-seg.nii.gz 
--------BraTS-GLI-00002-000-seg.nii.gz 
 
--MSLUB_clean 
----t2 
--------patient01_T2W.nii.gz 
--------patient02_T2W.nii.gz 

--seg 
--------patient01_consensus_gt.nii.gz
--------patient02_consensus_gt.nii.gz 

becomes:

<DATA_DIR> 
--IXI_clean 
----t2 
--------IXI012-HH-1211_t2.nii.gz 
--------IXI002-Guys-0828_t2.nii.gz 

--BraTS21_clean 
----t2 
--------BraTS-GLI-00000-000_t2.nii.gz 
--------BraTS-GLI-00002-000_t2.nii.gz 

----seg 
--------BraTS-GLI-00000-000_seg.nii.gz 
--------BraTS-GLI-00002-000_seg.nii.gz 
 
--MSLUB_clean 
----t2 
--------patient01_t2.nii.gz 
--------patient02_t2.nii.gz 

--seg 
--------patient01_seg.nii.gz
--------patient02_seg.nii.gz 


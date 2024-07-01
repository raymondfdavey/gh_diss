***

27th June
Today I have been trying to get the scripts working with mps and hd bet workig.

I got updated hd bet to download correctly, then I have been experimenting with the mps setting. 
Basically there is part of the hd-bet prcoess that does not work with mps, so I have tried to allow pytorch to fall back to cpu when needed. 
```
PYTORCH_ENABLE_MPS_FALLBACK=1 hd-bet -i $DATA_DIR/v1resampled/IXI/t2 -o $DATA_DIR/v2skullstripped/IXI/t2 -device mps -mode fast -tta 0
```

This code is super fast and great, BUT i was curious about the flags. when I ran:
```
PYTORCH_ENABLE_MPS_FALLBACK=1 hd-bet -i $DATA_DIR/v1resampled/IXI/t2 -o $DATA_DIR/v2skullstripped/IXI/t2 -device mps
```

It is mega crazy stupid slow, so I asked clause who reckons:

the fast flag determines fast or accurate.
in fast one set of params is used, in accurate then 5 sets are used
tta is [[test time augmentation]] which is a big deal and takes a long lomng time

so the compromise may be 

`PYTORCH_ENABLE_MPS_FALLBACK=1 hd-bet -i $DATA_DIR/v1resampled/IXI/t2 -o $DATA_DIR/v2skullstripped/IXI/t2 -device mps -tta 0`

this switches off tta but keeps the multi level checks
I actually just used the fast one to test things

In terms of other changes, there was some learning to be done about how the registration and cut pythorn scripts worked - it turns out although they take only the t2 directory, within the scripts they go looking for segmentation directory and do the same on that, this has to be dealt with in mslub.

more majorly, the BRATS dataset had a bit more goin gon in its preprocessing. It is already skull stripped and resampled so these parts of the pipeline were not required. however this meant there was some naming issues when it came to registration as the resampling stages actually did some renaming. luckily this was found and resolved.

but then the next bit was more interesting - as the data had alreadsy been skul stripped there was no 'mask' and so i discovered that the code actually created a mask (OR ANTS DOES) from the skill stripped image by turning black space into mask. Interesting. As in it sort of retrospectively derives a mask from the black space in the image.  but anyway the code then didnt use this mask for bias field correction, which seemed to be due to directory naming errors so i fixed this too. 
***




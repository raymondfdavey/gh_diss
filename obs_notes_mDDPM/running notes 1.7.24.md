- checking mini data pre prcessing still working
- added to script code to reorganise the code into the desired format for training
- added to running script so it takes all paths as params

- it seems that I should not have removed the file names so much intially?
- but those in the splits csv files are really weird like tey are all t1 images????? wtf
***
sit rep
	- script takes and preprocessed everything fine
	- concerns regarding filenames but I can't look into that until I have original images

MOVING ON TO RUNNING THE MODEL:
\
`You should then specify the path the location of <DATA_DIR> in the pc_environment.env file. Additionally, specify the <LOG_DIR>.`

env creation with  [[NO CONDA]] 

had to use `requirements_versionless.txt`

git ignored SRI atlas and all of the mad packages that you need for training

Got very concerned about the FOLD.csv files which all seemed to refer to T1 files whereas the model uses t2. However, the code handles this dynamically and so the  [[t1-t2 mismatch]] is actually not an issue. 

So now all I have to do is get the data into the correct format, check that it is dealt with fine (on mini sample) and then try running the training!!!!!!!!


It is all handled by the mode: 't2' bit in all of the yamls
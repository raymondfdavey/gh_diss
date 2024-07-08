In the provided scripts, there are two required command-line arguments:

1. `INPUT_DIR`: The path to the input data directory. This directory should contain the raw or source data that needs to be preprocessed.

2. `DATA_DIR`: The path to the output directory where the preprocessed data will be saved. The scripts will create subdirectories within this output directory to store the intermediate and final results of the preprocessing pipeline.

The scripts expect these arguments to be provided in the specified order when running the script from the command line. For example:

```
./prepare_IXI.sh /path/to/input/data /path/to/output/directory
```

The scripts also include some error handling to ensure that both arguments are provided and that the `INPUT_DIR` is an absolute path (not a relative path like "." or ".."). If either of the arguments is missing or if the `INPUT_DIR` is a relative path, the script will display an error message and exit.

Here's the relevant code snippet from the scripts that handles the command-line arguments:

```bash
# cli arguments: 
# 1. path to data directory
# 2. path to output directory
INPUT_DIR=$1
DATA_DIR=$2

# make the arguments mandatory and that the data dir is not a relative path
if [ -z "$INPUT_DIR" ] || [ -z "$DATA_DIR" ] 
then
  echo "Usage: ./prepare_IXI.sh <input_dir> <output_dir>"
  exit 1
fi

if [ "$INPUT_DIR" == "." ] || [ "$INPUT_DIR" == ".." ]
then
  echo "Please use absolute paths for input_dir"
  exit 1
fi
```

This code assigns the first command-line argument to the `INPUT_DIR` variable and the second argument to the `DATA_DIR` variable. It then checks if either of the arguments is empty or if the `INPUT_DIR` is a relative path, and displays an appropriate error message if the conditions are not met.

So, in summary, the two required arguments for these scripts are:
1. The path to the input data directory.
2. The path to the output directory where the preprocessed data will be saved.
## Installing FastSurferCNN 
### For Linux/Ubuntu users:
    - Create conda environment using ```conda env create -f <path_of_fastsurfer.yml>```
    - Activate the environment using ```conda activate fastsurfer```
    - Add the directory parent to ```FastSurferCNN``` to ```PYTHONPATH``` using ```export PYTHONPATH="${PYTHONPATH}:$PWD"```
### For Windows users:
    - - Create conda environment using ```conda env create -f <path_of_fastsurfer.yml>```
    - Activate the environment using ```conda activate fastsurfer```
    - Add the directory parent to ```FastSurferCNN``` to ```PYTHONPATH``` using ```$env:PYTHONPATH = "$PWD;$env:PYTHONPATH"```


## Running FastSurferCNN
    - Run ```python run_prediction.py``` with arguments. Run ```python run_prediction.py --help``` to get information about the arguments.
    - Note: For Windows, DLL import errors may occur. Try to force reinstall the libraries that are causing the error and also the Conda distribution.
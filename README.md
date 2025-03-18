# Installing FastSurferCNN 

## For Linux/Ubuntu users:
1. Create a conda environment using:
    ```bash
    conda env create -f <path_of_fastsurfer.yml>
    ```
2. Activate the environment:
    ```bash
    conda activate fastsurfer
    ```
3. Add the directory parent to `FastSurferCNN` to `PYTHONPATH`:
    ```bash
    export PYTHONPATH="${PYTHONPATH}:$PWD"
    ```

---

## For Windows users:
1. Create a conda environment using:
    ```powershell
    conda env create -f <path_of_fastsurfer.yml>
    ```
2. Activate the environment:
    ```powershell
    conda activate fastsurfer
    ```
3. Add the directory parent to `FastSurferCNN` to `PYTHONPATH`:
    ```powershell
    $env:PYTHONPATH = "$PWD;$env:PYTHONPATH"
    ```

---

# Running FastSurferCNN
1. Run `python run_prediction.py` with arguments:
    ```bash
    python run_prediction.py --help
    ```
    Use `--help` to see available arguments.

2. **Note:** On Windows, you might encounter DLL import errors. To resolve this:
    - Try force reinstalling the libraries causing the error.
    - Also, try reinstalling Conda distribution.

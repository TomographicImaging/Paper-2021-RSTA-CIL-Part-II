## 1) **Install the environment**

**Note:** Depending on your nvidia-drivers, you can modify the `cudatoolkit` parameter. See [here](https://docs.nvidia.com/deploy/cuda-compatibility/index.html) for more information.

```bash
conda create --name cil2_demos -c conda-forge -c astra-toolbox/label/dev -c ccpi cil cil-astra ccpi-regulariser nb_conda_kernels jupyterlab scikit-image cudatoolkit=_._
```      

## 2) **Activate the environment**

```bash
conda activate cil2_demos
```

## 3) **Install wget (via pip)**

**Note:** We use `wget` package to download all the real tomographic data directly from `Zenodo`.

```bash
pip install wget
```

## **Create the environment from the requirements.yml file:**

```bash
conda env create -f environment.yml
```
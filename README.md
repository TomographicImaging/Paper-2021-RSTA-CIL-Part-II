This code reproduces all the results presented in **[Core Imaging Library part II: multichannel reconstruction
for dynamic and spectral tomography**](https://doi.org/10.1098/rsta.2020.0193).

![](images.png)

# Instructions

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

# **Create the environment from the requirements.yml file:**

```bash
conda env create -f environment.yml
```

## There are 3 directories for 3 different case studies:

- **CaseStudy_ColourProcessing (Section 3)** :
    
    1. Color Denoising
    1. Color Inpainting
    <br></br>
        
- **CaseStudy_DynamicTomography (Section 4)** :   

    1. LoadData_CreateSparseData
    1. FBP_reconstructions
    1. TikhonovReconstructions
    1. TVReconstructions
    1. dTVReconstructions
    1. ShowFigure
    <br></br>
    
- **CaseStudy_HyperspectralTomography (Section 5)** :

    1. LoadRawDataAndCrop
    1. PreProcessRingRemover
    1. SIRT_reconstructions
    1. SPDHG_SpatioSpectralTV
    1. SPDHG_3D_spectral_TV
    1. PDHG_SpatioSpectralTV
    1. ShowFigures
    <br></br>
    
# CITE
    
Papoutsellis E et al. 2021 Core imaging library part II: multichannel reconstruction for dynamic and spectral tomography. Phil. Trans. R. Soc. A 20200193.           https://doi.org/10.1098/rsta.2020.0193)


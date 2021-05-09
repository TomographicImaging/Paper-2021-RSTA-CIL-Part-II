import os
import wget

def download_zenodo():
    
    if os.path.exists("MatlabData"):
        pass
    else:
        print("Download files from Zenodo ... ")
        os.mkdir("MatlabData")
        wget.download("https://zenodo.org/record/4157615/files/Au_rock_scan_geometry.txt", out="MatlabData")
        wget.download("https://zenodo.org/record/4157615/files/Au_rock_sinogram_full.mat", out="MatlabData")
        wget.download("https://zenodo.org/record/4157615/files/commonX.mat", out="MatlabData")
        wget.download("https://zenodo.org/record/4157615/files/FF.mat", out="MatlabData")
        print("Finished.")        
            
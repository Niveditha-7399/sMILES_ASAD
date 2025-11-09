# sMILES_ASAD
Collection of scripts that assist with a research project that analyzes observed spectral data of star clusters using full-spectrum fitting with sMILES models. The scripts are designed for using with Analyzer of integrated Spectra for Age, henceforth abbreviated in this project as ASAD. 

## filter_sMILES_models.py
This script filters observations by providing the indices of observations to be removed.

## BC03_all_model_compilation.py
This script is used to create a single model file from a folder full of BC03 (Bruzual & Charlot 2003) models. It creates a single model file to be compatible with Analyzer of integrated Spectra for Age.

## BC03_filtered_model_compilation.py
This script is used to create a single model file from a folder full of BC03 (Bruzual & Charlot 2003) models but retaining only the models mentioned in a text document 'base_info_file'. It creates a single model file to be compatible with Analyzer of integrated Spectra for Age.

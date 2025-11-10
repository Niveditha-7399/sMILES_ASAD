# sMILES_ASAD
Collection of scripts that assist with a research project that analyzes observed spectral data of star clusters using full-spectrum fitting with sMILES models. The scripts are designed for using with Analyzer of integrated Spectra for Age, henceforth abbreviated in this project as ASAD. 

## filter_sMILES_models.py
This script filters observations by providing the indices of observations to be removed.
Input:
- source_folder is the folder with all models in TXT format.
Output:
- destination_folder is folder with the filtered models.
  
## BC03_all_model_compilation.py
This script is used to create a single model file from a folder full of BC03 (Bruzual & Charlot 2003) models. It creates a single model file to be compatible with Analyzer of integrated Spectra for Age.
Input:
- input_folder is the folder with all the models in TXT format to be compiled.
Output:
- output_file is the name of the compiled model in TXT document.

## BC03_filtered_model_compilation.py
This script is used to create a single model file from a folder full of BC03 (Bruzual & Charlot 2003) models but retaining only the models mentioned in a text document 'base_info_file'. It creates a single model file to be compatible with Analyzer of integrated Spectra for Age.
Input: 
- input_folder is the folder with all models in TXT format.
- base_info_file is the output file with the filtered models (the ones to keep in the final output).
Output:
- output_file is the compiled mode with just the desired models.

## BC03_results_indexing.py
This script is used for reading the results obtained from the full-spectrum fitting performed with Analyzer of integrated Spectra for Age, using the BC03 (Bruzual & Charlot 2003) models.

Input:
- results_file is the results file txt document.
- info_file is the bc03 model Index to age, metallicity information matching document.
Output:
- output_csv is the name of the results file with the matched information added to it.

##############################################################
"""
This code is created by Niveditha Parthasarathy
and it is useful for filtering the sMILES models
to create observation sets.
"""
##############################################################

#Importing Packages
import os
import shutil


#This is a loop that is relevant to my models
#The models that I wished to remove had a pattern
##in their file name, so this code is used to retrieve their indeces
def get_listt():
    a=[]
    num=46

    for i in range(58):
        current=num
        for i in range(5):
            a.append(current)
            current+=1
        num+=50
    return a


def new_smiles():

    #This folder will have the complete set of models
    source_folder = "observations_smiles"

    #This folder will contain models that are not at Index defined by
    #the numbers in remove_numbers list
    destination_folder = "observations_match" # New folder to create
    remove_numbers = get_listt()
    #Firstly, a copy of the source_folder is created as the desired folder
    if os.path.exists(destination_folder):
        shutil.rmtree(destination_folder)

    shutil.copytree(source_folder, destination_folder)
    print(f"Copied '{source_folder}' to '{destination_folder}'.")

    #All files that are at Index: remove_numbers are removed from the (copy) folder
    for num in remove_numbers:
        #This is the way I have named the model files
        filename = f"smiles_obs_{num}.txt"
        filepath = os.path.join(destination_folder, filename)

        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"Removed model: {filename}")
        else:
            print(f"File not found (so I skipped): {filename}")

    print("Process has completed.")





new_smiles()

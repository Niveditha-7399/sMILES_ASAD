def new_smiles():
    import os
    import shutil

    #This folder will have the complete set of models
    source_folder = "observations_smiles"

    #This folder will contain models that are not at Index defined by
    #the numbers in remove_numbers list
    destination_folder = "observations_match" # New folder to create
    remove_numbers = [46, 47, 48, 49, 50, 96, 97, 98, 99, 100, 146, 147, 148, 149, 150, 196, 197, 198, 199, 200, 246, 247, 248, 249, 250, 296, 297, 298, 299, 300, 346, 347, 348, 349, 350, 396, 397, 398, 399, 400, 446, 447, 448, 449, 450, 496, 497, 498, 499, 500, 546, 547, 548, 549, 550, 596, 597, 598, 599, 600, 646, 647, 648, 649, 650, 696, 697, 698, 699, 700, 746, 747, 748, 749, 750, 796, 797, 798, 799, 800, 846, 847, 848, 849, 850, 896, 897, 898, 899, 900, 946, 947, 948, 949, 950, 996, 997, 998, 999, 1000, 1046, 1047, 1048, 1049, 1050, 1096, 1097, 1098, 1099, 1100, 1146, 1147, 1148, 1149, 1150, 1196, 1197, 1198, 1199, 1200, 1246, 1247, 1248, 1249, 1250, 1296, 1297, 1298, 1299, 1300, 1346, 1347, 1348, 1349, 1350, 1396, 1397, 1398, 1399, 1400, 1446, 1447, 1448, 1449, 1450, 1496, 1497, 1498, 1499, 1500, 1546, 1547, 1548, 1549, 1550, 1596, 1597, 1598, 1599, 1600, 1646, 1647, 1648, 1649, 1650, 1696, 1697, 1698, 1699, 1700, 1746, 1747, 1748, 1749, 1750, 1796, 1797, 1798, 1799, 1800, 1846, 1847, 1848, 1849, 1850, 1896, 1897, 1898, 1899, 1900, 1946, 1947, 1948, 1949, 1950, 1996, 1997, 1998, 1999, 2000, 2046, 2047, 2048, 2049, 2050, 2096, 2097, 2098, 2099, 2100, 2146, 2147, 2148, 2149, 2150, 2196, 2197, 2198, 2199, 2200, 2246, 2247, 2248, 2249, 2250, 2296, 2297, 2298, 2299, 2300, 2346, 2347, 2348, 2349, 2350, 2396, 2397, 2398, 2399, 2400, 2446, 2447, 2448, 2449, 2450, 2496, 2497, 2498, 2499, 2500, 2546, 2547, 2548, 2549, 2550, 2596, 2597, 2598, 2599, 2600, 2646, 2647, 2648, 2649, 2650]

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
    print(a)


new_smiles()
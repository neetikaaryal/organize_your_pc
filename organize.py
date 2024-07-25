import os

folder_path = "/home/dpaisa/Downloads/"
# print(os.listdir(folder_path))
folders = {
    "image" : ["img", "png", "jpg", "jpeg"],
    "deb" : ["deb"],
}

def assign_folder(extension:str)->str | bool:
    for folder_name in folders:
        # print(folder_name)
        folder_ext = folders[folder_name]
        # print(folder_ext)
        if extension in folder_ext:
            return folder_name
        else:
            return False    
        
folder_name = assign_folder("pdf")
print(folder_name)
for i in os.listdir(folder_path):
    # print(i)
    if "." in i:
        # print("file")
        extention = i.split(".")[1]
        print(extention)
        folder_name =  assign_folder(extention)
    else:
        print("folder")
import os

def rename_files():
    # 1. get file names from a folder
     file_list = os.listdir(r"F:\Programming\Full stack web development\FullStackWebDevelopment\alphabet")
     print(file_list)
     saved_path = os.getcwd()
     print("Current Working Directory is " + saved_path)
     os.chdir(r"F:\Programming\Full stack web development\FullStackWebDevelopment\alphabet")

     # 2. for each file, rename filename
     for file_name in file_list:
         translation_table = dict.fromkeys(map(ord, "0987654321"), None)
         new_name = file_name.translate(translation_table)
         print("Old name - " + file_name)
         print("To - " + new_name)
         os.rename(file_name, new_name)
     os.chdir(saved_path)
rename_files()

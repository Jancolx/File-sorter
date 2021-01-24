import os 
import shutil 
   
path=input("Enter the path/directory for sort: ")
  

list_ = os.listdir(path) 
print(list)

for file_ in list_: 
    name, ext = os.path.splitext(file_) 
    ext = ext[1:] 
    if ext == '': 
        continue
#file creation and insertion:
    if os.path.exists(path+'/'+ext): 
       shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_) 

    else: 
        os.makedirs(path+'/'+ext) 
        shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_) 
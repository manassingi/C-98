import os
import shutil
os.system("date")
# os.mkdir("back.py")
#os.getcwd()
path="/Users/manassingi/Desktop/python/C-99/module.js"
#isExist=os.path.exists(path)
#print(isExist)
#root_ext=os.path.splitext(path)
#print("rootpart",root_ext[0])
#print("ext part",root_ext[1])
#os.listdir()
path ='/Users/manassingi/Desktop/'
print(os.listdir(path))
source="/Users/manassingi/Desktop/python/C-99/module.py"
destination="/Users/manassingi/Desktop/python/C-98/module(copy).py"
dest=shutil.copy(source,destination)
print(os.listdir(path))
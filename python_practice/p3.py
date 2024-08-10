import shutil
import os
print(os.getcwd())
os.mkdir("A")
file=open("A/blank.txt", 'x')
file.close()
os.mkdir("B")





shutil.copyfile("A/blank.txt","B/file.txt")




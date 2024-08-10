'''Write a program to move a file in directory 'source' and copy it to 'destination'. Handle necessary exceptions:
1. if file does not exists in source, print "no file found in source".
2. if same file already exists in target, print "file with same name already exists"'''

shutil.move(source_path, destination_path)
import shutil
import os
print(os.getcwd())
os.mkdir("source")
file=open("source/blank.txt", 'x')
file.close()

def move_file():
    source_path = 'source/blank.txt'
    destination_path = 'destination/file.txt'

    if not os.path.isfile(source_path):
        print("No file found in source.")
        return

   
    if os.path.isfile(destination_path):
        print("File with same name already exists.")
        return

    os.mkdir("destination")
    shutil.move("source/blank.txt","destination/file.txt")
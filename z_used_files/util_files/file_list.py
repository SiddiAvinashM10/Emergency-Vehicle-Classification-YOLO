import os
f = open("labels.txt", 'a')
for folder in os.listdir('.'):
    if folder == "rename.py" or folder == "labels.txt":
        continue
    a,class_name = folder.split('-')
    f.write(class_name+'\n')
    #print(class_name)
import os

imdir = 'images1'
if not os.path.isdir(imdir):
    os.mkdir(imdir)

fidget_folders = [folder for folder in os.listdir('.') if 'n' in folder]

for folder in fidget_folders:
    for imfile in os.scandir(folder):
        print(imfile.name)
        os.rename(imfile.path,os.path.join(imdir, imfile.name))
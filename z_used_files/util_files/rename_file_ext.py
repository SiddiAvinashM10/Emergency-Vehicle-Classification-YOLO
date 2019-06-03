import os

imdir = 'annotations'
if not os.path.isdir(imdir):
    os.mkdir(imdir)

fidget_folders = [folder for folder in os.listdir('.') if 'images1' in folder]


for folder in fidget_folders:
    for imfile in os.scandir(folder):
        os.rename(imfile.path, os.path.join(imdir,'{}.xml'.format(imfile.name)))
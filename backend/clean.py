import subprocess

paths = ['dataset/val_img/', 'dataset/val_label/', 'dataset/val_inst/']

for path in paths:
    subprocess.run(['rm', path + '*'])

subprocess.run(['ls', '-R', 'dataset/'])
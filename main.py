import csv
import os
import shutil

files = []
pasteDir = r"" # populate this with the destination folder you want the files to be copied into


# recursively digs down to the bottom of directories until there are not directories contained, only files
# then returns filenames
def subExtract(subpath):
    # print(subpath)
    listDir = os.listdir(subpath)
    # print(listDir)
    for i in listDir:
        subSubPath = subpath + "\\" + i
        if os.path.isdir(subSubPath):
            # print("directory")
            subExtract(subSubPath)
        elif os.path.isfile(subSubPath):
            # print("file")
            files.append(subSubPath)


# breaks down initial parent directory and then calls subextract function
def extract(filepath):
    cwd = os.getcwd()
    # print(cwd)
    workingDir = cwd + '\\' + filepath
    # print(workingDir)
    listDir = os.listdir(filepath)
    for i in listDir:
        sub1 = workingDir + "\\" + i
        if os.path.isdir(sub1):
            # print("directory")
            subExtract(sub1)
        if os.path.isfile(sub1):
            # print("file")
            files.append(sub1)
            continue


# accepts a list of folders containing the audit files and iteratively runs extract method
if __name__ == "__main__":
    filepaths = [""]  # populate this list with the folders you want to pull files from
    for i in filepaths:
        extract(i)
    # strips out filenames and outputs a list of them
    # then makes copies of the files into a singular folder
    outFile = 'out.csv'
    with open(outFile, mode='w', newline='') as file:
        writer = csv.writer(file)
        for i in files:
            shutil.copy(i, pasteDir)
            print(os.path.basename(i))
            writer.writerow([os.path.basename(i)])

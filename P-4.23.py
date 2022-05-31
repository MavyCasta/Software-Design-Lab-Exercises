import os

for path, currentDirectory, files in os.walk("E:\PYTHON PROJECTS\SD Laboratory Report No 4"):
    for file in files:
        print(os.path.join(path, file))
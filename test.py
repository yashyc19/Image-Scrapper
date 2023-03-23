# Description: Test file for imageList.txt
def updateImageList(data):
    with open("imageList.txt", "a") as f:
        f.write(f'{data}\n')

# read imageList.txt line by line
def readImageList():
    with open("imageList.txt", "r") as f:
        return f.readlines()

print(readImageList())
import os


def addToFile(fileName, link):
    if not os.path.exists('textfiles/'):
        os.mkdir('textfiles/')
    with open(f'textfiles/{fileName}.txt', 'a') as file:
        file.write(f'{link}\n')


def readFromFile(fileName):
    # if file exists return data
    if os.path.exists(f"textfiles/{fileName}.txt"):
        with open(f"textfiles/{fileName}.txt", 'r') as file:
            return file.read()
    else:
        return None

def imageFolder(fileName):
    # if file exists
    if os.path.exists(f"textfiles/{fileName}.txt"):
        # read file
        with open(f"textfiles/{fileName}.txt", 'r') as file:
            links = file.read().splitlines()
    # image folder
    if not os.path.exists(f'images/{fileName}/'):
        os.makedirs(f'images/{fileName}/')

# addToFile('jenna_ortega', link='jenna_ortega')
# print(readFromFile(fileName='jenna_ortega'))
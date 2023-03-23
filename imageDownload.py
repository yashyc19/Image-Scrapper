import shutil
import requests
import os


# download images from a text file
def readLinks(fileName):
    if not os.path.exists(f'textfiles/{fileName}.txt'):
        print("No text file found")
        return
    with open(f'textfiles/{fileName}.txt', 'r') as file:
        global links
        links = file.read().splitlines()
        return links
    

def downloadImagesFromLink(link, fileName):
    res = requests.get(link, stream=True)
    res.raw.decode_content = True
        
    if not os.path.exists(fileName):

        with open(fileName, 'wb') as file:
            shutil.copyfileobj(res.raw, file)

    else:
        print("File already exists")


def imagesFolder(fileName):
    links = readLinks(fileName)
    if not os.path.exists(f'images/{fileName}/'):
        os.makedirs(f'images/{fileName}/')
    for i in range(len(links)):
        downloadImagesFromLink(links[i], f'images/{fileName}/{i+1}.jpg')
    print(f"Log: Images successfully downloaded to images/{fileName}/")
# imagesFolder(fileName='jenna_ortega')
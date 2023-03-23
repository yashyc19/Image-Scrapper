def generateLink():
    search = input("Enter search: ").lower().replace(" ", "+")
    imageSize = input("Enter image size (none|Small|Medium|Large|Wallpaper): ").capitalize()
    imageColor = input("Enter image color (none|color|Monochrome): ")
    imageType = input("Enter image type (none|photo|gif): ")
    imageLayout = input("Enter image layout (none|Square|Tall|Wide): ").capitalize()

    link = f"https://duckduckgo.com/?q={search}&t=h_&iar=images&iax=images&ia=images&iaf="
    if imageSize != "None":
        link += f"%2Csize%3A{imageSize}"
    if imageColor != "none":
        link += f"%2Ccolor%3A{imageColor}"
    if imageType != "none":
        link += f"%2CimgType%3A{imageType}"
    if imageLayout != "None":
        link += f"%2Clayout%3A{imageLayout}"

    return link

def main():
    searchLink = generateLink()
    print(searchLink)

if __name__ == "__main__":
    main()


''' 
https://duckduckgo.com/?q={firstName+secondName}&t=h_&iar=images&iax=images&ia=images
https://duckduckgo.com/?q=gigi+hadid&t=h_&iar=images&iax=images&ia=images

size: &iaf=size%3A{size} Small|Medium|Large|Wallpaper
color: &iaf=color%3A{color} color|Monochrome
imgType: &iaf=imgType%3A{imgType} photo|gif
layout: &iaf=layout%3A{layout} Square|Tall|Wide

%2C_%3A_
'''
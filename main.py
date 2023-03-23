import userInput as ip
import scrape as sc
import imageDownload as id

def main():
    print("Scrapinator - An image scraping tool")
    searchLink, limit, outputFileName = ip.getUserInput()
    sc.scrapeImages(searchLink=searchLink, limit=limit, outputFileName=outputFileName)
    id.imagesFolder(fileName=outputFileName)

if __name__ == "__main__":
    main()
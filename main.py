import userInput as ip
import scrape as sc

def main():
    print("Scrapinator - An image scraping tool")
    searchLink, limit, outputFileName = ip.getUserInput()
    sc.scrapeImages(searchLink=searchLink, limit=limit, outputFileName=outputFileName)

if __name__ == "__main__":
    main()

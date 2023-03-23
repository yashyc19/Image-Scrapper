# Image Scrapper

This is a python based image scraping bot that will extract and download images as per users' input.

## Installation

You might also need some modules (if not installed, such as selenium, urllib3, etc)
```
py -m pip install -r requirements.txt
```

You also might need to download your own [ChromeDriver](https://chromedriver.chromium.org/downloads)
(for better experience and less bugs) 

## Usage

After downloading the [ChromeDriver](https://chromedriver.chromium.org/downloads), move the .exe file in the webdriver folder.
Do download proper supported version of driver according to your device

After that go to your browser and search "My user agent" and copy/paste your user agent in "sel.py >> user_agent"

And VOILA !!  Run main.py on your terminal
```
python main.py
```

## Remember
1. Your images will be saved in the folder called "data / <your_search>" eg. data / jamie_clayton
2. This program was developed on win10/64bits. For other platforms all you need to do is:
    - change the driver
    - update your user_agent
    - necessary changes in path syntax
 
## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

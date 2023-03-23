# Image Scrapper

This is a python based image scraping bot that will extract and download images as per users' request.

## Working

In order to run the tool there are few main components required
- a webdriver (here i have used chromedriver) based on your system and available browser
- necessary libraries to implement the code
- the code itself

## Installation

You will need to download your own [Selemium Webdriver](https://www.selenium.dev/documentation/webdriver/)
(for better experience and less bugs)

In order to have all the modules (if not installed, such as selenium, requests, shutil, etc), run the following command
```
pip install -r requirements.txt
``` 

## Usage

After downloading the [Selemium Webdriver](https://www.selenium.dev/documentation/webdriver/), move the .exe file in the webdriver folder.
Do download proper supported version of driver according to your device.

It is also necessary to update the locations so just make sure all the paths for files and folders are set right.

Then finally to run, enter
```
python main.py
```
The script will display the update log in the terminal itself.

All the data will be stored in the `textfiles/<filename>` and `images/<filename>`

Some glimpses:


## Remember
1. Your images will be saved in the folder called "data / <your_search>" eg. data / jamie_clayton
2. This program was developed on win11/64bits. For other platforms all you need to do is:
    - change the driver
    - update your user_agent
    - necessary changes in path syntax
 
## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

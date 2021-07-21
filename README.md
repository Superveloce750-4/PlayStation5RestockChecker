# PlayStation5RestockChecker
Checks to see if PlayStation 5 is in stock using Python and Selenium

In order to use this script, you must have Google Chrome and Selenium installed
It is possible to use other browsers as well, but modifications must be made to the code.

If you are using chrome make sure the exe file is at path: "C:\Users\YOURUSERNAME\AppData\Local\Google\Chrome\Application\chrome.exe"

To install selenium, use pip install selenium

(If you don't have pip, install that first -  There are tonnes of tutorials online)

Next you will need chromedriver.exe (or other browser's selenium driver file) - https://chromedriver.chromium.org/

Once you have done this, point the code to your chromedriver installation (Line18) 

Ex: driver = webdriver.Chrome(r'C:\Drivers\chromedriver.exe')

Next, change the URL for Amazon to a different product or leave it as ks, if you are trying to use it for PS5 (Line21)

Finally, you may want to change the value that the variable x is equal to
X represents the time taken that Selenium will pause before starting a new action
This is done to simulate a real human's interaction with the website, so that you do not get banned from using Amazon (or any other website you use bots on)
You can make it faster or slower.

This code can work on other browser; you would have to download the new selenium browser drivers and point them to the code. You would also have to make sure you save the 
browser's executable file to the default location that Selenium will look for it at.

This code can also work on different websites. You would have to input the new URL in line 18 and you would have to find the xpath for the buy now and purchase now links 
on that website. Different websites might also have different procedures to buy a product, so keep that in mind. Ex: Sign in, Add to Cart, Buy Now

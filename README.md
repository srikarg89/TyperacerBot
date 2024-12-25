# TyperacerBot

A bot that plays typeracer for you.
Written in **Python** version **3.6**

## Setup

First, make sure you install the required libraries.
```
pip install -r requirements.txt
```

Then install [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract/wiki) and confirm that pytesseract is working.

## Run

In order to run the code, first go to [typeracer](https://play.typeracer.com/). Then, hit "Enter a typing race" and wait for the game to start.

Make sure that you have a command prompt open and are ready to run the code. The words "change display format," "main menu (leave race)," and "wpm" should be visible on your screen.

Once the game starts, quickly switch to command prompt, run 
```
python bot.py
```
and switch back to the typeracer screen within two seconds of running the code. You can change this delay by changing the DELAY variable in [bot.py](bot.py).

For the CAPTCHA, perform the same procedure, but use [captcha.py](captcha.py) instead of bot.py.

### High score
My high score so far is 437 WPM, let me know if you do better!

![](CAPTCHA%20420.png)
![](First%20Place%20437.png)

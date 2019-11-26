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

### High score
My high score so far is 267, let me know if you do better! Shoot me an email at srikarg89@gmail.com.
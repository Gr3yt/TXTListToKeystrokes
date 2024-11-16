import pyautogui
import time
import os
import platform
import sys
from tqdm import tqdm 

countdown = 5

def cls():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

if len(sys.argv) > 1:
    Path = sys.argv[1]
else:
    Path = input("Please input the text file's file path: ")

try:
    with open(Path, "r") as file:
        words = file.read().splitlines()
except FileNotFoundError:
    print("Error: File not found. Please check the path and try again.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()


for i in range(countdown):
    x = countdown - i
    cls()
    print("Typing in", x)
    time.sleep(1)

print("\nTyping")
time.sleep(1)

cls()

for word in tqdm(words, desc="Typing words", unit="word"):
    pyautogui.write(word)
    pyautogui.press("enter")

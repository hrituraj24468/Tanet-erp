import webbrowser
import keyboard
import time


webbrowser.open("https://web.whatsapp.com/send?phone=+919630276554")

time.sleep(10)

for i in range(0,50):
    keyboard.write("hey ")
    keyboard.press_and_release('Return')
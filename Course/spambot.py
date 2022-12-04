# SPAM BOT

import time
import pyautogui

msg = input('Type your message: ')
# n = input("How many times do you want to send this message? ")

print ('Sending message...')

count = 5
while (count != 0 ):
    print(count)
    time.sleep(1)
    count -= 1

print('Starting spam...')

n = 0
while (n != 100):
    pyautogui.typewrite(msg + '\n')
    time.sleep(10)
    n += 1


# for i in range (0, int(n)):
#     pyautogui.typewrite(msg + '\n')
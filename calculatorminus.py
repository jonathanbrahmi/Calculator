# This code as write by Jonathan brahmi

import os
import time
import platform
from tqdm import tqdm


logo = '''
   8888 8888 8888         88888888       888           8888 8888 8888   8888       88888  888                 88888888     888 8888 888    8888888888    888   888888
  8888                  888      888     888          8888              8888       88888  888                888     888       8888       888      888   888 888
  8888                 888        888    888          8888              8888       88888  888               888       888      8888      88          88  888 88
  8888                888  888888  888   888          8888              8888       88888  888              888 888888  888     8888       888      888   888
   8888 8888 8888    8888          8888  888888888888  8888 8888 8888   8888 88888 88888  888888888888    8888         8888    8888        8888888888    888

'''

for i in tqdm(range(10)):
    time.sleep(0.3)

print("[*]developer on python 3.9")
print("[*]Runing on processor",platform.processor())
print("[*]Runing on machine",platform.machine())

print("\n")
print("Welcome to")
print(logo)
print("By Jonathan brahmi \n")

for i in tqdm(range(10)):
    time.sleep(0.3)

print("\n")
x = int(input("[x]  Enter a number with 1 digit:"))
y = int(input("[y]  Enter a number with 1 digit:"))

sum = x - y
print("Result = " + str(sum))

for i in tqdm(range(10)):
    time.sleep(0.3)

os.system("pause")
exit()
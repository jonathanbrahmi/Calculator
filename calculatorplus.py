# This code as write by Jonathan brahmi

from tqdm import tqdm
import time
import os

logo = '''
   8888 8888 8888         88888888       888           8888 8888 8888   8888       88888  888                 88888888     888 8888 888    8888888888    888   888888
  8888                  888      888     888          8888              8888       88888  888                888     888       8888       888      888   888 888
  8888                 888        888    888          8888              8888       88888  888               888       888      8888      88          88  888 88
  8888                888  888888  888   888          8888              8888       88888  888              888 888888  888     8888       888      888   888
   8888 8888 8888    8888          8888  888888888888  8888 8888 8888   8888 88888 88888  888888888888    8888         8888    8888        8888888888    888

'''
print("Welcome to")
print(logo)
print("By Jonathan brahmi \n")
print("\n")
for i in tqdm(range(10)):
    time.sleep(0.3)

x = int(input("[*][x][1]Enter a number with 1 digit:"))
y = int(input("[*][y][2]Enter a number with 1 digit:"))
sum = x + y
print("Result = " + str(sum) + "\n")

for i in tqdm(range(10)):
    time.sleep(0.3)

os.system("pause")

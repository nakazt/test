#! /usr/bin/env python3

import sys
import random

def main():
  if len(sys.argv) != 3:
    print('１〜 <max> までの重複しないランダム値を <cnt> 個出力します')
    print(f'Usage: {sys.argv[0]} <max> <cnt>\n')
    exit()

  try:
    max = int(sys.argv[1])
    cnt = int(sys.argv[2])
  except:
    print('整数値を指定してください\n')
    exit()

  # cnt = max if max < cnt else cnt
  if max < cnt:
    cnt = max
   
  lst = [i for i in range(1, max + 1)]
  num = []
  for i in range(cnt):
    n = random.randint(0, len(lst) - 1)
    num.append(lst.pop(n))

  num.sort()
  print(num)

if __name__ == '__main__':
  main()

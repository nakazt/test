#! /usr/bin/env python3

import sys
import datetime

def main():
  opt = sys.argv[1] if len(sys.argv) != 1 else ""
  print(opt)

  dt = datetime.date.today()
  tm = datetime.datetime.now()
  print(f'{dt} {type(dt)}')
  print(f'{tm} {type(tm)}')

if __name__ == '__main__':
  main()

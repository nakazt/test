#! /usr/bin/env python3

import sys
import re

def main():
  opt = sys.argv[1] if len(sys.argv) != 1 else ""

  # m = re.match(r'[0-9]{3}', opt)
  m = re.search(r'[0-9]{3}', opt)
  print(m)
  if m:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())

if __name__ == '__main__':
  main()

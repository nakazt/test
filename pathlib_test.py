#! /usr/bin/env python3

# カレントのファイル、ディレクトリを再帰的に表示する
# オプション
# 　dn　ディレクトリ名のみ
# 　fn　ファイル名のみ
# 　d　ディレクトリ一覧
# 　f　ファイル一覧
# 　n　ディレクトリ名・ファイル名

import sys
from pathlib import Path

def main():
  option = []
  if len(sys.argv) == 2:
    option = sys.argv[1]

  option = sys.argv[1] if len(sys.argv) == 2 else []

  dir = Path.cwd()
  # dir = Path('dir1')
  for d in dir.glob('**/*'):
    if not ('.git' in str(d)):
      if 'dn' in option:
        if d.is_dir():
          print(d.name)
      elif 'fn' in option:
        if d.is_file():
          print(d.name)
      elif 'd' in option:
        if d.is_dir():
          print(d)
      elif 'f' in option:
        if d.is_file():
          print(d)
      elif 'n' in option:
        print(d.name)
      else:
        print(d)

if __name__ == '__main__':
  main()
 
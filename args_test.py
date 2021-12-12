#! /usr/bin/env python3

# 可変長引数 *args / **kwargs

# 可変長引数 *args タプルとして受け取る
def sample1(x, y, *args):
  print(x)
  print(y)
  print(args)
  print(type(args))

# 位置引数
def sample2(*args, x, y):
  print(args)
  print(x)
  print(y)

# キーワード引数 **kwargs 辞書として受け取る
def sample3(**kwargs):
  print(kwargs)

# キーワード引数
def sample4(w, x, **kwargs):
  print(w)
  print(x)
  print(kwargs)

def main():
  sample1(1, 2, 3, 4)
  sample2(1, 2, x = 3, y = 4)
  sample3(x = 3, y = 4)
  sample4(1, 2, y = 3, z = 4)

if __name__ == '__main__':
  main()

#! /usr/bin/env python3

def main():
  x = { 'apple': 120, 'banana': 300, 'orange': 80 }
  print(x['apple'])

  x['berry'] = 150
  print(x)
  
  x['banana'] = 280
  print(x)

  y = { 'abcd': 500, 'efgh': 600 }
  # x.update(y)
  print(x)

  z = x | y
  print(z)
  print(len(z))

  for _ in z:
    print(_, z[_])

  print(z.get('undefined_key'))  # get でも取得できる(get は key が存在しないと None(デフォルト)を返す)
  print(z.get('undefined_key', 'oops!'))  # 存在しなかったときの値を第2引数で指定できる

if __name__ == '__main__':
  main()

#! /usr/bin/env python3

import sys
import re
import requests

def main():
  opt = sys.argv[1] if len(sys.argv) != 1 else ""

  if re.match('^[0-9]{7}$', opt):
    params = { 'zipcode': {int(opt)} }
  else:
    print(f'Usage: {sys.argv[0]} <zip code>\n')
    sys.exit()

  url = 'https://zipcloud.ibsnet.co.jp/api/search'
  res = requests.get(url, params)

  print(res.status_code)
  # print(res.text)
  res_json = res.json()

  if res_json['results'] is not None:
    results = res_json['results'][0]
    address = results['address1'] + results['address2'] + results['address3']
    print(address)
  else:
    print(f'zip code error({opt}: {res_json["results"]})')

if __name__ == '__main__':
  main()

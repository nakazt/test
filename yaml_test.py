#! /usr/bin/env python3

import sys
import yaml
import traceback

from yaml.error import YAMLError

def main():
  yaml_file = sys.argv[1] if len(sys.argv) != 1 else ""

  try:
    with open(yaml_file) as f:
      yml = yaml.safe_load(f)
  except FileNotFoundError as e:
    print(e)
    sys.exit()
  except YAMLError as e:
    print(e)
    sys.exit()
  except:
    t = traceback.format_exc()
    print(t)
    sys.exit()
  
  for key in yml:
    print(f'{key}: {yml[key]}')

if __name__ == '__main__':
  main()

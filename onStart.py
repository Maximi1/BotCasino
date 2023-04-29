from time import sleep
from os.path import isfile, exists

if not isfile('config.txt'):
    with open('config.txt', 'w') as f:
        f.write('token = Token here')
        print('\n[BOT] Config file created.\n[BOT] Program will stop in 5 seconds...')
        sleep(5)
        exit()
else:
    with open('config.txt', 'r') as f:
        token = f.readlines()[0].split(' = ')[1].strip()
        if token.startswith('Token'):
            print('\n[BOT] Please fill config file.\n[BOT] Program will stop in 5 seconds...')
            sleep(5)
            exit()

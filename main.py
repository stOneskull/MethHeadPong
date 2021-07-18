from pong import Pong
from time import sleep


def go(players):
    game = Pong()
    game.go(players)
    while True:
        game.window.update()
        if players != '2':
            game.ghosts(players)
        game.balling()


if __name__ == '__main__':
    while True:
        players = input('number of players [0-2]? ')
        if not players:
            players = '0'
        if players in ['0', '1', '2']:
            break

    waitsecs = 7

    print()
    if players == '2': 
        print('-- "W" for up and "S" for down')
    if players != '0':
        print('-- "I" for up and "K" for down')
    print()

    for wait in range(waitsecs, 1, -1):
        print(f'starting game in {wait} seconds')
        sleep(1)

else:
    players = '1'

try:
    go(players)
except:
    quit()

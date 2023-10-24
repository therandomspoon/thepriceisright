import time
import random
import threading
from playsound import playsound

round = 1
user1guess = 0
user2guess = 0
user3guess = 0
user4guess = 0
user1dif = 0
user2dif = 0
user3dif = 0
user4dif = 0
user1 = ''
user2 = ''
user3 = ''
user4 = ''
item_list =  [
    {"item": "TV", "price": 500},
    {"item": "Gaming Console", "price": 300},
    {"item": "Washing Machine", "price": 700},
    {"item": "Vacation Package", "price": 2000},
    {"item": "Smartphone", "price": 800},
    {"item": "Laptop", "price": 1000},
    {"item": "Bicycle", "price": 200},
    {"item": "Kitchen Appliances", "price": 400},
    {"item": "Fitness Equipment", "price": 600},
    {"item": "Coffee Maker", "price": 50},
    {"item": "Diamond Ring", "price": 1500},
    {"item": "Car", "price": 25000},
    {"item": "Designer Handbag", "price": 300},
    {"item": "Home Theater System", "price": 1500},
    {"item": "Luxury Watch", "price": 10000},
    {"item": "Grill", "price": 300},
    {"item": "Sofa", "price": 700},
    {"item": "Guitar", "price": 400},
    {"item": "Cruise Vacation", "price": 5000},
    {"item": "Jet Ski", "price": 8000},
    {"item": "Dining Table", "price": 600},
]

def play_background_music():
    while True:
        playsound('tpis.mp3')

def collectguess():
    global user1guess, user2guess, user3guess, user4guess
    print('The item is', item_name, 'Enter your guesses!')
    user1guess = int(input('Contestant 1 enter your guess: '))
    user2guess = int(input('Contestant 2 enter your guess: '))
    user3guess = int(input('Contestant 3 enter your guess: '))
    user4guess = int(input('Contestant 4 enter your guess: '))

def mathtime():
    global user1dif, user2dif, user3dif, user4dif
    user1dif = abs(user1guess - item_price)
    user2dif = abs(user2guess - item_price)
    user3dif = abs(user3guess - item_price)
    user4dif = abs(user4guess - item_price)

def verify():
    if user1dif < user2dif and user1dif < user3dif and user1dif < user4dif:
        return "Contestant 1 wins!"
    elif user2dif < user1dif and user2dif < user3dif and user2dif < user4dif:
        return "Contestant 2 wins!"
    elif user3dif < user1dif and user3dif < user2dif and user3dif < user4dif:
        return "Contestant 3 wins!"
    elif user4dif < user1dif and user4dif < user2dif and user4dif < user3dif:
        return "Contestant 4 wins!"
    else:
        return "It's a tie!"


music_thread = threading.Thread(target=play_background_music)
music_thread.daemon = True
music_thread.start()

while round <= 5:
    selected_item = random.choice(item_list)
    item_name = selected_item['item']
    item_price = selected_item['price']

    print(f'\nRound {round}:')
    collectguess()
    mathtime()

    print("Results:")
    print(f"{user1}'s guess: {user1guess} (Difference: {user1dif})")
    print(f"{user2}'s guess: {user2guess} (Difference: {user2dif})")
    print(f"{user3}'s guess: {user3guess} (Difference: {user3dif})")
    print(f"{user4}'s guess: {user4guess} (Difference: {user4dif})")

    winner = verify()
    print(winner)
    print("It's price is", item_price)

    round += 1

print("Game Over")

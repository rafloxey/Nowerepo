from math import sqrt
from random import randint

game_width = 10
game_height = 10

steps = 0
player_x = 0
player_y = 0

key_x = randint(0, game_width)
key_y = randint(0, game_height)

distance_before_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)


print(key_x, key_y)


player_found_key = False

while not player_found_key:
    steps += 1
    print()
    print("Możesz udać się w kierunkach określonych jako [W,A,S,D]")
    
    move = input("Dokąd idziesz? ")
    match move:
        case "w":
            player_y += 1
            if player_y > game_height:
                print("Auć! uderzasz w ścianę! ")
        case "s":
            player_y -= 1
            if player_y < 0:
                print("Auć! uderzasz w ścianę! ")
        case "a":
            player_x -= 1
            if player_x < 0:
                print("Auć! uderzasz w ścianę! ")
        case "d":
            player_x += 1
            if player_x > game_width:
                print("Auć! uderzasz w ścianę! ")
        case "q":
            quit()
        case _:
            print("Podano błędne dane. Wybierz 'W', 'A', 'S' lub 'D'.")
            continue
    
    if player_x == key_x and player_y == key_y:
            
        print("Gratulacje! Odnalazłeś klucz!")
        print(f"Wykonałeś {steps} kroków.")
        exit()
        
    distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)
    
    if distance_before_move > distance_after_move:
        print("Jesteś bliżej do klucza!")
    else:
        print("Oddalasz się od klucza! ")
        
    distance_before_move = distance_after_move
    
    print(player_x, player_y)
        
        
        
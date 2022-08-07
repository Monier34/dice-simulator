import random

dice_random = random.randint(1, 6)
dice_random1 = random.randint(1, 6)
dice_sum = dice_random + dice_random1

player_choice = 1

while player_choice != dice_sum:
    player_choice = int(input("Введите число от 1 до 12: "))
    if player_choice < dice_sum:
        print("Компьютер выйграл! ")
    elif player_choice > dice_sum:
        print("Вы выйграли! ")
    else:
        print("Сумма одиноковая. Ничья! ")

    play_again = input("Сыграем еще? (д/н): ")
    if play_again.lower() != "д":
        break

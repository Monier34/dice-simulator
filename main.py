# Импорт библиотек
import matplotlib.pyplot as plt
import random


# Функция броска кубика
def roll_dice():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)

    # Определяет является ли значение на костях одинаковым
    if dice_1 == dice_2:
        same_num = True
    else:
        same_num = False
    return same_num


# Входные данные
num_silumations = 10000
max_num_rolls = 1000
bet = 1

# Отслеживаемые переменные
win_probability = []
end_balance = []

# Фигура, для симуляции баланса
fig = plt.figure()
plt.title("Monte Carlo Dice Game [" + str(num_silumations) + "simulation]")
plt.xlabel("Roll Number")
plt.ylabel("Balance [$]")
plt.xlim([0, max_num_rolls])

# Цикл for запускает желаемое количество симуляций
for i in range(num_silumations):
    balance = [1000]
    num_rolls = [0]
    num_wins = 0
    # Выполняется до тех пор пока игрок не выкинет 1000 раз
    while num_rolls[-1] < max_num_rolls:
        same = roll_dice()
        # Результат если кости одинаковые
        if same:
            balance.append(balance[-1] + 4 * bet)
            num_wins += 1
        # Результат если кости разные
        else:
            balance.append(balance[-1] - bet)

        num_rolls.append(num_rolls[-1] + 1)

    # Сохраняем отслеживаемую переменную и добавляем строку к рисунку
    win_probability.append(num_wins/num_rolls[-1])
    end_balance.append(balance[-1])
    plt.plot(num_rolls, balance)

plt.show()

overall_win_probability = sum(win_probability)/len(win_probability)
overall_end_balance = sum(end_balance)/len(end_balance)

print("Average win propability after " +str(num_silumations) + "runs: " +str(overall_win_probability))
print("Average ending balance after " +str(num_silumations) + "runs: $" +str(overall_end_balance))

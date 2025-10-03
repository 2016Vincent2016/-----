import random

options = ['камень', 'ножницы', 'бумага', 'колодец']
user_score = 0
computer_score = 0
number_of_winnings = 0
number_of_losts = 0
number_of_ties = 0
number_of_failures = 0

while user_score < 10 and computer_score < 10:
    user_choice = input("Выберите: камень, ножницы, колодец или бумага (или 'выход' для завершения): ")

    if user_choice == 'выход':
        print("Спасибо за игру!")
        print(f"Вы выиграли {number_of_winnings} раз, проиграли {number_of_losts} раз, сыиграли {number_of_ties} раз в ничью и сделали {number_of_failures} ощибок в правописание!")
        print(f"Конечный счёт: {user_score}:{computer_score}")
        break

    if user_choice not in options:
        print("Неверный выбор. Попробуйте снова.")
        print(f"Cчёт: {user_score}:{computer_score}")
        number_of_failures = number_of_failures + 1
        continue


    computer_choice = random.choice(options)
    print(f"Компьютер выбрал: {computer_choice}")

    if user_choice == computer_choice:
        number_of_ties = number_of_ties + 1
        print(f"Ничья! Счёт: {user_score}:{computer_score}")


    elif(user_choice == 'камень' and computer_choice == 'ножницы'):
        number_of_winnings = number_of_winnings + 1
        user_score = user_score + 1
        print(f"Вы победили! Cчёт: {user_score}:{computer_score}")


    elif(user_choice == 'ножницы' and computer_choice == 'бумага'):
        number_of_winnings = number_of_winnings + 1
        user_score = user_score + 1
        print(f"Вы победили! Cчёт: {user_score}:{computer_score}")


    elif(user_choice == 'бумага' and computer_choice == 'камень'):
        number_of_winnings = number_of_winnings + 1
        user_score = user_score + 1
        print(f"Вы победили! Cчёт: {user_score}:{computer_score}")


    elif(user_choice == 'бумага' and computer_choice == 'колодец'):
        number_of_winnings = number_of_winnings + 1
        user_score = user_score + 1
        print(f"Вы победили! Cчёт: {user_score}:{computer_score}")


    elif(user_choice == 'колодец' and computer_choice == 'ножницы'):
        number_of_winnings = number_of_winnings + 1
        user_score = user_score + 1
        print(f"Вы победили! Cчёт: {user_score}:{computer_score}")

    elif(user_choice == 'колодец' and computer_choice == 'камень'):
        number_of_winnings = number_of_winnings + 1
        user_score = user_score + 1
        print(f"Вы победили! Cчёт: {user_score}:{computer_score}")

    else:
        number_of_losts = number_of_losts + 1
        computer_score = computer_score + 1
        print(f"Вы проиграли! Счёт: {user_score}:{computer_score}")

if user_score == 10:
    print(f"🎉 Вы победили со счётом 10:{computer_score}!")
    print(f"Вы выиграли {number_of_winnings} раз, проиграли {number_of_losts} раз, сыиграли {number_of_ties} раз в ничью и сделали {number_of_failures} ощибок в правописание!")
elif computer_score == 10:
    print(f"🎮 Компьютер победил со счётом 10:{user_score}!")
    print(f"Вы выиграли {number_of_winnings} раз, проиграли {number_of_losts} раз, сыиграли {number_of_ties} раз в ничью и сделали {number_of_failures} ощибок в правописание!")
print("Игра окончена!")
import random

def get_user_choice():
    user_choice = input("Выберите: камень, ножницы, бумага, ящерицу или Спока? ").lower()
    while user_choice not in ['камень', 'ножницы', 'бумага', 'ящерица', 'спок']:
        print("Неверный ввод. Пожалуйста, выберите камень, ножницы, бумагу, ящерицу или Спока.")
        user_choice = input("Выберите: камень, ножницы, бумага, ящерицу или Спока? ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага', 'ящерица', 'спок'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (
            (user_choice == 'камень' and (computer_choice == 'ножницы' or computer_choice == 'ящерица')) or
            (user_choice == 'ножницы' and (computer_choice == 'бумага' or computer_choice == 'ящерица')) or
            (user_choice == 'бумага' and (computer_choice == 'камень' or computer_choice == 'спок')) or
            (user_choice == 'ящерица' and (computer_choice == 'спок' or computer_choice == 'бумага')) or
            (user_choice == 'спок' and (computer_choice == 'ножницы' or computer_choice == 'камень'))
    ):
        return f"Вы выиграли!"
    else:
        return f"Вы проиграли."

def game():
    print("Добро пожаловать в игру 'Камень, ножницы, бумага, ящерица, Спок'!")
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Вы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "Вы выиграли!":
            user_score += 1
        elif result == "Вы проиграли.":
            computer_score += 1
        print(f"Счет: Вы {user_score} : {computer_score} Компьютер")
        if user_score == 3 or computer_score == 3:
            if user_score > computer_score:
                print("Вы победили в серии игр!")
            else:
                print("Компьютер победил в серии игр.")
            play_again = input("Хотите сыграть еще раз? (да/нет) ").lower()
            if play_again != 'да':
                print("Спасибо за игру! До свидания.")
                break
            else:
                user_score = 0
                computer_score = 0

game()

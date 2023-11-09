import random

def get_user_choice():
    user_choice = input("Выберите: камень, ножницы или бумага? ").lower()
    while user_choice not in ['камень', 'ножницы', 'бумага']:
        print("Неверный ввод. Пожалуйста, выберите камень, ножницы или бумагу.")
        user_choice = input("Выберите: камень, ножницы или бумага? ").lower()
    return user_choice


def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (
            (user_choice == 'камень' and computer_choice == 'ножницы') or
            (user_choice == 'ножницы' and computer_choice == 'бумага') or
            (user_choice == 'бумага' and computer_choice == 'камень')
    ):
        return f"Вы выиграли!"
    else:
        return f"Вы проиграли."


def game():
    print("Добро пожаловать в игру 'камень, ножницы, бумага'!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Вы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Хотите сыграть еще раз? (да/нет) ").lower()
        if play_again != 'да':
            print("Спасибо за игру! До свидания.")
            break

game()

from art import logo, vs
from game_data import data
from random import sample


def number_select():
    num_data = []
    random_select = sample(data, 2)
    num1 = random_select[0]
    num2 = random_select[1]
    num_data.append(num1)
    num_data.append(num2)
    return num_data


def game_data(compare_a, compare_b):
    print(logo)
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
    print(vs)
    print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")


def game():
    num_data = number_select()
    compare_a = num_data[0]
    compare_b = num_data[1]

    score = 0

    game_over = False
    while not game_over:
        game_data(compare_a, compare_b)

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        if compare_a['follower_count'] > compare_b['follower_count'] and answer == 'a':
            compare_b = number_select()[1]
            while compare_a == compare_b:
                compare_b = number_select()[1]
            score += 1
            print(f"You're right! Current score: {score}.")
            print("\n")

            
        elif compare_a['follower_count'] < compare_b['follower_count'] and answer == 'b':
            compare_a = compare_b
            compare_b = number_select()[1]
            while compare_a == compare_b:
                compare_b = number_select()[1]
            score += 1
            print(f"You're right! Current score: {score}.")
            print("\n")

            
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True


game()









from prompt import string


def run_game(main_question, get_question_answer):
    name = string('''Welcome to the Brain Games!
May I have your name? ''')
    print(f'Hello, {name}!')
    print(main_question)
    ROUNDS = 3
    for _ in range(ROUNDS):
        (question, correct) = get_question_answer()
        print(f'Question: {question}')
        ans = string('Your answer: ')
        if ans == correct:
            print('Correct!')
        else:
            print(
                f"""'{ans}' is wrong answer ;(. Correct answer was '{correct}'.
Let's try again, {name}!
"""
            )
            quit()
    print(f'Congratulations, {name}!')

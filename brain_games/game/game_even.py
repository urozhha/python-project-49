def get_even_data(num1, num2):
    problem_even = num1 * num2
    correct_even = 'yes' if problem_even % 2 == 0 else 'no'
    even_out = (problem_even, correct_even)
    return even_out

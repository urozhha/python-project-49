def get_is_prime(num1, num2):
    correct_prime = ''
    problem_prime = abs(num1 - num2)
    for i in range(2, problem_prime):
        if problem_prime % i == 0:
            correct_prime = 'no'
            break
        else:
            correct_prime = 'yes'
    prime_out = (problem_prime, correct_prime)
    return prime_out

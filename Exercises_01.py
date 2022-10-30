import random
import math


# Question 1
def sum_four():

    counter = 0
    n = 100000

    for i in range(n):
        if random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) == 4:
            counter += 1

    print(counter / n)


sum_four()


# Question 2
def independent():

    counter_a = counter_b = counter_a_b = 0
    n = 100000

    for i in range(n):

        roll = random.randint(1, 6)

        if roll % 2 == 1:
            counter_a += 1
        if roll >= 3:
            counter_b += 1
        if (roll % 2 == 1) and (roll >= 3):
            counter_a_b += 1

    p_a = round(counter_a / n, 2)
    p_b = round(counter_b / n, 2)
    p_a_b = round(counter_a_b / n, 2)

    print(f"Probability odd: {p_a}")
    print(f"Probability ge 3: {p_b}")
    print(f"Probability odd and ge 3: {p_a_b}")

    print(f"Verifying A and B are independent: {math.isclose(p_a * p_b, p_a_b, abs_tol=0.01)}")


independent()


# Question 3
def conditional():

    primes = [2, 3, 5]
    counter_a = counter_b = counter_a_b = 0
    n = 100000

    for i in range(n):

        roll = random.randint(1, 6)

        if roll % 2 == 1:
            counter_a += 1
        if roll in primes:
            counter_b += 1
        if (roll % 2 == 1) and (roll in primes):
            counter_a_b += 1

    p_a = round(counter_a / n, 2)
    p_b = round(counter_b / n, 2)
    p_a_b = round(counter_a_b / n, 2)

    print(f"Probability odd: {p_a}")
    print(f"Probability prime: {p_b}")
    print(f"Probability odd and prime: {p_a_b}\n")

    print(f"Verifying P(A | B): {math.isclose(p_a_b / p_b, 0.67, abs_tol=0.02)}")
    print(f"Verifying P(B | A): {math.isclose(p_a_b / p_a, 0.67, abs_tol=0.02)}")


conditional()

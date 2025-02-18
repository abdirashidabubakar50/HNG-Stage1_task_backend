""" Utils functions for mathematical and funfacts about numbers """
import math
import requests

def is_prime(n):
    """ check if a number is prime """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """ Returns True if a number is perfect otherwise False"""
    if n < 2: 
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_even_or_odd(n):
    """ Returns even if a number is even and odd if a number is odd """
    if n %  2 == 0:
        return "even"
    else:
        return "odd"

def is_armstrong(n):
    """ returns True if a number is armstrong else false """
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def sum_digits(n):
    total = 0
    for d in str(n):
        total += int(d)
    return total

def get_number_fact(n):
    """ fetch a fun fact about the number from NumbersApi"""
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            data = response.json()
            return data.get("text", "This number does not have a fun fact.")
        else:
            return "This number does not have a fun fact."
    except Exception as e:
        print(f"Error fetching number fact: {e}")
        return "This number does not have a fun fact."
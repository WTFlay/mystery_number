#!/usr/bin/env python3

import random

print("Try to guess the mystery number !")

rand_num = random.randint(1,100)
user_num = 0

while rand_num != user_num:
    user_num = int(input("Enter a number: "))
    if user_num < rand_num:
        print("It's more!")
    elif user_num > rand_num:
        print("It's less...")
    else:
        print("GG ! You find the number", rand_num, "! :)")

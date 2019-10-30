"""Restaurant rating lister."""

import random

file = open("scores.txt")

dictionary = {}

for line in file:
    line = line.rstrip()
    line_list = line.split(':')
    
    dictionary[line_list[0]] = line_list[1]

restaurant_list = dictionary.items()
key_list = [key for key in dictionary.keys()]

while True:
    user_action = input("[S]ee, [A]dd, [U]pdate, [Q]uit > ").upper()

    if user_action == "Q":
        break

    if user_action == "U":
        rand_res = random.choice(key_list)
        print(f'{rand_res} is rated at {dictionary[rand_res]}.')
        new_rating = input("What's the new rating? > ")
        dictionary[rand_res] = new_rating

    if user_action == "S":
        sorted_restaurant_list = sorted(restaurant_list)

        for item in sorted_restaurant_list:
            print(f'{item[0]} is rated at {item[1]}.')
        # print("{} is rated at {}".format(item[0], item[1]))

    if user_action == "A":
        res_name = input("What's the restaurant name? > ").title()
            
        while True:
            res_score = int(input("Whats the restaurant score? > "))
            if res_score not in range(1, 6):
                print("Invalid, try again")
            else:
                break

        dictionary[res_name] = res_score






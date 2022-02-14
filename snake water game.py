print('\t\t\t\t"Welcome To Snake Water Gun Game:" ')
import random
user_points = 0
pc_points = 0
i = 0
list = ["s", "w", "g"]
while i < 10:
# for i in range(10):
    user_choice = input("'s' for snake 'w' for water 'g' for gun: ")
    pc_choice = random.choice(list)
    user_choice.lower()
    if user_choice == pc_choice:
        print("Both are equal")
        # i -= 1
        continue
    elif user_choice not in list:
        print("Wrong Input: ")
        continue
    elif user_choice == "s" and pc_choice == "w":
        print("Snake Drinks Water ")
        user_points += 1
    elif user_choice == "w" and pc_choice == "s":
        pc_points += 1
        print("Snake Drinks Water ")
    elif user_choice == "w" and pc_choice == "g":
        print("Gun is drown in water")
        user_points += 1
    elif user_choice == "g" and pc_choice == "w":
        pc_points += 1
        print("Gun is drown in water")
    elif user_choice == "s" and pc_choice == "g":
        print("Gun Shoots Snake ")
        pc_points += 1
    elif user_choice == "g" and pc_choice == "s":
        print("Gun Shoots Snake ")
        user_points += 1
    i += 1
if pc_points > user_points:
    print(f"Your points {user_points} and PC points {pc_points}")
    print("You Lose! Better Luck will next time insha'Allah: ")
elif user_points < pc_points:
    print(f"Your points {user_points} and PC points {pc_points}")
    print("Congratulations! You Won: ")
elif user_points == pc_points:
    print(f"Your points {user_points} and PC points {pc_points}")
    print("Great Competition! Both of equal Scores")
import random

def user_bat(target=None):
    user_score = 0
    balls = 0
    for i in range(30):  # 30 balls
        balls += 1
        while True:
            try:
                user = int(input('Enter your choice between 0 to 6: '))
                if user not in range(0, 7):
                    print("Invalid input. Please choose a number between 0 and 6.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
                continue
            break

        computer = random.randint(0, 6)
        print(f"Computer's choice: {computer}")
        print(f"Your choice: {user}")

        if user == computer:
            if user_score == 0:
                print("You're DUCK out... HAHA")
            else:
                print("\nYou're out!!")
            break
        else:
            user_score += user
            print(f"Your score is: {user_score}\n")
            if target and user_score > target:
                break
        
        if balls >= 30 :
            print("Innings completed")
            break

    return user_score

def com_bat(target=None):
    com_score = 0
    balls = 0
    for i in range(30):  # 30 balls
        balls += 1
        while True:
            try:
                user = int(input('Enter your choice between 0 to 6: '))
                if user not in range(0, 7):
                    print("Invalid input. Please choose a number between 0 and 6.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
                continue
            break

        computer = random.randint(0, 6)
        print(f"Computer's choice: {computer}")
        print(f"Your choice is: {user}")

        if user == computer:
            if com_score == 0:
                print("Computer's DUCK out... HAHA")
            else:
                print("\nComputer's out!!")
            break
        else:
            com_score += computer
            print(f"Computer's score is: {com_score}\n")
            if target and com_score > target:
                break
        
        if balls >= 30 :
            print("Innings completed")
            break

    return com_score


def winner(user_score,com_score):
    if user_score < com_score:
            print("Computer wins! Better luck next time.\n")            
    elif user_score > com_score:
        print("You won the match!!...YAYY!!\n")
    else:
        print("It's a tie!!\n")
    print("---------------------------------------------------")


def hand_cricket():
    print('''Game rules:
      1. There will be a toss between you and the computer. You have to choose either odd or even. Then, choose a number between 0 to 6.
      2. If the sum of your and the computer's number is odd or even, according to what you chose, you will either win or lose the toss.
      3. If you win the toss, you can choose to bat or bowl.
      4. If you are batting, choose a number between 0 to 6 to score runs. If your number matches the computer's, you're out and vice versa.
      5. The game consists of 5 overs, with each over having 6 balls.
      6. Have fun and play fair!''')

    choice = ['odd', 'even']
    you = input("Odd or Even: ").lower()
    
    if you not in choice:
        print("Invalid input...Enter from the given choices\n")
        return
        
    com = random.randint(0, 6)
    try:
        user_oe = int(input('Enter your choice between 0 to 6: '))
        if user_oe not in range(0, 7):
            print("Invalid input. Please choose a number between 0 and 6.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
        return
    

    print(f"Computer's choice is: {com}")
    print(f"Your choice is: {user_oe}\n")

    choose = ['bat', 'bowl']
    Bat_Bowl_1 = None
    Bat_Bowl_2 = None

    if (you == 'even' and (com + user_oe) % 2 == 0) or (you == 'odd' and (com + user_oe) % 2 == 1):
        print("You win the toss, choose to bat or bowl\n")
        Bat_Bowl_1 = input("Bat or Bowl? - ").lower()
    else:
        Bat_Bowl_2 = random.choice(choose)
        print(f"Computer wins the toss and chooses to {Bat_Bowl_2}\n")

    if Bat_Bowl_1 == 'bat':
        print("\nYou are batting... Let the match begin\n")
        user_score = user_bat()
        print(f"Your final score is: {user_score}\n")

        print("Computer is batting now...\n")
        com_score = com_bat(target=user_score)
        print(f"Computer's final score is: {com_score}\n")

        winner(user_score,com_score)


    elif Bat_Bowl_2 == 'bat':
        print("Computer is batting now...Let the match begin\n")
        com_score = com_bat()
        print(f"Computer's final score is: {com_score}\n")

        print("You are batting now...\n")
        user_score = user_bat(target=com_score)
        print(f"Your final score is: {user_score}\n")
        
        winner(user_score,com_score)

            
    elif Bat_Bowl_1 =='bowl':
        print("\nComputer is batting... Let the match begin\n")
        com_score = com_bat()
        print(f"Computer's final score is: {com_score}\n")

        print("You are batting now...\n")
        user_score = user_bat(target=com_score)
        print(f"Your final score is: {user_score}\n")

        winner(user_score,com_score)


    elif Bat_Bowl_2 =='bowl':
        
        print("You are batting...Let the match begin\n")
        user_score = user_bat()
        print(f"Your final score is: {user_score}\n")

        print("Computer is batting now...\n")
        com_score = com_bat(target=user_score)
        print(f"Computer's final score is: {com_score}\n")

        winner(user_score,com_score)

hand_cricket()

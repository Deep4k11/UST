
p1_name = input("Player 1 enter your name:")
p2_name = input("Player 2 enter your name:")
p1_action = input(p1_name + " Enter a choice (rock, paper, scissors): ")
p2_action = input(p2_name + " Enter a choice (rock, paper, scissors): ")

if p1_action == p2_action:
   print("Both players selected " + p1_action + " It's a tie!")
elif p1_action == "rock":
        if p2_action == "scissors":
            print("Rock smashes scissors! " + p1_name+" wins!")
        else:
            print("Paper covers rock! " + p2_name+" wins!")
elif p1_action == "paper":
        if p2_action == "rock":
            print("Paper covers rock! " + p1_name + " wins!")
        else:
            print("Scissors cuts paper! " + p2_name + " wins" )
elif p1_action == "scissors":
        if p2_action == "paper":
            print("Scissors cuts paper! " + p1_name + " wins!")
        else:
            print("Rock smashes scissors! " + p2_name + " wins")

else:
    print('Enter a valid choice')
# LAB 2 - HOCKEY TEAM
#Write a program that will ask the user to enter the name of a hockey team, how many wins the team has and 
# how many losses #the team has.

#The program should calculate and display a single string output containing the team name, it's win-loss 
# ratio and the win #percentage formatted to 4 decimal places.

#Ex: The Calgary Flames have 10 wins and 5 losses, with a win percentage of 0.6667.

#Purpose/Concepts: Input and output to screen, string concatentation, string formatting, datatype casting, 
# simple math operations

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Gets user inputs for teamName, teamWins, and teamLosses. Takes the wins/loses vals as integers.
    teamName = input("What is the name of the team you would like to look at today?: ")
    winsNum = int(input(f"\nHow many games have the {teamName}'s won so far this season?: "))
    lossesNum = int(input(f"\nHow many games have the {teamName}'s lost so far this season?: "))

    # Does the caclc for the win % of the team. 
    totalGamesPlayed = winsNum + lossesNum
    winPerercentage = winsNum / totalGamesPlayed

    # Prints out the team name, wins, losses, and the win percentage. formats the win percentage to 4 decimal places.
    print(f"The {teamName}"+"'s"+f" have {winsNum} wins and {lossesNum} losses, with a win percentage of "f"{winPerercentage:.4f}.") 
    # YOUR CODE ENDS HERE
main()
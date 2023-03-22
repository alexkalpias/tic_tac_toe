print("TIC TAC TOE GAME\n----------------")
option = 0
while exit != 4:
    print("Choose one of the following games:\n")
    print("1: 2 Players\n")
    print("2: Against the computer - You play first\n")
    print("3: Against the computer - You play second\n")
    print("4: Exit\n")
    option = int(input())
    if option == 1:
        import tic_tac_toe_2_Players
    elif option == 2:
        import tic_tac_toe_AI_Second_Turn
    elif option == 3:
        import tic_tac_toe_AI_First_Turn
    elif option == 4:
        print("Bye!")
        break
    else:
        print("Wrong option")


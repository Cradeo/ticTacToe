import ticTacToe
import ticTacComp


def start_up():
    print(""""
  ::::::::::: ::::::::::: :::::::: ::::::::::: :::      :::::::: ::::::::::: ::::::::  :::::::::: 
     :+:         :+:    :+:    :+:    :+:   :+: :+:   :+:    :+:    :+:    :+:    :+: :+:         
    +:+         +:+    +:+           +:+  +:+   +:+  +:+           +:+    +:+    +:+ +:+          
   +#+         +#+    +#+           +#+ +#++:++#++: +#+           +#+    +#+    +:+ +#++:++#      
  +#+         +#+    +#+           +#+ +#+     +#+ +#+           +#+    +#+    +#+ +#+            
 #+#         #+#    #+#    #+#    #+# #+#     #+# #+#    #+#    #+#    #+#    #+# #+#             
###     ########### ########     ### ###     ###  ########     ###     ########  ##########       
Coded by Cradeo
    """)

    menu()


def menu():
    print("""
Please pick a program you wish to run
1: TicTacToe - player vs player
2: TicTacToe - player vs computer
3: Exit
          """)
    while True:
        user_input = input("> ")
        try:
            val = int(user_input)
            if val in range(1, 4):
                run(val)
                break
            else:
                print("Not a valid number")
        except ValueError:
            print("Not a valid number")


# Condense this code
def run(selection):
    if selection == 1:
        ticTacToe.board = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9"
        ]
        ticTacToe.play_game()
        while True:
            if selection == 1:
                print("Would you like to play again?(Y/N)")
                user_input = input("> ")
                if user_input.upper() == 'N':
                    menu()
                    break
                elif user_input.upper() == 'Y':
                    ticTacToe.board = [
                        "1", "2", "3",
                        "4", "5", "6",
                        "7", "8", "9"
                    ]
                    ticTacToe.play_game()
                else:
                    print("That's not a valid input")
    elif selection == 2:
        ticTacComp.board = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9"
        ]
        ticTacComp.play_game()
        while True:
            if selection == 2:
                print("Would you like to play again?(Y/N)")
                user_input = input("> ")
                if user_input.upper() == 'N':
                    menu()
                    break
                elif user_input.upper() == 'Y':
                    ticTacComp.board = [
                        "1", "2", "3",
                        "4", "5", "6",
                        "7", "8", "9"
                    ]
                    ticTacComp.play_game()
                else:
                    print("That's not a valid input")
    else:
        quit()


start_up()

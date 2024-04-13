class TicTacToe:

    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.Player = 1
        self.Win = 1
        self.Draw = -11
        self.Running = 0
        self.Stop = 1
        self.Game = self.Running
        self.Mark = 'X'

    def DrawBoard(self):
        print(" %c | %c | %c " %(self.board[1], self.board[2], self.board[3]))
        print("___|___|___")
        print(" %c | %c | %c " %(self.board[4], self.board[5], self.board[6]))
        print("___|___|___")
        print(" %c | %c | %c " %(self.board[7], self.board[8], self.board[9]))
        print("   |   | ")

    def CheckPosition(self, x):
        if self.board[x] == ' ':
            return True
        else:
            return False
    
    def CheckWin(self):
        global Game

        if self.board[1] == self.board[2] and self.board[2] == self.board[3] and self.board[1] != ' ':
            self.Game = self.Win

        elif self.board[4] == self.board[5] and self.board[5] == self.board[6] and self.board[4] != ' ':
            self.Game = self.Win

        elif self.board[7] == self.board[8] and self.board[8] == self.board[9] and self.board[7] != ' ':
            self.Game = self.Win

        elif self.board[1] == self.board[4] and self.board[4] == self.board[7] and self.board[1] != ' ':
            self.Game = self.Win

        elif self.board[2] == self.board[5] and self.board[5] == self.board[8] and self.board[2] != ' ':
            self.Game = self.Win

        elif self.board[3] == self.board[6] and self.board[6] == self.board[9] and self.board[3] != ' ':
            self.Game = self.Win

        elif self.board[1] == self.board[5] and self.board[5] == self.board[9] and self.board[5] != ' ':
            self.Game = self.Win

        elif self.board[3] == self.board[5] and self.board[5] == self.board[7] and self.board[5] != ' ':
            self.Game = self.Win

        elif self.board[1] != ' ' and self.board[2] != ' ' and self.board[3] != ' ' and \
                self.board[4] != ' ' and self.board[5] != ' ' and self.board[6] != ' ' and \
                self.board[7] != ' ' and self.board[8] != ' ' and self.board[9] != ' ':
            self.Game = self.Draw
            
        else:
            self.Game = self.Running

    def main(self):
        import os
        import time
        print("Tic-Tac-Toe")
        print("Player 1 [X] --- Player 2 [O]\n")
        print()
        print()
        print("Please Wait...")
        print()
        print()
        time.sleep(2)
        while self.Game == self.Running:
            os.system('cls')
            self.DrawBoard()

            if self.Player % 2 != 0:
                print("Player 1's chance")
                print()
                self.Mark = 'X'
            else:
                print("Player 2's chance")
                print()
                self.Mark = 'O'

            try:
                self.position = int(input("Enter the position between [1-9] where you want to mark: "))
                if self.position < 1 or self.position > 9:
                    raise ValueError("Position must be between 1 and 9")
            except ValueError as e:
                print("Invalid input:", e)
                continue
                
            if self.CheckPosition(self.position):
                self.board[self.position] = self.Mark
                self.Player += 1
                self.CheckWin()

            if self.Game == self.Draw:
                print("Game Draw")
                print()
                print("Tap To Play Again")
            elif self.Game == self.Win:
                self.Player -= 1
                os.system('cls')
                self.DrawBoard()
                if self.Player % 2 != 0:
                    print("Player 1 Won")
                    print()
                    print("Tap To Play Again")
                else:
                    print("Player 2 Won")
                    print()
                    print("Tap To Play Again")

TTT = TicTacToe()
TTT.main()

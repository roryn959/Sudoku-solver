#Rory Nicholas
#19/10/2018

instructor = input("Please input the sudoku task into a file called 'sudokutask', and save it in the same folder as you have saved the program in. If you experience a delay of longer than 5 seconds, the program is unable to complete the sudoku. Press enter when done ")
f = open("sudokutask.txt", "r")
fileContent = f.readlines()
solved = False

class Sudoku:

    def __init__(self):
        global tempCell
        f = open("sudokutask.txt", "r")
        fileContent = f.readlines()
        self.__board = []
        for y in range(0,9):    # 9 rows
            tempList = []                 #A temporary list which will become each individual row to be added to the board
            for x in range(0,9): # 9 columns
                tempCell = cell(int(fileContent[y][x]), x, y)
                tempCell.SetBox()
                tempList.append(tempCell) # Creates the temporary list to be added to the sudoku board as a row
            self.__board.append(tempList) # self.__board, after these loops, will be a big list which is just the value of each cell concatenated, with each row containing in its own sub-list

    def Solver1(self):
        global solved
        solved = True
        for y in range(0, 9):
            for x in range(0,9):
                cellToCheck = self.__board[y][x] #Cell currently being checked
                if cellToCheck.GetNumber() == 0:
                    solved = False
                    for j in range(0, 9):
                        for t in range(0, 9):
                            cellAgainst = self.__board[j][t] #The cell to check the cellToCheck against
                            relevant = False
                            if cellAgainst == cellToCheck:
                                relevant = False
                            elif y == j or x == t or cellToCheck.GetBox() == cellAgainst.GetBox() and cellAgainst.GetNumber() != 0:                  
                                relevant = True

                            if relevant == True:
                                if cellAgainst.GetNumber() in cellToCheck.possibilities:
                                    cellToCheck.possibilities.remove(cellAgainst.GetNumber())
                if len(cellToCheck.possibilities) == 1:
                    cellToCheck.SetNumber(cellToCheck.possibilities[0])
                    self.__board[y][x].SetNumber(cellToCheck.GetNumber())
                    #self.__board[y][x].SetNumber(cellToCheck.possibilities[0])

        if solved == True:
            r = open("solved sudoku.txt", "w+")
            for p in range(0, 9):
                for e in range(0, 9):
                    r.write(str(self.__board[p][e].GetNumber()))
                r.write("\n")
            print("\nDone. You should now find a file called 'solved sudoku' in the same folder as the original task.")

    def Solver2(self):
        for g in range(1, 10):
            #rows
            for k in range(0, 9):
                counter = 0
                rowList = []
                for f in range(0, 9):
                    checkingCell = self.__board[k][f]
                    if g in checkingCell.possibilities:
                        counter = counter+1
                        rowList.append(0)
                    else:
                        rowList.append(1)
                if counter == 1 and g in self.__board[k][rowList.index(1)].possibilities:
                    self.__board[k][rowList.index(1)].SetNumber(g)

            #columns
            for a in range(0, 9):
                counterc = 0
                colList = []
                for s in range(0, 9):
                    checkingCell = self.__board[s][a]
                    if g in checkingCell.possibilities:
                        counterc = counterc+1
                        colList.append(1)
                    else:
                        colList.append(0)
                if counterc == 1 and g in self.__board[s][colList.index(1)].possibilities:
                    self.__board[s][colList.index(1)].SetNumber(g)


class cell:

    def __init__(self, newNumber, newColumn, newRow):
        self.possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.__number = newNumber
        self.__column = newColumn
        self.__box = 0
        self.__row = newRow

    def GetNumber(self):
        return self.__number

    def SetNumber(self, changedNumber):
        self.__number = changedNumber
        return self.__number

    def GetColumn(self):
        return self.__column

    def GetRow(self):
        return self.__row

    def SetBox(self):
        if tempCell.GetRow()<3 and tempCell.GetColumn()<3:
            self.__box = 1            
        elif tempCell.GetRow()<3 and 6>tempCell.GetColumn()>2:
            self.__box = 2
        elif tempCell.GetRow()<3 and tempCell.GetColumn()>5:
            self.__box = 3
        elif 6>tempCell.GetRow()>2 and tempCell.GetColumn()<3:
            self.__box = 4
        elif 6>tempCell.GetRow()>2 and 6>tempCell.GetColumn()>2:
            self.__box = 5
        elif 6>tempCell.GetRow()>2 and tempCell.GetColumn()>5:
            self.__box = 6
        elif tempCell.GetRow()>5 and tempCell.GetColumn()<3:
            self.__box = 7
        elif tempCell.GetRow()>5 and 6>tempCell.GetColumn()>2:
            self.__box = 8
        elif tempCell.GetRow()>5 and tempCell.GetColumn()>5:
            self.__box = 9
        return self.__box

    def GetBox(self):
        return self.__box

theSolver = Sudoku()
while solved == False:
    theSolver.Solver2()
    theSolver.Solver1()

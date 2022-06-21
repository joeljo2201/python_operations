##class QueenChessBoard:
##     def __init__(self, size):
##         self.size = size
##         self.columns = []
##     def place_in_next_row(self, column):
##         self.columns.append(column)
##     def remove_in_current_row(self):
##         return self.columns.pop()
##     def is_this_column_safe_in_next_row(self, column):
##         row = len(self.columns)
##         for queen_column in self.columns:
##             if queen_column == column  :
##                 return False
##         for queen_row, queen_column in enumerate(self.columns):
##             if queen_column - queen_row == column - row:
##                return False
##         for queen_row, queen_column in enumerate(self.columns):
##             if ((self.size - queen_column) - queen_row == (self.size - column) - row):
##                return False
##         return True
##     def display(self):
##        for row in range(self.size):
##            for column in range(self.size):
##                if column == self.columns[row]:
##                    print('Q', end=' ')
##                else:
##                    print('.', end=' ')
##            print()
##def solve_queen(size):
##    board = QueenChessBoard(size)
##    number_of_solutions = 0
##    row = 0
##    column = 0
##    while True:
##         while column < size:
##             if board.is_this_column_safe_in_next_row(column):
##                 board.place_in_next_row(column)
##                 row += 1
##                 column = 0
##                 break
##             else:
##                 column += 1
##         if (column == size or row == size):
##             if row == size:
##                 board.display()
##                 print()
##                 number_of_solutions += 1
##                 board.remove_in_current_row()
##                 row -= 1
##             try:
##                 prev_column = board.remove_in_current_row()
##             except IndexError:
##                 break
##             row -= 1
##             column = 1 + prev_column
##    print('Number of solutions:', number_of_solutions)
##n = int(input('Enter n: '))
##solve_queen(n)
class queen:
  def __init__(self,size):
    self.size=size
    self.columns=[]
  def add(self,column):
    self.columns.append(column)
  def remove(self):
    return self.columns.pop()
  def check(self,column):
    row=len(self.columns)
    for qcol in self.columns:
      if qcol==column:
        return False
    for qrow,qcol in enumerate(self.columns):
      if qcol-qrow==column-row:
        return False
    for qrow,qcol in enumerate(self.columns):
      if ((self.size-qcol)-qrow==((self.size-column)-row)):
        return False
    return True
  def display(self):
    for row in range(self.size):
      for column in range(self.size):
        if column==self.columns[row]:
          print('Q',end=' ')
        else:
          print('.',end=' ')
      print()
def solveq(size):
  board=queen(size)
  rows=0
  column=0
  nos=0
  while True:
    while column<size:
      if board.check(column):
        board.add(column)
        rows+=1
        column=0
      else:
        column+=1
        break
    if(column==size or rows==size):
      if rows==size:
        board.display()
        print()
        nos+=1
        board.remove()
        rows-=1
      try:
        prev_col=board.remove()
      except IndexError:
        break
      rows-=1
      column=1+prev_col
  print("nos: ",nos)
n=int(input("enter n: "))
solveq(n)









































        
         













































































              
           
                

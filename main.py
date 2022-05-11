import tkinter as tk
import puzzles as pz
from warnings import warn
class Card:
  def __init__(self,root):
    self.var = tk.StringVar()
    self.lbl = tk.Label(root, textvariable = self.var, bg = "light grey", bd = 1, justify = "right", padx = 7, pady = 7)
  def color(self,colour):
    self.lbl.config(bg = colour)

class Grid:
  def __init__(self,root):
    self.cards = []
    for row in range(0,5):
      col_list = []
      for column in range(0,15):
        col_list.append(Card(root))
      self.cards.append(col_list)
  def get(self,index):
    return self.cards[index[0]][index[1]]
  
  def blank(self,index):
    self.get(index).color('gray')
    self.change_val(index, ' ')

  def empty(self,index):
    self.change_val(index,'_')
    self.get(index).color('light gray')

  
  def change_val(self,index,val):
    self.get(index).var.set(val)

  def load(self,puzzle):
    for row in range(0,len(puzzle)):
      for letter in range(0,len(puzzle[row])):
        if puzzle[row][letter] == ' ':
          self.blank((row,letter))
        else:
          self.empty((row,letter))
  def pzadd(self,puzzle):
    self.currentpuzzle = puzzle
    self.currentpuz_row_gen = range(0,len(puzzle))
    self.currentpuz_cols_gen = range(0,len(puzzle[0]))
    self.load(puzzle)

  def pzget(self,index):
    return self.currentpuzzle[index[0]][index[1]]
  
  def reveal(self, index):
    self.change_val(index,self.pzget(index))

  def reveal_ltr(self, letter):
    revealn = 0
    for rown in self.currentpuz_row_gen:
      for coln in self.currentpuz_cols_gen:
        if self.pzget((rown,coln)) == letter:
          self.reveal((rown,coln))
          revealn += 1
    print(revealn)

a = tk.Tk()  
a.geometry("400x400")  
a.title("Wheel of Fortune")  


num = 0
rown = 0
grid = Grid(a)
for row in grid.cards:
  coln = 0
  for card in row:
    card.var.set(num)
    card.lbl.grid(row = rown, column = coln, padx = 0, pady= 0, sticky= 'nsew')
    coln += 1
    num += 1
  rown += 1

bottom_text = tk.StringVar()

bottom = tk.Label(a, textvar = bottom_text, bg = "cyan", bd = 5, justify = "center", padx = 225, pady = 6)

bottom.grid(row = 6, columnspan = 15)

puzzles = pz.puzzles().puzs
clues = pz.puzzles().clues


bottom_text_num = 0
for puzzle in puzzles:
  grid.pzadd(puzzle)
  bottom_text.set(clues[bottom_text_num])
  while True:
    answer = input("command?")
    if answer.isalpha() and len(answer) == 1:
      grid.reveal_ltr(answer)
    elif answer == 'solved':
      break
    else:
      warn("invalid answer")
  bottom_text_num += 1


a.mainloop()
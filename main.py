import tkinter as tk
import puzzles as pz
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
    self.get(index).var.set(" ")

  def change_val(self,index,val):
    self.get(index).var.set(val)

  def load(self,puzzle):
    for row in range(0,len(puzzle)):
      for letter in range(0,len(puzzle[row])):
        if puzzle[row][letter] == '':
          self.blank((row,letter))
        else:
          self.change_val((row,letter),'_')
  def pzadd(self,puzzle):
    self.currentpuzzle = puzzle
    self.load(puzzle)

a = tk.Tk()  
a.geometry("400x400")  
a.title("test")  


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

bottom = tk.Label(a, text = 'placeholder', bg = "cyan", bd = 5, justify = "center", padx = 225, pady = 6)

bottom.grid(row = 6, columnspan = 15)

puzzles = pz.puzzles().puzs


grid.pzadd(puzzles[0])

a.mainloop()
import tkinter as tk
from warnings import warn
from textwrap import fill
from time import sleep

class Card:
  def __init__(self,root):
    self.var = tk.StringVar()
    self.lbl = tk.Label(root, textvariable = self.var, bg = "light grey", bd = 1, justify = "right", padx = 7, pady = 7, font = font)
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

  def color(self,index,color):
    self.get(index).color(color)
  def blank(self,index):
    self.color(index,'grey')
    self.change_val(index, ' ')

  def empty(self,index):
    self.change_val(index,'_')
    self.color(index,'light grey')
  
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

  def pzfyadd(self,puzzle_str):
    self.pzadd(puzzlify(puzzle_str))
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
    return revealn

  def reveal_board(self):
    for letter in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
      self.reveal_ltr(letter)

def puzzlify(puzzlestr):
  quote = puzzlestr
  WIDTH = 15
  HEIGHT = 5
  
  import textwrap  # It has a cool `fill` function, see below
  
  # break it up using max WIDTH, then split the lines
  broken_quote = textwrap.fill(quote, width=WIDTH).split('\n')
  print(broken_quote)
  
  extra_lines = HEIGHT - len(broken_quote)  # how many extra lines do you need?
  extra_at_top = int(extra_lines/2)  # half at top
  extra_at_bottom = extra_lines - extra_at_top  # the rest at bottom
  
  blank_line = [' '] * WIDTH  # define a blank line
  blank_line
  
  final = []
  # First add the blank lines at top
  for idx in range(extra_at_top):
    final.append(blank_line.copy())
  
  # Then the main text lines, center aligned
  for row in broken_quote:
    final.append(list((row.center(WIDTH))))  # list() converts the string into list of chars
  
  # Lastly the blank lines at bottom
  for idx in range(extra_at_bottom):
    final.append(blank_line.copy())
  
  return final

def value_change(scorel, str_index, str_val):
  scorel[int(str_index)].set(scorel[int(str_index)].get() + int(str_val))
  

a = tk.Tk()  
a.geometry("500x500")  
a.title("Wheel of Fortune")
font = ('Helvetica', 32)
font1 = ('Helvetica', 20)
font2 = ('Helvetica', 20)
num = 0
# rown = 0
grid = Grid(a)
for row_idx, row in enumerate(grid.cards):
  # coln = 0
  for col_idx, card in enumerate(row):
    card.var.set(num)
    card.lbl.grid(row = row_idx, column = col_idx, padx = 0, pady= 0, sticky= 'nsew')
    # coln += 1
    num += 1
  # rown += 1

bottom_text = tk.StringVar()

bottom = tk.Label(a, textvar = bottom_text, bg = "cyan", bd = 5, justify = "center", padx = 225, pady = 6,font = font2)

guessed_letters = tk.StringVar()

guessed = tk.Label(a, textvar = guessed_letters, bg = "cyan", bd = 5, justify = "center", padx = 100, pady = 6,font = font2)

bottom.grid(row = 5, columnspan = 15, sticky= 'nsew')
guessed.grid(row = 6, columnspan = 15,  sticky= 'nsew',)

score_head_1 = tk.Label(a, text = 'Team 1:', bg = "light grey", bd = 5, justify = "center", padx = 6, pady = 6,font = font1)

score_head_2 = tk.Label(a, text = 'Team 2:', bg = "light grey", bd = 5, justify = "center", padx = 6, pady = 6,font = font1)

score_head_3 = tk.Label(a, text = 'Team 3:', bg = "light grey", bd = 5, justify = "center", padx = 6, pady = 6,font = font1)

score_top = tk.Label(a, text = "Scores", bg = "light grey", bd = 5, justify = "center", padx = 10, pady = 6,font = font1)

score_top.grid(row = 0, column = 16, sticky= 'nsew')
score_head_1.grid(row = 1, column = 16,  sticky= 'nsew')
score_head_2.grid(row = 3, column = 16,  sticky= 'nsew')
score_head_3.grid(row = 5, column = 16,  sticky= 'nsew')

score = [0,tk.IntVar(),tk.IntVar(),tk.IntVar()]

for val in score[1:]:
  val.set(0)

score_1 = tk.Label(a, textvar = score[1], bg = "light grey", bd = 5, justify = "center", padx = 6, pady = 6,font = font1)
score_2 = tk.Label(a, textvar = score[2], bg = "light grey", bd = 5, justify = "center", padx = 6, pady = 6,font = font1)
score_3 = tk.Label(a, textvar = score[3], bg = "light grey", bd = 5, justify = "center", padx = 6, pady = 6,font = font1)

score_1.grid(row = 2, column = 16,  sticky= 'nsew')
score_2.grid(row = 4, column = 16,  sticky= 'nsew')
score_3.grid(row = 6, column = 16,  sticky= 'nsew')


puzzles = []
clues = []

initial_puzzle = 'a feather in your cap'
initial_clue = 'phrase'

grid.pzfyadd(initial_puzzle)
bottom_text.set(initial_clue)


guessed_letters.set('Guessed Letters:')

bottom_text_num = 0


while True:
  answer = input("command?")
  if answer.isalpha() and len(answer) == 1:
    print(grid.reveal_ltr(answer))
    guessed_letters.set(guessed_letters.get() + ' ' + answer)
  elif answer == 'next':
    grid.pzfyadd(puzzles.pop(0))
    bottom_text.set(clues.pop(0))
    guessed_letters.set('Guessed Letters: ')
  elif answer == 'reveal':
    grid.reveal_board()
  elif answer.startswith("pzuse "):
    grid.pzfyadd(answer[6:])
  elif answer.startswith("cluse "):
    bottom_text.set(answer[6:])
  elif answer.startswith("pzadd "):
    puzzles.append(answer[6:])
    print(puzzles)
  elif answer.startswith("cladd "):
    clues.append(answer[6:])
    print(clues)
  elif answer.startswith('score '):
    value_change(score,answer[6],answer[7:])
  else:
    warn("invalid answer")
bottom_text_num += 1


a.mainloop()
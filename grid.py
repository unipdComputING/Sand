import pygame
import random
import copy
import math

class Grid:

  def __init__(self, cols, rows):
    self.cols = cols
    self.rows = rows
    self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
    # self.color = [255, 190, 50]
    self.color = [0, 190, 255]
    self.background = [255, 255, 255]
    self.background_boundary = [100, 40, 10]

  def update(self):
    for irow in range(self.rows - 1, 0, -1):
      for icol in range(self.cols - 1, 0, -1):
        if self.grid[irow][icol] > 0:
          if irow + 1 < self.rows and self.grid[irow + 1][icol] == 0:
            self.grid[irow + 1][icol] = self.grid[irow][icol]
            self.grid[irow][icol] = 0
          else:
            if random.random() <= 0.5:
              if icol - 1 >= 0 and irow + 1 < self.rows and self.grid[irow + 1][icol - 1] == 0:
                self.grid[irow + 1][icol - 1] = self.grid[irow][icol]
                self.grid[irow][icol] = 0
              elif icol + 1 < self.cols and irow + 1 < self.rows and self.grid[irow + 1][icol + 1] == 0:
                self.grid[irow + 1][icol + 1] = self.grid[irow][icol]
                self.grid[irow][icol] = 0
              else: # water
                for i in range(icol, 0, -1):
                  if irow + 1 < self.rows and self.grid[irow + 1][i] < 0:
                    break
                  if irow + 1 < self.rows and self.grid[irow + 1][i] == 0:
                    self.grid[irow + 1][i] = self.grid[irow][icol]
                    self.grid[irow][icol] = 0
                    break
            else: 
              if icol + 1 < self.cols and irow + 1 < self.rows and self.grid[irow + 1][icol + 1] == 0:
                self.grid[irow + 1][icol + 1] = self.grid[irow][icol]
                self.grid[irow][icol] = 0
              elif icol - 1 >= 0 and irow + 1 < self.rows and self.grid[irow + 1][icol - 1] == 0:
                self.grid[irow + 1][icol - 1] = self.grid[irow][icol]
                self.grid[irow][icol] = 0
              else: # water
                for i in range(icol, self.cols, 1):
                  if irow + 1 < self.rows and self.grid[irow + 1][i] < 0:
                    break
                  if irow + 1 < self.rows and self.grid[irow + 1][i] == 0:
                    self.grid[irow + 1][i] = self.grid[irow][icol]
                    self.grid[irow][icol] = 0
                    break
  
  def itialize_grid(self):
    self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
  
  def draw(self, screen):
    cell_size_x = screen.get_width() // self.cols
    cell_size_y = screen.get_height() // self.rows
    # print(f"Cell size: {cell_size_x * self.cols}, {cell_size_y * self.rows}")
    for i in range(self.rows):
      for j in range(self.cols):
        rect = pygame.Rect(i * cell_size_x, j * cell_size_y, cell_size_x, cell_size_y)
        if self.grid[j][i] <= -1:
          color: list = copy.deepcopy(self.background_boundary)
          color[1] += -self.grid[j][i]
          pygame.draw.rect(screen, color, rect)
        elif self.grid[j][i] > 0:
          # print(f"Drawing at {i}, {j}"
          color: list = copy.deepcopy(self.color)
          color[1] += self.grid[j][i]
          pygame.draw.rect(screen, color, rect)
        else:
          pygame.draw.rect(screen, self.background, rect)
        # pygame.draw.rect(screen, (200, 200, 200), rect, 1)  # grid lines
  
  def plot(self):
    print()
    for i in range(self.rows):
      for j in range(self.cols):
        print(f"{self.grid[i][j]} ", end="")
      print()
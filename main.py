# sand simulator using pygame
#
#
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import time
import random
from grid import Grid

def add_boundaries(grid, pos, screen, val= -1, size = 1):
  cell_size_x = screen.get_width() // grid.cols
  cell_size_y = screen.get_height() // grid.rows
  col = pos[0] // cell_size_x
  row = pos[1] // cell_size_y
  for i in range(-size, size):
     for j in range(-size, size):
      if 0 <= row + i < grid.rows and 0 <= col + j < grid.cols:
        val = -random.randint(1, 20)
        grid.grid[row + i][col + j] = val

def clean(grid, pos, screen, size = 1):
  cell_size_x = screen.get_width() // grid.cols
  cell_size_y = screen.get_height() // grid.rows
  col = pos[0] // cell_size_x
  row = pos[1] // cell_size_y
  for i in range(-size, size):
     for j in range(-size, size):
      if 0 <= row + i < grid.rows and 0 <= col + j < grid.cols:
        grid.grid[row + i][col + j] = 0

def mouse_press(grid, pos, screen, val=1, size = 1):
  cell_size_x = screen.get_width() // grid.cols
  cell_size_y = screen.get_height() // grid.rows
  col = pos[0] // cell_size_x
  row = pos[1] // cell_size_y
  for i in range(-size, size):
     for j in range(-size, size):
      if 0 <= row + i < grid.rows and 0 <= col + j < grid.cols:
        if grid.grid[row + i][col + j] > -1:
          val = random.randint(1, 20)
          grid.grid[row + i][col + j] = val

def init():
  pygame.init()

def start():
  screen = pygame.display.set_mode((800, 800))
  clock = pygame.time.Clock()
  running = True
  grid = Grid(200, 200)
  val = 0.1
  cursor_size: int = 2
  draw_boundary = False
  clear_flag = False
  update_flag = True
  # grid.grid[1][5] = 1  # initial sand particle
  # grid.grid[5][5] = 1  # initial sand particle

  while running:
      # poll for events
      # pygame.QUIT event means the user clicked X to close your window
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
          elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b: # draw boundary conditions
              draw_boundary = not draw_boundary
              clear_flag = False
            elif event.key == pygame.K_c: # clean sand and boundary conditions
              clear_flag = not clear_flag 
              draw_boundary = False
            elif event.key == pygame.K_d: # draw sand
              draw_boundary = False 
              clear_flag = False
            elif event.key == pygame.K_i: # initialize grid
               grid.itialize_grid()
            elif event.key == pygame.K_u: # update grid
               update_flag = not update_flag
            elif event.key == pygame.K_PLUS: # increase the cursor
              cursor_size += 1
            elif event.key == pygame.K_MINUS: # decrease the cursor
               cursor_size -= 1
               cursor_size = max(1, cursor_size)
          # elif event.type == pygame.MOUSEBUTTONDOWN:
          #     mouse_press(grid, event.pos, screen, val, size=2)
      mouse_pos = pygame.mouse.get_pos()
      if pygame.mouse.get_pressed()[0] == True:
          val = random.randint(0, 20)
          if clear_flag:
             clean(grid, mouse_pos, screen, size=cursor_size)
          elif draw_boundary:
             add_boundaries(grid, mouse_pos, screen, -val, size=cursor_size)
          else:
            mouse_press(grid, mouse_pos, screen, val, size=cursor_size)

      # fill the screen with a color to wipe away anything from last frame
      screen.fill((255, 255, 255))

      # RENDER YOUR GAME HERE
      if update_flag:
        grid.update()
      grid.draw(screen)

      # flip() the display to put your work on screen
      pygame.display.flip()

      clock.tick(60)  # limits FPS to 60
      # time.sleep(1)

  pygame.quit()


if __name__ == "__main__":
    init()
    start()
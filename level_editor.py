"""
IMPORT PYGAME MODULE

COORDINATES SYSTEM IN PYGAME:
	TOP-LEFT IS (0, 0)
"""
import pygame

# IMPORT PRETTY PRINTING MODULE
import pprint

# IMPORT SYS MODULE
import sys

# IMPORT FUNCTIONS FROM THE scripts/ DIRECTORY
from scripts.utils import load_image, load_images
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap

class LevelEditor:
	def __init__(self) -> None:
		

		# NAME THE WINDOW
		pygame.display.set_caption("2D Level Editor")

		# CREATE THE WINDOW
		self.WIDTH = 640
		self.HEIGHT = 480
		self.TILE_SIZE = 16
		self.LOWER_MARGIN = 100 # LOAD & SAVE BUTTONS ARE HERE
		self.SIDE_MARGIN = 300 # TILE SETS ARE HERE
		self.screen = pygame.display.set_mode(
			(self.WIDTH + self.SIDE_MARGIN, self.HEIGHT + self.LOWER_MARGIN)
			)

		"""
		CREATE PIXEL ART EFFECT:

			1. RENDER SPRITES ONTO SMALLER DISPLAY, i.e:
				SCREEN WITH SMALLER RESOLUTION

			2. SCALE IT UP TO THE SCREEN, i.e:
				SCREEN WITH LARGER RESOLUTION
		"""
		self.PIXEL_WIDTH = 320
		self.PIXEL_HEIGHT = 240
		self.display = pygame.Surface(
			(self.PIXEL_WIDTH, self.PIXEL_HEIGHT)
			)

		# FORCE GAME TO RUN AT 60FPS
		self.clock = pygame.time.Clock()
		self.fps = 60

		# LOAD IMAGES
		self.tile_sets = {
			"background": load_image("background.png"),
			"decor": load_images("tiles/decor"),
			"grass": load_images("tiles/grass"),
			"large_decor": load_images("tiles/large_decor"),
			"stone": load_images("tiles/stone"),
			"clouds": load_images("clouds"),
			"leaf": load_images("particles/leaf"),
			"particle": load_images("particles/particle")
		}

	# DRAW THE BOARD
	def draw_board(self):
		# LOAD IMAGES
		self.key_items = []
		self.value_items = []
		for dict_key, dict_value in self.tile_sets.items():
			self.key_items.append(dict_key)
			self.value_items.append(dict_value)

		"""
		INDEX:
			0: background, 1: decor, 2: grass,
			3: large_decor, 4: stone, 5: clouds,
			6: leaf, 7: particle
			print(self.value_items[5][0])
		"""
		self.screen.blit((self.value_items[0], (0, 0)))


	# MAIN LOOP
	def run(self):
		while True:
			#COLOR OF THE SKY
			self.display.fill((14, 219, 248))

			# DRAW BOARD
			self.draw_board()

			"""
			GET INPUT
				pygame.event.get():
					GET INPUT BY INTERACTING WITH OS
			"""
			for event in pygame.event.get():
				"""
				WHEN EVENT TYPE IS pygame.quit():
					CLOSE GAME WINDOW
				"""
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()


			"""
			THE BLIT FUNCTION COPIES A SECTION OF MEMORY
			ONTO ANOTHER SURFACE

			IN PYGAME, A SURFACE IS AN IMAGE.
			THE WINDOW'S SURFACE IS THE SCREEN.
			IT IS SPECIAL TYPE OF SURFACE.

			MOST SURFACES ARE AN IMAGE LOCATED IN MEMORY.

			YOU CAN BLIT ANY SURFACE ONTO ANY SURFACE.
			IT IS LIKE MAKING A COLLAGE OF IMAGES.

			SCALE():
				SCALE DISPLAY SURFACE
				ONTO THE SIZE OF THE SCREEN SURFACE
				REGARDLESS OF SIZE
			"""
			self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))

			# UPDATE DISPLAY
			pygame.display.update()

			# FORCE MAIN LOOP TO RUN AT 60FPS
			self.clock.tick(self.fps)

# RUN LEVEL EDITOR
LevelEditor = LevelEditor().run()

LevelEditor()


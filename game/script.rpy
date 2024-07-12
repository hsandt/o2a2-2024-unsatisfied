# The script of the game goes in this file.


## Backgrounds (1080p)

image bg black = Solid("#000000")
image bg white = Solid("#ffffff")

image bg classroom = "images/bg/classroom.webp"


## Characters

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Teacher")
define b = Character("Đạt")


# The game starts here.

label start:

    jump scene1

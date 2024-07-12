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


# Story event flags

# A1S1
default talked_about_alternative_grading = False
default talked_about_private_grades = False
default talked_about_elitism = False
default talked_about_why_study = False
default talked_about_other_classmates_worse = False
default talked_about_other_classmates_better = False
default talked_about_facial_expression = False


# The game starts here.

label start:

    jump scene1

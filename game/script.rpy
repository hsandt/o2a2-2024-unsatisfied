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

default talked_about_alternative_grading = False
default talked_about_other_classmates_better = False

default unlocked_talked_about_circumstances = False
default talked_about_circumstances = False

default unlocked_private_grades = False
default talked_about_private_grades = False

default unlocked_elitism = False
default talked_about_elitism = False

default unlocked_why_study = False
default talked_about_why_study = False

default unlocked_dialogue_end = False

# unused
# default talked_about_facial_expression = False


# The game starts here.

label start:

    jump scene1

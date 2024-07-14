# The script of the game goes in this file.


## Backgrounds (1080p)

image bg black = Solid("#000000")
# image bg white = Solid("#ffffff")
# image bg white_blueish = Solid("#f4f4f8")
image bg white_yellowish = Solid("#ffffef")

image bg classroom = "images/bg/classroom.webp"


## Characters

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Teacher")
define b = Character("Đạt")

## BGM assets

# Not used, as options.rpy > config.main_menu_music must access file by path
# In this case, I precut the track to be 72.274s long so `to` is optional here
define bgm.theme = "<loop 1.365 to 72.274>audio/bgm/unsatisfied_theme_intro-loop.opus"

## SFX assets

define sfx.crumple_paper = "audio/sfx/crumple_paper.opus"
define sfx.crumple_paper_short = "<to 1.430>audio/sfx/crumple_paper.opus"


# Story event flags

default talked_about_alternative_grading = False
default talked_about_other_classmates_better = False

default unlocked_circumstances = False
default talked_about_circumstances = False

default unlocked_private_grades = False
default talked_about_private_grades = False

default unlocked_elitism = False
default talked_about_elitism = False

default unlocked_why_study = False
default talked_about_why_study = False

default unlocked_hobbies = False
default talked_about_hobbies = False

default unlocked_dialogue_end = False

# unused
# default talked_about_facial_expression = False


transform center:
    xalign 0.5
    yalign 0.5

# https://www.renpy.org/doc/html/splashscreen_presplash.html
label splashscreen:
    scene bg white_yellowish
    with Pause(1)

    show image "images/logo/O2A2 logo transparent.webp" at center
    with dissolve
    with Pause(2)

    scene bg white_yellowish
    with dissolve
    with Pause(1)

    return


# The game starts here.

label start:

    jump scene1

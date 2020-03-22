# P03-Mc Gyver Labyrinth
# project 3 of the 'python developper' learning path of OpenClassrooms

Simply graphic and text labyrinth game 

![screenshot](https://github.com/jmlm74/P3-McGyver/tree/master/ressource/screenshotg.png?raw=true "screenshot")

<br/><br />

##### Instructions
run with -t or -g parameter (text or graphic mode)<br/>
ie : python Labyrinthe.py -g  <br />
You must pick up 3 items before reaching the goal to win otherwise you loose<br />
<br/><br/>

##### Requirements 
* Python V3.6 or higher
* Pygame V1.9.6 (in requirements.txt)
<br/><br/>

##### MVC pattern
- Models : directory models 
  - hero.py --> the hero in text mode
  - herograph.py --> the hero in graphic mode (inherit hero)
  - map.py --> the map
  - position.py --> the position (tuple (x,y))
- Views : directory views
  - consolemode.py --> the display in console-text mode
  - graphicmode.py --> the display in graphic mode
- controlers : directory controllers
  - playtxt.py --> the game controls in text mode
  - playgraphic.py --> the game controls in graphic mode
- ressource directory contains images,fonts,musics and the map file
- root directory
  - Labyrinthe.py --> main
  - setup.py --> variables and constants

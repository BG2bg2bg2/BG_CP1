#BG 1st maze generator

import turtle as t


#make the boards
maze = [["______ _"],
        ["| |   |"]
        ]
    
#make the screen
def setup():
    screen = t.Screen()
    screen.setup(500,500)
    screen.title("Maze running")
    
for a in enumerate(maze, 0):
    print(maze)





#print("Save the file as maze_generator.py")

#print("Include your 1st line comment with initials, class period, and assignment name")

#print("Import the turtle library at the beginning")

#print("Set up the screen with appropriate dimensions and a background color")

#Use nested loops to iterate through a grid system for maze creation

#Implement conditionals to determine wall placement

#Ensure that the maze has at least one valid path from start to finish

#Use functions to organize code, e.g., one for setup, one for drawing walls, and one for generating the maze layout

#Make sure the maze generation logic is correctly implemented

#Test the program to ensure it consistently generates valid, solvable mazes

#Clearly mark the start and end points of the maze

#Commit and push your code to Github


#Advanced

#Add User Interaction: Allow the user to specify maze size or complexity before generation
#Implement Different Maze Generation Algorithms: Research and implement various maze generation 
# algorithms (e.g., Recursive Backtracking, Prim's Algorithm)

#Create a Solving Feature: Implement a maze-solving algorithm that visually demonstrates the 
# solution path

#Add Visual Enhancements: Use different colors for walls, paths, start, and end points. 
# Optionally, add textures or patterns

#Generate Multiple Levels: Create a system that generates progressively more complex mazes as 
# levels

#Implement a Player Character: Add a small turtle that the user can control to navigate through 
# the maze

#Add a Timer or Step Counter: Include a feature that tracks how long it takes to solve the maze 
# or how many steps are taken

#Create a Maze-Based Game: Turn the maze generator into a simple game where the user must 
# navigate through the maze while avoiding obstacles or collecting items
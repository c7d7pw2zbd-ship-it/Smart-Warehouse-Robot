Smart Warehouse Robot

Project Description

Smart Warehouse Robot is an AI-based pathfinding and obstacle avoidance system.

The project simulates a robot moving inside a warehouse. The robot uses the A* Search Algorithm to find an efficient path from a starting position to a destination while avoiding obstacles.

The system displays the warehouse grid, obstacles, the calculated path, the robot movement, the path length, and the number of explored nodes.

Problem Formulation

States

Each cell in the warehouse grid represents a possible state for the robot.

Initial State

The robot starts at position:

(1, 1)

Goal State

The destination is:

(10, 14)

Actions

The robot can move in four directions:

* Up
* Down
* Left
* Right

Cost

Each movement from one cell to another has a cost of 1.

Algorithm

The project uses the A* Search Algorithm.

A* selects the most promising node using:

f(n) = g(n) + h(n)

Where:

* g(n) = actual cost from the start node to the current node.
* h(n) = estimated cost from the current node to the goal.
* f(n) = total estimated cost.

Heuristic

The project uses Manhattan Distance as the heuristic:

h(n) = |x1 - x2| + |y1 - y2|

Manhattan Distance is suitable because the robot moves only horizontally and vertically.

Features

* Warehouse grid visualization
* Start and goal positions
* Obstacles
* A* pathfinding
* Manhattan Distance heuristic
* Automatic robot movement
* Path length calculation
* Nodes explored calculation
* Start and Reset buttons
* Visual legend

Results

The system displays:

* Algorithm used: A*
* Path Length
* Nodes Explored
* Robot status

The robot successfully finds a path to the destination while avoiding the warehouse obstacles.

Technologies Used

* Python
* Pygame
* A* Search Algorithm

How to Run

1. Install Python

Python 3.13 is recommended for this project.

2. Install Pygame

Open the terminal and run:

py -3.13 -m pip install pygame

3. Run the Project

Open the project folder in VS Code and run:

py -3.13 main.py

4. Use the Application

Press:

START ROBOT

to start the robot movement.

Press:

RESET

to return the robot to its initial position.

Project Structure

Smart-Warehouse-Robot/
│
├── main.py
└── README.md

Conclusion

The project demonstrates how the A* Search Algorithm can be used to solve a pathfinding problem in a warehouse environment.

The robot finds an efficient path from the initial state to the goal while avoiding obstacles.
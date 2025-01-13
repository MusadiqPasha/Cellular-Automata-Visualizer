# Cellular-Automata-Visualizer
It is a collection of interactive simulations for various cellular automata models, including Amoeba, Game of Life, and more. It provides real-time visualization of the grid evolution, allowing users to explore different patterns and behaviors of these automata.

# Cellular Automata Games

A collection of cellular automata simulations implemented using [Processing.org](https://processing.org/). To run the project, make sure to use Python mode in Processing for proper execution and visualization of grid evolution.

This project features four unique games: 

- **Amoeba**
- **Brian's Brain**
- **Game of Life**
- **Larger Than Life**
  
each demonstrating distinct rules and behaviors for cellular automata.

## Features
- **Interactive Visualization**: Dynamic, grid-based simulations with color-coded states for easy visualization.
- **Four Cellular Automata Games**:
  1. **Amoeba**: Simulates organic-like growth patterns with unique rules.
  2. **Brian's Brain**: A three-state cellular automaton with "on," "dying," and "off" cells.
  3. **Game of Life**: Conway's famous simulation of life and death based on simple neighbor-count rules.
  4. **Larger Than Life**: A generalized automaton with custom rules for more complex patterns.

## How It Works

- The grid is initialized with random states or a preset configuration.
- Each simulation computes the next generation based on its specific rules.
- Color-coded grids visually represent the changes in real time.

## Color Representation

### Default States:
- Blue: "Off" or inactive.
- White: Neutral or empty state.
  
### Dynamic States:
- Yellow: Cells being compared or in transition.
- Red: Cells marked for change (e.g., "Dying").
- Black: Cells in an active state (e.g., "On").
  
## Cellular Automata Rules
### 1. **Amoeba**
- Simulates dynamic and organic growth patterns.
- Rules are tailored to produce self-sustaining patterns.

### 2. **Brian's Brain**
- Each cell has three states: **On** (blue), **Dying** (red), and **Off** (white).
- Rules:
  - **Off** → **On** if exactly two neighbors are "On."
  - **On** → **Dying** in the next step.
  - **Dying** → **Off** in the subsequent step.

### 3. **Game of Life**
- A classic cellular automaton invented by John Conway.
- Each cell can be **Alive** (black) or **Dead** (white).
- Rules:
  - **Dead** → **Alive** if it has exactly three live neighbors.
  - **Alive** → **Dead** if it has fewer than two or more than three live neighbors.
  - **Alive** → **Alive** if it has two or three live neighbors.

### 4. **Larger Than Life**
- A generalized cellular automaton with custom survival and birth rules.
- Each cell can be **On** (black) or **Off** (blue).
- Rules:
  - **Off** → **On** if surrounded by 2-3 "On" neighbors.
  - **On** → **Off** if surrounded by fewer than 2 or more than 3 "On" neighbors.

## Installation
1. Download and install [Processing](https://processing.org/) [use Python Mode]
2. Clone this repository or download the ZIP file:
   ```bash
   git clone https://github.com/kmusadiqpasha/cellular-automata-visualizer

3. Open the .pde files for each simulation in Processing.
4. Run the sketches and watch the cellular automata come to life!

### License
- This project is licensed under the MIT License - see the LICENSE file for details.

##
## Just follow me and Star ⭐ my repository 
## Thank You!!

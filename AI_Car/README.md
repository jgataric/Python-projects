# AI Car Simulation with NEAT
This project simulates an autonomous car using the NeuroEvolution of Augmenting Topologies (NEAT) algorithm. The car navigates a track, making decisions based on radar inputs, and learns through evolution to avoid obstacles and maximize its performance. The simulation runs in a Pygame environment, where multiple generations of cars are trained to optimize their movement using a NEAT neural network.

## How It Works
Car Movement: Each car uses five radars to detect the distance to the track border, feeding this data into the NEAT neural network, which outputs movement decisions.
NeuroEvolution: The NEAT algorithm evolves the neural networks controlling the cars over generations, improving their ability to navigate the track.
Fitness: Each car's fitness is determined by the distance it travels before crashing, and the reward is based on the distance traveled.

## Project Structure
main.py: The core simulation script that initializes the environment, runs the NEAT algorithm, and handles car movement.
config.txt: NEAT configuration file containing parameters for evolution (e.g., population size, mutation rates).
car.png: The car sprite used in the simulation.
map.png: The track image used for the simulation.

## How to Run
### Set Up Environment:
Ensure you have the required Python packages installed. These include pygame, neat-python, os, math, and random.
### Prepare Assets:
The folder should include car.png (the car sprite) and map.png (the track).
### Run the Simulation:
From the command line, navigate to the project folder and run the script:
open terminal and type in following
python main.py
The NEAT algorithm will start evolving the cars, with the simulation running in a Pygame window.
### Controls:
Press ESC to exit the simulation.

## NEAT Configuration:
The config.txt file is used to configure NEAT’s parameters. You can modify this file to adjust aspects like population size, mutation rates, or fitness thresholds.
NEAT Configuration Overview
The key parameters defined in config.txt are:

#### Population Size:
pop_size = 30 defines that each generation will have 30 cars.
#### Fitness Criterion:
The evolution is guided by maximizing fitness (fitness_criterion = max), where fitness is based on the distance traveled.
#### Mutation Rates:
Connection and node mutation probabilities are set to:
conn_add_prob = 0.5 and node_add_prob = 0.2
conn_delete_prob = 0.5 and node_delete_prob = 0.2
Mutation rates for bias, weight, and activation functions are also defined to promote diversity in evolving neural networks.
#### Stagnation:
To avoid getting stuck in a local optimum, the algorithm resets after max_stagnation = 20 generations with no improvement.

### Simulation Overview
Generations: The NEAT algorithm trains over several generations (default set to 5000). Each generation consists of cars trying to navigate the track.
Car Behavior: The cars adjust their speed and angle based on radar inputs. If a car collides with the track's border, it is considered "dead," and its simulation ends.
Rewards and Fitness: Cars are rewarded based on the distance they travel before crashing. The best-performing cars are used to evolve future generations.
Pygame Interface
Display: The Pygame window will show the track, cars, and the current generation and number of still-alive cars.

### File Details
config.txt: NEAT configuration file containing the genetic algorithm settings.
car.png: A 60x60 pixel image used as the sprite for the car.
map.png: The background image for the track.

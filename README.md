# EVALUATION OF A NEW MULTI-AGENT APPROACH ON MAZE PROBLEMS BASED ON THE Q-LEARNING ALGORITHM

## Project Overview

This project explores a novel multi-agent reinforcement learning (MARL) approach to solving maze problems using the Q-learning algorithm. Traditionally, maze-solving relies on a single agent to find the shortest path from a start to an end point. This project investigates the potential benefits of employing two agents working together to solve the maze by meeting at a dynamic intermediate goal state.

<video controls src="assets/readme_videos/Maze 5 - Multi-agent Solution - 5000 episodes_5000 steps.mp4" title="Maze 5 - Multi-agent Solution - 5000 episodes_5000 steps"></video>

## Key Features

- **Multi-Agent System:** Two agents collaborate by starting from different ends of the maze and aiming to meet at a dynamically determined goal state.
- **Reinforcement Learning:** Based on the Q-learning algorithm to enable agents to learn the optimal paths through the maze.
- **Dynamic Goal State:** A novel concept where the goal state can change dynamically, enhancing the agents' ability to find efficient paths.

##

## Aims and Objectives

1. **Evaluate Performance:** Compare the efficiency and effectiveness of the multi-agent approach against traditional single-agent methods.
2. **Literature Integration:** Incorporate findings from existing research on maze-solving and reinforcement learning to provide a comprehensive analysis.
3. **Explore Multi-Agent Frameworks:** Provide an overview of common multi-agent approaches and their applicability to maze-solving.

## Project Deliverables

1. **Literature Review:** Comprehensive review of the Q-learning algorithm, traditional maze-solving approaches, and multi-agent systems.
2. **Evaluation System:** A developed system with a user-friendly interface for testing different models on various maze designs.
3. **Experimental Results:** Comparative analysis through experiments, resulting in data and graphs that illustrate performance differences.
4. **Comprehensive Analysis:** In-depth discussion of the results, highlighting the advantages and potential improvements for the multi-agent approach.

## Results

- **Small Mazes:** Multi-agent approach shows superior performance in solving simple mazes efficiently.
- **Medium and Large Mazes:** Demonstrates significant adaptability and improved efficiency over traditional methods.
- **Special Designs:** Highlights scenarios where the new approach provides clear benefits.

## Future work

Despite the progress made, further work is required to fully realize the potential of the suggested algorithm. Key areas for future research include:

- **Algorithm Improvement:** Investigate why the multi-agent system occasionally fails to find the shortest path and refine the algorithm to prevent this by analyzing training sessions, adjusting parameters, and testing different reward structures.
- **Resource Analysis:** Conduct a detailed analysis of memory usage and processing power for both single-agent and multi-agent systems by benchmarking and profiling resource consumption across various maze complexities.
- **Distributed Processing:** Implement the multi-agent algorithm on separate processing units, develop communication protocols, and compare performance metrics like latency and throughput.
- **Complex Environments and Real-world applications":** Test the algorithm in varied scenarios to evaluate its robustness, including environments with intermediate goal states and dynamic obstacles, and extend the approach to more complex environments and real-world applications where unexpected obstacles may appear.

## Installation

To replicate the experiments and explore the maze-solving system, clone the repository and run the provided scripts:
'''
git clone https://github.com/fzaiter/Multi-Agent_Maze-Solver.git
cd Multi-Agent_Maze-Solver
python main.py
'''

## Usage

Use the graphical user interface to select different maze designs and test the single-agent and multi-agent models. Analyze the results through the generated graphs and data.

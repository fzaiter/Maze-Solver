# Maze-Solver
Evaluation of a new multi-agent approach on maze problems based on the Q-learning algorithm

## Abstract

The maze-solving problem consists of a system of paths on which,
given one starting position and one ending position, we should find the
shortest possible path that connects these. Reinforcement Learning
techniques such as those based on the Q-learning algorithm have already
been applied to this type of problems by creating agents that are capable of
learning how to best traverse these environments. However, no technique
seems to have been researched in regards to the use of two different agents
that could find this path jointly.

The following project introduces a new multi-agent Reinforcement
Learning algorithm based on Q-learning and the concept of the dynamic
goal state. This new approach is tested against the common single agent
model and an approach consisting of a maze solver and an explorer that
helps this explore the maze. The experiments performed show the potential
of this new approach along with some future work that may be required.
Along these benefits we highlight its greater adaptability for different types
of scenarios and its better performance for most of the performed
experiments.

## Introduction

Maze-solving systems generally rely on Reinforcement Learning (RL) techniques to create
a single agent that will need to find a path through a maze from a starting to a finish state. The
following project evaluates an alternative approach based on two agents, each of which starting at
one of these key points and finding a shortest path by finding a dynamic goal state shared by both of
them. If this is achieved, it would mean that by linking both paths together from their respective
starting points to this new goal state would give us a correct path from start to end that would solve
the maze.
The question trying to be answered on the project could be informally defined as:
*Would it be better to solve a maze if we start from both ends and try to find an intermediate goal state?*

As highlighted by Shoham, Powers and Grenager (2007), “learning in MAS [Multi-agent
Systems] is conceptually, not only technically, challenging”. The formulation of the problem trying
to be solved as well as the criteria used to evaluate this needs to be as clear as possible. As a result,
the following project tries not only to review and analyse relevant literature on this field but also
creates a maze solving system and sets up some experiments that go beyond the mere technical
analysis in order to understand the implications of the suggested approach.
As a starting point, we could assume that, if two agents were to be executed in parallel, this
would increase the resources required to navigate through the maze, both in terms of computing
resources and time required to progress. However, and despite this, we could also assume that some
mazes may be easier to solve from one of its end states which could potentially compensate for the
resources required and thus, find a more efficient solution to the maze. Along this, if the approach
proves to be successful it could potentially be extended to several processing units which could in
turn boost its performance even further.
Mazes are important types of problems within the Artificial Intelligence field as they may
be considered a simplification of more complex real-world examples being quite useful for new
techniques and algorithms to be tested. Also, by testing these in a simpler simulated environment
makes it easier to understand and gain insight on the different results achieved. As mentioned by
Futschek (2006), “the maze-problem is an interesting starting point to discuss many variants of
maze algorithms and is an ideal tool to give first insight in different aspects of algorithms.”
Furthermore, as software and robotic agents become more prevalent so do multi-agent
systems and algorithms for coordinating these (Bowling and Veloso, 2002). Applications are widely
varied, including disaster mitigation and rescue, automated driving and information agents amongst
many others.
After an in-depth research and to my best knowledge, there are no academic studies that
implement a similar approach to the one being suggested here. As explained later in this report,
applications of such an algorithm could be very useful for a wide range of applications from
navigation and routing to search and planning problems. These applications could also be extended,
both in terms of range and efficiency, if an optimal multi-agent approach could be set.

The main motivation for this project relies on the great progress and potential that the RL
field has shown over the past years. Achievements in the field have accumulated over the past 3
decades, from backgammon (Tesauro, 1995) to Starcraft II (Vinyals et al., 2019) including the
well-known AlphaGo (Silver et al., 2016) which has increased the expectations on this type of
learning, not only from experts on the field but from the general public.
This project has been developed without the help of any supervisor and hasn’t been
work-related; in fact, when I first started this project I had no experience in this field apart from the
courses studied on this degree. In regards to this, the project will be primarily built upon the
concepts studied on the Artificial Intelligence and Neural Network courses, CO3310 and CO3311
respectively. The interest on this topic also relies on the fact that those courses only introduce the
topic of RL briefly and do not go into any further detail on how they work or can be implemented.

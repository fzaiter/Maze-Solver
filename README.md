# Maze-Solver
Evaluation of a new multi-agent approach on maze problems based on the Q-learning algorithm

*SUBMITTED AS PART OF THE REQUIREMENTS FOR
THE AWARD OF THE DEGREE IN COMPUTING AND
INFORMATION SYSTEMS OF THE UNIVERSITY OF LONDON*

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

## Conclusion
This project proves the great benefits that a multi-agent approach could provide for the
maze-solving problem with special attention to its greater adaptability for different types of
scenarios and its better performance for most of the considered experiments. If we were to revisit
the benefits and challenges of MARL as identified by Busoniu, Babuska and De Schutter (2008)
and highlighted on Table 2-3, we could conclude the following:

- The additional redundancy provided by the multi-agent approach guarantees greater
adaptability to complex mazes that are better solved from one of its ends.
- The suggested approach seems to have the potential to increase maze-solving speeds if
parallel computation was implemented.
- The dynamic goal approach, while robust in most of the cases, has presented failures on two
scenarios and hence should be further reviewed to check if these issues may be overcomed
with an improved version of the proposed algorithm.
- The minimal communication required between the agents as part of the dynamic goal
concept would help provide simpler implementation on real-life scenarios.
- The suggested approach has shown no problems regarding its scalability when compared
with the rest of the approaches.

Additionally, and while it has not been proved mathematically on this project, based on the
principles of Q-learning, we could estimate that the suggested algorithm could guarantee a
minimum cost path between two points in a maze as long as the general conditions of Q-learning
convergence are respected.

Based on the failures of the multi-agent approach to find the shortest path on two of the
experiments, we could state that maze designs that show greater choices in terms of the directions
on which the agent can move could pose a higher difficulty for the agents to move and establish a
dynamic goal state. This may imply one of the main drawbacks of the suggested approach, because
of the dynamic goal state the agents may get trapped into local optimal solutions. In any case, more
work will be required to find the reasons and implications that this result could have.

Overall, the proposed algorithm could help improve the common applications of
maze-solving techniques by increasing both their range of use and their efficiency. For example,
with regard to increasing their range, on a common navigation application where the algorithm was
to be used to help a robot transport an object from an initial to a goal position, this could now be
extended to a more complex scenario as set below:

*Two robots could cooperate in transporting a certain object while each of them stays
closer to their dock area. This may be required in situations where the robots need to limit
the distance to their docks due to connection range or battery reasons. Along this, splitting
the task between several robots/agents could also allow each of them to implement more
suited features to respond to their particular tasks. For example, one of them may need to
transport the object through a lake and contact the others on solid ground.*

As a general rule, any problem that can be reformulated as a graph can potentially be set as
a maze design and therefore, the suggested algorithm could be used. Despite this, and as mentioned
in Section 2.1, one of the main drawbacks of this proposal with respect to others considered and
evaluated on this project is that we can’t consider directed graphs for this scenario. This itself
means that certain common applications of navigation and routing problems cannot be solved by
the proposed algorithm.

With regards to the scalability, in these simulated environments, the complexity and time
required for the simulation is increased as we increase the number of agents. However, in real
applications, as stated by Kivelevitch and Cohen (2010), “using real robots will keep the
complexity linear with the number of agents in the group”.

Lastly, the lack of an extended communication system for the suggested multi-agent
approach could imply great benefits such as a lower implementation costs. The only communication
between these agents happens when both are in the same state meaning that a short-range
communication technique could be used to notify this when it happens.

### Future work
Having achieved a certain level of success with the suggested algorithm there’s still more
work to do in order to consider it fully successful. The main two issues highlighted by this project
that would required further work are:

1. Understanding why the multi-agent “failed” twice to find the shortest path during standard
training sessions and how the algorithm could be improved to address these .
2. Perform a more detailed analysis on memory requirements and processing power for each of
the approaches that gives more insight on how each of these perform.

Like this, and as it has been shown in previous chapters, making an exhaustive and fair
comparison between the different agents is a really complicated task due to the amount of variables
that need to be individually considered and tested. Ideally, isolated experiments should be prepared
to further consider if any of these variables may have any impact on the performance of each of the
models.

Additionally to these, a study should be undertaken to try to implement the multi-agent
algorithm into two different processing units. This should include details on the communications
required between these and its performance with regards to the experiments that have been carried
out here.

Finally, the considered approaches could be tested on different environments to test how
each of these would perform. This includes but is no limited to some of the following scenarios:

- Several intermediate goal states may be set on the environment so the agent needs to go
through this before reaching the other of the maze. This could be considered an extension of
the suggested application for two robots as suggested in the previous section.
- More complex environments that include moving elements that could block the agent's path.

By considering this, we could prepare the algorithm for real-world applications where
unexpected obstacles may appear on the way.

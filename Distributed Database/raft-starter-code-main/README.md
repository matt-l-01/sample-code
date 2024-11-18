# RAFT (CS3700) - Project 6 - Matthew Love
## High-level Approach
This is an implementation of a simple distributed and replicated key-value datastore across multiple replicas. This allows a client to make put and get requests to the distributed database and receive accurate and reliable responses.

This distributed system utilizes the Raft consensus protocol to allow multiple replicas to run in parallel to maintain consensus among themselves.

## Challenges
The main challenge that I faced while designing this program was ensuring that the repliacs did not start an erroneous election process. When I was in the early stages of development for the system, the repliacs continued to start new elections even though the leader did not die. Therefore, there were unnecessary elections occuring which hinders performance.

I resolved this issue by re-formatting the process to closely align with the Raft protocol for elections and using debugging statements to show the state of the system at certain points in time to resolve any bugs.

## How I Tested
I tested the system by utilizing debug print statements in order to print out the state of the system at certain points in time. Additionally, I used the feedback from the autograder tests to understand how the replicas were interacting with each other and to determine if any changes needed to be made.
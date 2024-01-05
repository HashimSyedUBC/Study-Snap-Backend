# CS 3305A Lecture 5 Summary: Process 

## Pipe()

- Values from parent are copied to the child process but exist in different memory locations in the process.
- A code snippet showcasing this usually involves creating a parent process, setting a fork and determining the separate values for the parent and child.

## Interprocess Communication using Pipe()

- Pipe() function can be used for shared memory, allowing communication between two processes.
- Should be created before fork()
- Allows for Single R/W operations and Multiple R/W operations by parent and child

## Creating a Pipe

- Pipe is created by allocating an array with two integer values representing read and write ports.
- The status of creating the pipe is returned as 0 if successful and -1 if an error occurs.
- pipe[0] - open for reading
- pipe[1] - open for writing

## Fork and Pipes

- Fork() copies the port information to the child
- Both port[0] (read) and port[1] (write) of parent and child point to the same location in the pipe.

## Behaviour of Pipes

- In a full pipe situation, if a writing process tries to write more, the system will automatically block the process until there's room.
- The operating system limits pipe buffer space. Once the limit is reached, 'write' will be blocked.
- In an empty pipe situation, a read attempt will block the process until data is available.

## Example

- Two examples of creating a pipe and how communication between parent and child processes can happen: pipe_SRW.c and pipe_MRW.c.

Each of these subtopics cover the lecture content succinctly and ensures none of the information provided in the lecture is missed out.
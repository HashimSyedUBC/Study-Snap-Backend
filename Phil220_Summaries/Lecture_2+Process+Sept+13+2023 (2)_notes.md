## CS 3305A: Process Basics and Creation Using C

### Copyright Notice:
- Lecture slides provided with permission only for in-class (CS3305A) use. 
- Slides must not be provided or reproduced for anyone outside the class.
- Download copies of slides/lecture recordings are for personal use only.
- These copies must be destructed within 30 days after receiving final course evaluations.

### Topics Covered:
- Process Basics
- Creating a Process using C
- 'fork()' System Call
- Programming Demo: Parent & Child Process (qfork1.c and qfork2.c)

### Process:
- A process is an instance of an application running.
- A process changes state as it executes. 
- Potential states include, New, Running, Waiting, and Terminated.

### Process Control Block (PCB):
- A process is represented in the operating system by a process control block (PCB).
- PCB includes information such as 
  - Process Identifier (PID)
  - Process state
  - Program counter
  - CPU registers
  - CPU-Scheduling information
  - Memory-Management information
  - I/O status information

### Fork Concept:
- The Unix system call for process creation is 'fork()'.
- A child process that is a duplicate of the parent is created through 'fork()'.
- The parent and child have separate copies of the state, stored in separate memory locations.

### Fork System Call:
- Returns > 0 (ID of the child) to the parent and 0 to the child if it succeeds.
- Returns -1 to the parent if it fails (no child is created).
- pid_t data type represents process identifiers.
- Other calls:
  - pid_t getpid() – returns the ID of the calling process.
  - pid_t getppid() – returns the ID of the parent process.
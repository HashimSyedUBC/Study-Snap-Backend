# CS 3305A: Understanding Fork() & Execl() in Process Management 

**Copyright Notice**
- Lecture slides are for in-class use (CS3305A) only.
- Download copies of the slides and/or lecture recordings are for personal use only.
- Students must destroy these copies within 30 days after receipt of final course evaluations.

## Fork() Example 
- Demonstrates the creation of a child process by the parent process.
- Exhibits possible outputs of the parent and child processes. 

## Execution 
- Processes get a share of the CPU to give another process a turn.
- The switching between the parent and child is nondeterministic and relies on various factors like machine load, process scheduling.

## execl() 
- The system call, execl(), replaces a process (the caller process) with a new loaded program. 
- Upon success, execl() never returns; on failure, it returns -1.

## execl() Example Program A
- The binary executable B replaces the Program A after fork() call, executing the statements in Program B while destroying other statements of A's program.

## Fork() and execl() 
- The execl() overlays a new program on the existing process.
- The child process will not return to the old program unless exec fails.

## How many Processes are created by this Program?
- With three fork() calls in the program, eight processes are created including the parent.

## Multiple fork() call Example 
- Illustrates multiple forking from both parent and child processes.
- Total of 7 child processes are created by the parent.
- Each child and parent have different pid's (Process IDs) and ppid's (Parent Process IDs).
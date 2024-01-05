Q: What does the system call execl() do?
Options: 
A) Replaces a process with a new loaded program
B) Calls a new function within an existing program
C) Suspends an ongoing process
D) Creates a new process without affecting the existing one 
Answer: A

Q: On success, what does the system call execl() do?
Options: 
A) Returns 1
B) Returns -1
C) Never returns
D) Returns 0
Answer: C

Q: What does the function fork() do in a program?
Options:
A) It creates a new process by duplicating the existing process
B) It terminates the existing process
C) It pauses the execution of the current process
D) It merges two processes into one
Answer: A

Q: What is the maximum number of processes that can be created by calling fork() three times in a row in a program?
Options:
A) 3
B) 6
C) 7
D) 8
Answer: D

Q: What does getpid() function return?
Options: 
A) The process ID of the parent process
B) The process ID of the current process
C) The number of child processes
D) The process ID of the child process
Answer: B

Q: What is the output of execl() when it fails?
Options: 
A) 0
B) Any positive integer
C) Any non-zero value
D) -1
Answer: D

Q: What happens when the parent process waits using the wait(NULL) statement?
Options: 
A) It waits for any child process to end
B) It waits for a specific child process to end
C) It kills all child processes
D) It stops its own execution
Answer: A

Q: Will a child process return to the old program if the execution of exec in the child process fails?
Options: 
A) Yes
B) No
C) Depends on the return value of exec
D) Only if the parent process allows
Answer: A

Q: What is getppid() function used for?
Options: 
A) To get the process ID of the child process
B) To get the process ID of the parent process
C) To get the number of child processes
D) To get the process ID of the current process
Answer: B

Q: What can be said about the output of a program that includes process scheduling?
Options:
A) It is deterministic
B) It is not deterministic
C) It is always zero
D) It is always the same
Answer: B
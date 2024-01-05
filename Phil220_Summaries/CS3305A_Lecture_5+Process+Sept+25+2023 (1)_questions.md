Q: What does the pipe() function provide?
OPTIONS: 
A: Shared memory for communication between two processes
B: A way of deleting old processes
C: A method for speeding up code execution
D: A tool for organizing file directories
ANSWER: A

Q: When should the pipe() be created?
OPTIONS: 
A: After fork()
B: Before fork()
C: During the execution of fork()
D: There is no specific time
ANSWER: B

Q: If a writing process tries to write to a full pipe, what happens by default?
OPTIONS: 
A: The system will crash
B: The data will be lost
C: The process will automatically block until the pipe is able to receive the data
D: The process will terminate
ANSWER: C

Q: What happens if a read is attempted on an empty pipe?
OPTIONS: 
A: The process will crash
B: The process will terminate
C: The process will block until data is available
D: The process will delete the pipe
ANSWER: C

Q: When is a pipe typically full in a system?
OPTIONS: 
A: When a process attempts to duplicate it
B: When a process tries to communicate with a non-existent process
C: When the buffer space used by the pipe hits its limit
D: When a process gets an error while writing to it
ANSWER: C

Q: What does the fork() function do with the port information?
OPTIONS: 
A: It deletes it
B: It modifies it
C: It copies it to the child
D: It ignores it
ANSWER: C

Q: In the context of pipes and processes, what does the 'port' term refer to?
OPTIONS: 
A: A physical connection point on a computer
B: A point in the memory where data can be read or written
C: A program operating on a computer
D: A security measurement for data transfer
ANSWER: B

Q: What are the two main ports in the context of pipe communication?
OPTIONS: 
A: Delete port and copy port
B: Read port and write port
C: Parent port and child port
D: Fast port and slow port
ANSWER: B

Q: What happens when the status of a pipe equals -1?
OPTIONS: 
A: The pipe was created successfully
B: An error has occurred
C: The pipe is ready to read data
D: The pipe is ready to write data
ANSWER: B

Q: What does 'port[0]' specify in a pipe?
OPTIONS: 
A: It is used for writing
B: It addresses the parent process
C: It is open for reading
D: It signifies an error
ANSWER: C
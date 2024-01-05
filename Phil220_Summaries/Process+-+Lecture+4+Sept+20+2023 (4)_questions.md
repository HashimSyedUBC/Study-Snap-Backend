Q: What does every process have?
Options: 
A: A process file descriptor table
B: A process data table
C: A process function table
D: A process attribution table
Answer: A

Q: What does each entry in process file descriptor table represent?
Options:
A: stdin, stdout, stderr, and file pointer
B: Input, output, error, and data pointer
C: In-file, out-file, error-file, and file pointer
D: Main, function, condition, and file pointer
Answer: A

Q: What happens if a file is opened before a fork?
Options:
A: The child process gets a parent's process file descriptor table. The child and parent share a file pointer
B: The parent process gets a child's process file descriptor table. The parent and child share a file pointer
C: Each process gets a new file descriptor table. Both processes share a file pointer
D: The parent and child do not share any data
Answer: A

Q: What happens if a file is opened after a fork?
Options:
A: Each process gets a new file descriptor table. Both processes share a file pointer
B: The child process gets a parent's process file descriptor table. The child and parent share a file pointer
C: The parent process gets a child's process file descriptor table. The parent and child share a file pointer
D: The parent and child each open a file after the fork. They get their own entries in the file descriptor table
Answer: D

Q: What is the result of assuming that parent and child each open a file after the fork?
Options:
A: The file position information is different
B: The file position information is the same
C: The processes share the same file descriptor table
D: The processes do not have a file descriptor table
Answer: A

Q: What situation is better for opening files in terms of fork?
Options:
A: Before a fork
B: After a fork
C: It doesn't matter when to open files
D: It's recommended to not open files at all
Answer: B

Q: Where do the parent and child point to in a file descriptor table, when a file is opened before a fork?
Options:
A: Different file offsets
B: The same file offset
C: Each other's entries
D: No specific point
Answer: B

Q: Where are parent and child related to each other in the file descriptor table, when a file is opened after a fork?
Options:
A: Both have the same file offset
B: Each has a different file offset 
C: Both point to each other's entries
D: Both have the same entries
Answer: B

Q: In the given example programs, what happens after calling fork()?
Options:
A: A file is opened and read
B: A file is deleted
C: Data is written to a file
D: The program immediately ends
Answer: A

Q: What happens to the file descriptor table upon the destruction of a process?
Options:
A: It gets transferred to a child process
B: It remains in the system's memory
C: It gets deleted from the system's memory
D: It becomes inaccessible but remains in memory
Answer: C
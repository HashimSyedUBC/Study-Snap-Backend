# CS 3305A: Process - Lecture 4
## Date: Sept 20, 2023

### Copyright Notice:
- Lecture slides are provided for use within the class (CS3305A) only. They should not be shared outside of the class or reproduced.
- Downloaded copies of the slides and lecture recordings are for personal use only.
- Such copies must be destroyed within 30 days after final course evaluations are received.

### Topics Covered:

#### 1. Fork and Files
- Every process has a process file descriptor table.
- Each entry in the process file descriptor table represents stdin, stdout, stderr and a file pointer

#### 2. Process File Descriptor Table
- Example given in a program using 'int in_file' and 'in_file = open("list.txt", O_RDONLY)'

#### 3. Fork and Files
- Explanation of opening a file before a fork
    - The child gets a copy of the parent’s process file descriptor table.
    - Parent and child share a file pointer.
- Explanation of opening a file after a fork
    - Parent and child each have individual entries in the file descriptor table.
    - File position information is different for each.

#### 4. fopen() before fork
- Demonstrated through an example 'int main()' function

#### 5. fopen() after fork
- Demonstrated through a similar example 'int main()' function

#### 6. Question
- Discussion on the output of fopen() performed before and after the fork

#### 7. Important Reminder
- Caution about opening files with fork - it's generally better to open files after forking.
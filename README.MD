# Forks in Linux - Demonstrated using Manim
fork() creates a new process by duplicating the calling process.
The new process is referred to as the child process.  The calling
process is referred to as the parent process. <br>

The child process and the parent process run in separate memory
spaces.  At the time of fork() both memory spaces have the same
content. <br>

The child process is an exact duplicate of the parent process
except for the following points: <br>

*  The child has its own unique process ID, and this PID does not
match the ID of any existing process group (setpgid(2)) or
session.

*  The child's parent process ID is the same as the parent's
process ID.

## Output:

https://user-images.githubusercontent.com/104393371/220948522-752e8466-67b5-4bdf-8168-a67378eb24b3.mp4


## References:
- https://www.man7.org/linux/man-pages/man2/fork.2.html - fork()

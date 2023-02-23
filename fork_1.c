#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char *argv[])
{
    fork();
    fork();
    fork();
    printf("Hello!\n");
    return 0;
}
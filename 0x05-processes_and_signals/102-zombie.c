#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>


/**
 * infinite_while - infinite loop
 * Return: 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - program that creates 5 zombie processes.
 * Return: 0
*/
int main(void)
{
	pid_t child;
	int i;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		else if (child < 0)
		{
			perror("Fork failed");
			return (1);
		}
	}

	infinite_while();

return (0);

}

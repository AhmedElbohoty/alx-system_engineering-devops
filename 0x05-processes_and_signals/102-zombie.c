#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - infinite while
 *
 * Return: always success (0)
 */
int infinite_while(void)
{
	while (1)
		sleep(1);

	return (0);
}

/**
 * create_zombie - create zombie process.
 *
 * Return: Nothing.
 */
void create_zombie(void)
{
	pid_t child_pid = fork();

	if (child_pid > 0)
		printf("Zombie process created, PID: %d\n", child_pid);
	else
		exit(0);
}

/**
 * main - Init the program
 *
 * Return: always success (0)
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
		create_zombie();

	infinite_while();

	return (0);
}

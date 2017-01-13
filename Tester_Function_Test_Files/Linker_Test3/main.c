#include <stdio.h>
#include "myHeader.h"

int main(void)
{
	char someString[] = {"This is a clear text string"};

	putchar(10);
	puts(someString);
	do_something(someString);
	puts(someString);

	return 0;
}

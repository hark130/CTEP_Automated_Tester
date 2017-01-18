#include <stdio.h>
#include <ctype.h>

int main(void)
{
	char * currentChar_ptr;

	// Starting point
	char myString[] = {"This is my string!"};
	printf("My String:\t%s\n", myString);

	// To upper
	currentChar_ptr = myString;
	while (*currentChar_ptr)
	{
		*currentChar_ptr = toupper(*currentChar_ptr);
		currentChar_ptr++;
	}
	printf("Upper String:\t%s\n", myString);

	// To lower
	currentChar_ptr = myString;
	while (*currentChar_ptr)
	{
		*currentChar_ptr = tolower(*currentChar_ptr);
		currentChar_ptr++;
	}
	printf("Lower String:\t%s\n", myString);

	// Back again
	myString[0] = toupper(myString[0]);
	printf("Fixed String:\t%s\n", myString);

	return 0;
}

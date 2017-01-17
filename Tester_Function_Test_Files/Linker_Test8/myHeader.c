int do_something(char * string)
{
	int retVal = -1;

	if (string)
	{
		retVal = 0;

		while (*string)
		{
			*string = *string + 1;
			string++;
		}
	}

	return retVal;
}

// tolower()
int do_something_else(char * string)
{
	int retVal = -1;

	if (string)
	{
		retVal = 0;

		while (*string)
		{
			if (*string >= 'A' && *string <= 'Z')
			{
				*string = *string + 32;
			}

			string++;
		}
	}

	return retVal;
}

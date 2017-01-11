# 1. Determine files present  
# 2. Compile source code into object code  
# 3. Link existing object code into a binary executable  
# 4. Execute the binary  
# 5. Save the output of the execution into a file  

import os


'''
    Purpose: Return a list of files that match fileExt and exist in the dir path
    Input:
            dir - a string representing the path in which to search for files
            fileExt - a string or list representation of file extensions to look for
    Ouput:
            A list of appropriate files on success
            An empty list if no matches were made
    Exceptions:
            TypeError if parameters don't match the expected types
            ValueError if dir does not exist
    NOTE:
            If dir is blank or '.', current working directory will be used
            If fileExt is a empty string (or a list that contains an empty string), all files will be matched
'''
def create_file_list(dir, fileExt):
    cflRetVal = [] # Function return value
    fileExtList = [] # List of file extensions to search for
    matchAllFiles = False # Set this to True if all file extensions are to be matched

    # 1. INPUT VALIDATION
    ## 1.1. dir
    if isinstance(dir, str) is False:  # Verify datatype
        raise TypeError('dir is not a string')
    else:
        if dir.__len__() == 0 or dir == '.':
            dir = os.getcwd()
        elif os.path.exists(dir) is False:  # Verify directory exists
            raise ValueError('dir does not exist')

    ## 1.2. fileExt
    ### 1.2.1. Translate the parameter
    if isinstance(fileExt, list) is False:  # Verify acceptable datatype #1
        if isinstance(fileExt, str) is False:  # Verify acceptable datatype #2
            raise TypeError('fileExt is not a string or a list')
        # NO LONGER NECESSARY... BLANK FILE EXTENSIONS ARE CHECKED BELOW
        #elif fileExt.__len__() == 0:
        #    matchAllFiles = True
        else:
            fileExtList = [fileExt]
    else:
        fileExtList = fileExt

    ### 1.2.2. Verify the parameter's content
    if fileExtList.__len__() == 0:  # Verify there is content
        raise ValueError('fileExt is empty')
    else:
        for extension in fileExtList:
            if isinstance(extension, str) is False:  # Verify datatype
                raise ValueError('fileExt contains a non string')
            elif extension.__len__() == 0 or extension == '.':
                matchAllFiles = True
                break # Found a match. Stop looking.

    # 2. WALK DIR
    print('\n') # DEBUGGING
    for file in os.listdir(dir):
#        print("File:\t{}\t{}".format(file,os.path.isfile(file))) # DEBUGGING
        if os.path.isfile(os.path.join(dir, file)) is True:
            for extension in fileExtList:
#                print("file.find(extension):\t{}(file.__len__() - extension.__len__())\t{}".format(file.find(extension),(file.__len__() - extension.__len__()))) # DEBUGGING
                if file.find(extension) == (file.__len__() - extension.__len__()) or matchAllFiles is True:
                    cflRetVal.append(os.path.join(dir,file))
                    break # Found a match.  Move on to the next file.

    return cflRetVal

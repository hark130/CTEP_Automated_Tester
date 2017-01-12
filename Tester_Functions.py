# 1. [X] Determine files present  
# 2. [/] Compile source code into object code  
# 3. [ ] Link existing object code into a binary executable  
# 4. [ ] Execute the binary  
# 5. [ ] Save the output of the execution into a file  

import os
import subprocess
from time import sleep


# 1. Determine files present  
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


# 2. Compile source code into object code
'''
    Purpose: Return a list of object files that have been assembled from any file extension matches (see: fileExt) matches in directory 'dir'
    Input:
            dir - a string representing the path in which to search for files
            fileExt - a string or list representation of file extensions to look for
    Ouput:
            A list of object files that were modified, on success
            An empty list if no matches were made
    Exceptions:
            TypeError if parameters don't match the expected types
            ValueError if dir does not exist
    NOTE:
            This function is currently 'hard-coded' to assemble C files
            If dir is blank or '.', current working directory will be used
            If fileExt is a empty string (or a list that contains an empty string), all files will be matched
'''
def compile_source_to_object(dir, fileExt):
    cstoRetVal = [] # Function return value
    existingObjectMtimes = {} # Dictionary to store the mtimes of pre-existing .obj files

    # 1. GET THE EXISTING FILE LISTS
    ## 1.1. List of files to assemble
    sourceFileList = create_file_list(dir, fileExt)
    ## 1.2. List of existing object files
    existingObjList = create_file_list(dir, '.obj')
    ## 1.3. Store the mtime of any existing object files
    for objectCode in existingObjList:
        existingObjectMtimes[objectCode] = os.path.getmtime(objectCode)


    # 2. LOCATE THE MICROSOFT C/C++ COMPILER
    cmdAbsFilename = 'C:\\Windows\\SysWOW64\\cmd.exe'
    cmdAbsCommand = cmdAbsFilename + '\n\n'
    cmdDevPromptAbsFilename = 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\Common7\\Tools\\VsDevCmd.bat'
#    cmdDevPromptAbsCommand = '"C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\Common7\\Tools\\VsDevCmd.bat"\n\n'
#    cmdDevPromptAbsCommand = '"' + cmdDevPromptAbsFilename + '"' + '\n\n' # Now this variable doesn't have to be updated if cmdDevPromptAbsFilename ever changes
    cmdDevPromptAbsCommand = '"' + cmdDevPromptAbsFilename + '"' + '\n\n' # Now this variable doesn't have to be updated if cmdDevPromptAbsFilename ever changes

    if os.path.exists(cmdAbsFilename) is False:
        raise FileNotFoundError('cmd.exe not found')
    else:
#        print("Found {}".format(cmdAbsFilename)) # DEBUGGING
        pass

    if os.path.exists(cmdDevPromptAbsFilename) is False:
        raise FileNotFoundError('VsDevCmd.bat not found')
    else:
#        print("Found {}".format(cmdDevPromptAbsFilename)) # DEBUGGING
        pass
    
    # 3. SPAWN COMMAND DEVELOPER PROMPT
        try:
            ## 3.1. Invoke cmd.exe
#            cmdDevPromptProcess = subprocess.Popen([cmdPath], stdin=subprocess.PIPE, shell=True)
            cmdDevPromptProcess = subprocess.Popen([cmdAbsCommand], stdin=subprocess.PIPE, shell=True)
        except Exception as err:
            print(repr(err))
        else:
#            print("\nCommand Prompt Started") # DEBUGGING
            pass

            ## 3.2. Invoke VsDevCmd.bat
            try:
                cmdDevPromptProcess.stdin.write(cmdDevPromptAbsCommand.encode())
#                cmdDevPromptProcess.stdin.close() # DEBUGGING
            except Exception as err:
                print(repr(err))
            else:
#                print("\nDeveloper Command Prompt Started") # DEBUGGING
                pass

                # 4. COMPILE SOME FILES
                for sourceFile in sourceFileList:
#                    print("We're about to compile:\t{}".format(sourceFile)) # DEBUGGING
                    changeDirCmd = 'cd ' + os.path.dirname(sourceFile) + '\n\n'
                    compileCmd = 'cl /c ' + sourceFile + '\n\n'

                    try:
                        cmdDevPromptProcess.stdin.write(changeDirCmd.encode()) # Change directory
                        cmdDevPromptProcess.stdin.write(compileCmd.encode()) # Compile
                    except Exception as err:
                        print(repr(err))
                    else:
#                        print("Compiled:\t{}".format(sourceFile)) # DEBUGGING
                        # DIFFERENT APPROACH... UTILIZE CREATE FILE LIST
#                        cstoRetVal.append(sourceFile) # Appends the source file... 
                        pass

                # 5. END THE PROCESS
                try:
                    ## 5.1. Close the stream
                    cmdDevPromptProcess.stdin.close()

                    ## 5.2. Now that the stream is closed, wait for all the commands to finish
                    while cmdDevPromptProcess.poll() is None:
                        sleep(5)

                    cmdDevPromptProcess.terminate()
                except Exception as err:
                    print(repr(err))
                else:
#                    print("The Process Has Ended") # DEBUGGING
                    ## 5.3. Get the current list of object files
                    currentObjList = create_file_list(dir, '.obj')

                    ## 5.4. Test the mtimes of the current list against the existing dictionary
                    for sourceFile in currentObjList:
                        if sourceFile in existingObjList:
                            if existingObjectMtimes.get(sourceFile) is not None:
                                if os.path.getmtime(sourceFile) > existingObjectMtimes.get(sourceFile): # The current .obj mtime is newer than the old mtime
                                    cstoRetVal.append(sourceFile)
#                                    print("This file has changed:\t{}".format(sourceFile)) # DEBUGGING
                                else:
#                                    print("This file has NOT changed:\t{}".format(sourceFile)) # DEBUGGING
                                    pass
                            else: # Odd, the file is in the existingObjList but not in the mtime dictionary
                                raise ValueError("Found an existing .obj file that wasn't in the existingObjectMtimes dictionary:\t{}".format(sourceFile))
                        else: # It's new
                            cstoRetVal.append(sourceFile) 

    return cstoRetVal    












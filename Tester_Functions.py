# 1. [X] Determine files present  
# 2. [X] Assemble source code into object code  
# 3. [X] Link existing object code into a binary executable  
# 4. [/] Execute the binary  
# 5. [/] Save the output of the execution into a file  

import os
import subprocess
from time import sleep
from datetime import datetime


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
            If fileExt is an empty string (or a list that contains an empty string), all files will be matched
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
#    print('\n') # DEBUGGING
    for file in os.listdir(dir):
#        print("File:\t{}\t{}".format(file,os.path.isfile(file))) # DEBUGGING
        if os.path.isfile(os.path.join(dir, file)) is True:
            for extension in fileExtList:
#                print("file.find(extension):\t{}(file.__len__() - extension.__len__())\t{}".format(file.find(extension),(file.__len__() - extension.__len__()))) # DEBUGGING
                if file.find(extension) == (file.__len__() - extension.__len__()) or matchAllFiles is True:
                    cflRetVal.append(os.path.join(dir,file))
                    break # Found a match.  Move on to the next file.

    return cflRetVal


# 2. Assemble source code into object code
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
            If fileExt is an empty string (or a list that contains an empty string), all files will be matched
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


'''
    Purpose: Return an absolute filename, as a string, of a binary executable that's been linked against one or more object files
    Input:
            dir - a string representing the path in which to search for object files
            objFiles - a string or list representation of object code to look for
    Ouput:
            A string representation of the binary's absolute filename, on success
            An empty string if no matches were made
    Exceptions:
            TypeError if parameters don't match the expected types
            ValueError if dir does not exist
            ValueError if one of the entries in objFiles is missing
            RuntimeError if the intended binary was not created
    NOTE:
            BINARY NAME:
                The prepend name of the binary will be the name of the containing directory
                If a binary of that name already exists, -N will be appended where N is the next available number
                (e.g., Proj-Mayhem-7.exe would be compiled if Proj-Mayhem.exe, Proj-Mayhem-2.exe, and Proj-Mayhem-6.exe existed)
            This function is currently 'hard-coded' to link C object code
            If dir is blank or '.', current working directory will be used
            If objFiles is an empty string (or a list that contains an empty string), all .obj files in dir will be matched
'''
# 3. Link existing object code into a binary executable
def link_objects_to_binary(dir, objFiles):
    lotbRetVal = '' # Variable to hold the function's return value
    objFileList = [] # Holds the list of object files to link
    matchAllObjFiles = False # Bool variable to indicate wildcard (*) matching

    cmdAbsFilename = 'C:\\Windows\\SysWOW64\\cmd.exe'
    cmdAbsCommand = cmdAbsFilename + '\n\n'
    cmdDevPromptAbsFilename = 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\Common7\\Tools\\VsDevCmd.bat'
    cmdDevPromptAbsCommand = '"' + cmdDevPromptAbsFilename + '"' + '\n\n' # Now this variable doesn't have to be updated if cmdDevPromptAbsFilename ever changes

    # 0. OPERATING SYSTEM VERIFICATION
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

    # 1. INPUT VALIDATION
    ## 1.1. dir
    if isinstance(dir, str) is False:
        raise TypeError('dir is not a string')
    elif dir.__len__() == 0 or dir == '.':
        dir = os.getcwd()
    else:
        if os.path.exists(dir) is False:
            raise ValueError('dir does not exist')
        elif os.path.isdir(dir) is False:
            raise ValueError('dir is not a directory')

    ## 1.2. objFiles
    ### 1.2.1. Validate the parameter
    if isinstance(objFiles, list) is False:
        if isinstance(objFiles, str) is False:
            raise TypeError('objFiles is not a string or a list')
        else:
            objFileList = [objFiles]
    else:
        objFileList = objFiles
    
    ### 1.2.2. Verify the parameter's content
    if objFileList.__len__() == 0:  # Verify there is content
        objFileList = create_file_list(dir, '.obj') # Match all the .obj files
    else:
        for objFile in objFileList:
            if isinstance(objFile, str) is False:  # Verify datatype
                raise ValueError('objFiles contains a non string')
            elif objFile.__len__() == 0:
                matchAllObjFiles = True
                break # Found a match. Stop looking.

    # 2. PREPARE THE BINARY'S FILENAME
    ## 2.1. Determine parent folder name
    binaryFilename = dir.split('\\') # Split the dirs and filename into a list
    binaryFilename = binaryFilename[binaryFilename.__len__() - 1] # Get the filename from the list's last entry
    
    ## 2.2. Find all the binaries in this directory
    existingBinaryList = create_file_list(dir, '.exe')

    ## 2.3. Find the current highest binary number
    binaryNumber = 0 # Default starting position.  If 0 is the highest, binary file will be linked to <binaryFilename-1>.exe
    for existingBinaryName in existingBinaryList:
        ### 2.3.1. Extract just the filename from the binary absolute paths
        filenameParser = existingBinaryName.split('\\') # Split the dirs and filename into a list
        filenameParser = filenameParser[filenameParser.__len__() - 1] # Get the filename from the list's last entry

        ### 2.3.2. Exclude any binaries that don't start with the binaryFilename
        if filenameParser.find(binaryFilename) == 0: # Ensure the filename actually starts with binaryFilename
            ### 2.3.4. Remove binaryFilename just in case the parent directory contains numbers
            filenameParser = filenameParser[binaryFilename.__len__():]
            filenameDigits = ''.join(char for char in filenameParser if char.isdigit())
            ### 2.3.5. Only the numbers, if any, should be left over.  Verify and check. 
            #### 2.3.5.1 Found some numbers in the binary filename
            if filenameDigits.__len__() > 0:
                if int(filenameDigits) > binaryNumber: 
                    binaryNumber = int(filenameDigits)
            #### 2.3.5.2. No numbers in the binary filename... count it as 1
            elif filenameDigits.__len__() == 0:
                if 1 > binaryNumber:
                    binaryNumber = 1
    # binaryNumber should now hold the highest binary number

    ## 2.4. Setup intended binary name
    if binaryNumber <= 0:
        binaryNumber = 1
    else:
        binaryNumber += 1

    binaryFilename = binaryFilename + '-' + str(binaryNumber) + '.exe'
    
    # 3. SPAWN COMMAND DEVELOPER PROMPT
    try:
        ## 3.1. Invoke cmd.exe
        cmdDevPromptProcess = subprocess.Popen([cmdAbsCommand], stdin=subprocess.PIPE, shell=True)
    except Exception as err:
        print(repr(err))
    else:
#        print("\nCommand Prompt Started") # DEBUGGING
        pass

        ## 3.2. Invoke VsDevCmd.bat
        try:
            cmdDevPromptProcess.stdin.write(cmdDevPromptAbsCommand.encode())
#            cmdDevPromptProcess.stdin.close() # DEBUGGING
        except Exception as err:
            print(repr(err))
        else:
#            print("\nDeveloper Command Prompt Started") # DEBUGGING
            pass

            # 4. LINK SOME FILES
            ## 4.1. Prepare the cd command
            changeDirCmd = 'cd ' + dir + '\n\n'
            ## 4.2. Prepare the link command
            ## 4.2.1. "link" is the command
            linkCmd = 'link '
            ## 4.2.2. Add all the .obj files to the link command
            for objectFile in objFileList:
                linkCmd = linkCmd + objectFile + ' '
                
            ## 4.2.3.
            linkCmd = linkCmd + '/OUT:' + binaryFilename + '\n\n'

            try:
                cmdDevPromptProcess.stdin.write(changeDirCmd.encode()) # Change directory
                cmdDevPromptProcess.stdin.write(linkCmd.encode()) # Link
            except Exception as err:
                print(repr(err))
            else:
#                print("\nLinked:\t{}".format(binaryFilename)) # DEBUGGING
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
#                print("The Process Has Ended") # DEBUGGING
                ## 5.3. Get the absolute filename of the newly linked binary
                lotbRetVal = os.path.join(dir, binaryFilename)

    # 6. VERIFY BINARY IS PRESENT
    if lotbRetVal.__len__() > 0:
        if os.path.exists(lotbRetVal) is False or os.path.isfile(lotbRetVal) is False:
            raise RuntimeError('Linker did not create the binary')
    else:
        raise RuntimeError('Linker command was not executed')

    return lotbRetVal


'''
    Purpose: Run a given binary, capture the binary's output, and store the output into a file
    Input:
            absExeFilename - a string representing the absolute path of the binary to execute
            absOutputFilename - a string representing the intended absolute path of the log file
    Ouput:
            A string representation of the *actual* log file's absolute filename, on success
            An empty string on failure (in lieu of exceptions)
    Exceptions:
            TypeError if parameters don't match the expected types
            ValueError if absExeFilename does not exist
    NOTE:
            If absOutputFilename is blank or ".", file "<ExeFilename>-Output-YYYYMMDD-HHMMSS" will be saved in
                the current working directory.  Example: execute_this_binary("C:\\Users\\hark\\Documents\\Test.exe")
                will save the output in "C:\\Users\\hark\\Documents\\Test-Output-20170117-152755.txt".
            All absOutFilenames will be saved as .txt files.  Any existing file extensions will be stripped.
            If absOutputFilename exists, a timestamp (-YYYYMMDD-HHMMSS) will be added to the filename
            Return value is not guaranteed to match absOutputFilename! (this is to preserve existing log files)
'''
# 4. Execute the binary
# 5. Save the output of the execution into a file
def execute_this_binary(absExeFilename, absOutputFilename=''):
    ebRetVal = absOutputFilename # Variable to hold the functions return value (see: output file)
    addTimestamp = False # Does ebRetVal require a timestamp?  Default, no.
    createOutputFilename = False # Was absOutputFilename blank?  If so, create a filename.  Default, no.
    bareBinaryName = '' # Stores the name of the executable without path or file extension
    dateTimeStamp = '' # Will store the date-time stamp if necessary (format: YYYYMMDD-HHMMSS)

    cmdAbsFilename = 'C:\\Windows\\SysWOW64\\cmd.exe' # Location of cmd.exe
    cmdAbsCommand = cmdAbsFilename + '\n\n' # Preperatory command to send to a subprocess


    # 0. OPERATING SYSTEM VERIFICATION
    if os.path.exists(cmdAbsFilename) is False:
        raise FileNotFoundError('cmd.exe not found')
    else:
#        print("Found {}".format(cmdAbsFilename)) # DEBUGGING
        pass

    # 1. INPUT VALIDATION
    ## 1.1. absExeFilename
    ### 1.1.1. Verify absExeFilename is a string
    if isinstance(absExeFilename, str) is False:
        raise TypeError('absExeFilename is not a string')
    ### 1.1.2. Verify absExeFilename is not blank
    elif absExeFilename.__len__() == 0:
        raise ValueError('absExeFilename is empty')
    ### 1.1.3. Verify absExeFilename exists
    elif os.path.exists(absExeFilename) is False:
        raise ValueError('absExeFilename does not exist')
    ### 1.1.4. Verify absExeFilename is a file
    elif os.path.isfile(absExeFilename) is False:
        raise ValueError('absExeFilename is not a file')
    ### 1.1.5. Verify absExeFilename ends in .exe
    elif absExeFilename.find('.exe') != (absExeFilename.__len__() - '.exe'.__len__()):
        raise ValueError('absExeFilename is not named properly')
    else:
        binaryAbsCommand = '"' + absExeFilename + '"' + '\n\n' # Preperatory command to send to a subprocess

    ## 1.2. absOutputFilename
    ### 1.2.1. Verify absOutputFilename is a string
    if isinstance(absOutputFilename, str) is False:
        raise TypeError('absOutputFilename is not a string')
    ### 1.2.2. Check for absOutputFilename content
    elif absOutputFilename.__len__() == 0 or absOutputFilename == '.':
        createOutputFilename = True
        addTimestamp = True
        ebRetVal = os.getcwd()

    ### 1.2.3. Add a file extension if it's missing from absOutputFilename
    if createOutputFilename is False:
        #### 1.2.3.1. Split the intended output name
        outputFilenameList = absOutputFilename.split('\\')
        #### 1.2.3.2. Check the relative filename for a file extension
        bareFilename = outputFilenameList[outputFilenameList.__len__() - 1]
        if bareFilename.find('.') > 0:
            bareFilename = bareFilename[:bareFilename.find('.')]
        #### 1.2.3.3. Add a .txt file extension
        outputFilenameList[outputFilenameList.__len__() - 1] = bareFilename + '.txt'
        #### 1.2.3.4. Reassemble the absolute filename for the output file
        absOutputFilename = '\\'.join(outputFilenameList)

    ### 1.2.4. Check if absOutputFilename already exists
    if os.path.exists(absOutputFilename) is True:
        if os.path.isfile(absOutputFilename) is True:
            addTimestamp = True
        else:
            raise ValueError('absOutputFilename is not a file')

    ebRetVal = absOutputFilename # Variable to hold the functions return value (see: output file)

    # 2. CREATE DATE-TIME STAMP
    if addTimestamp is True:
        ## N.1.1. Get today's date time
        rightNow = datetime.now()

        ## 2.1.2. Parse today's date time into dateTimeStamp
        dateTimeStamp = rightNow.strftime("%Y%m%d") + '-' + rightNow.strftime("%H%M%S")

#        print("Date Stamp:\t{}".format(dateTimeStamp)) # DEBUGGING


    # 3. CREATE OUTPUT FILENAME
    ## 3.1. Get the binary name
    ### 3.1.1. Split the absolute filename
    bareBinaryName = absExeFilename.split('\\')

    ### 3.1.2. Get the name of the binary
    bareBinaryName = bareBinaryName[bareBinaryName.__len__() - 1]

    ### 3.1.3. Strip the file extension
    if bareBinaryName.find('.') > 0:
        bareBinaryName = bareBinaryName[:bareBinaryName.find('.')]

    ## 3.2. Create output filename
    if createOutputFilename is True:
        ### 3.2.1. Prepend
        ebRetVal = os.path.join(os.getcwd(), bareBinaryName + '-Output')
        ### 3.2.2. Add dateTimeStamp if it exists (and it should)
        if dateTimeStamp.__len__() == 15:
            ebRetVal = ebRetVal + '-' + dateTimeStamp
        ### 3.2.3. Add file extension
        ebRetVal = ebRetVal + '.txt'
    ## 3.3. Check if a timestamp is called for
    else:
        if addTimestamp is True and dateTimeStamp.__len__() == 15:
            ### 3.3.1. Split the absolute output filename
            absOutputFilenameList = absOutputFilename.split('\\')

            ### 3.3.2. Remove the file extension
            outputFilename = absOutputFilenameList[absOutputFilenameList.__len__() - 1]
            if outputFilename.find('.') > 0:
                outputFilename = outputFilename[:outputFilename.find('.')]
            absOutputFilenameList[absOutputFilenameList.__len__() - 1] = outputFilename

            ### 3.3.3. Change the name of the file by appending the dateTimeStamp
            absOutputFilenameList[absOutputFilenameList.__len__() - 1] = absOutputFilenameList[absOutputFilenameList.__len__() - 1] + '-' + dateTimeStamp + '.txt'

            ### 3.3.4. Put it all back together again
            ebRetVal = '\\'.join(absOutputFilenameList)


    # 4. OPEN THE FILE
    try:
        outFile = open(ebRetVal, 'w')
    except Exception as err:
        print(repr(err))
    else:
#        print("\nSuccessfully opened file\n{}".format(ebRetVal)) # DEBUGGING
        pass


    # 5. INVOKE THE BINARY
    ## 5.1. Invoke cmd.exe
    try:
        cmdDevPromptProcess = subprocess.Popen([cmdAbsCommand], stdin=subprocess.PIPE, stdout=outFile, shell=True)
    except Exception as err:
        print(repr(err))
    else:
#        print("\nCommand Prompt Started") # DEBUGGING
        pass

    ## 5.2. Invoke binary through cmd.exe
    try:
        cmdDevPromptProcess.stdin.write(binaryAbsCommand.encode())
#            cmdDevPromptProcess.stdin.close() # DEBUGGING
    except Exception as err:
        print(repr(err))
    else:
#        print("\nBinary Executable Started") # DEBUGGING
        pass   


    # 6. END THE PROCESS
    try:
        ## 6.1. Close the stream
        cmdDevPromptProcess.stdin.close()

        ## 6.2. Now that the stream is closed, wait for all the commands to finish
        while cmdDevPromptProcess.poll() is None:
            sleep(5)

        cmdDevPromptProcess.terminate()
    except Exception as err:
        print(repr(err))
    else:
#        print("The Process Has Ended") # DEBUGGING
        pass


    # 7. CLOSE THE FILE
    try:
        outFile.close()
    except Exception as err:
        print(repr(err))
    else:
#        print("\nSuccessfully closed file\n{}".format(ebRetVal)) # DEBUGGING
        pass


    return ebRetVal



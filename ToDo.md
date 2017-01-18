## CURRENTLY ##
- [X] Determine files present  
- [X] Compile source code into object code  
- [X] Link existing object code into a binary executable  
- [X] Execute the binary  
- [X] Save the output of the execution into a file
- [ ] Refactor the entire process so that one log file is used to store the stdout and stderr for:
	- [ ] compile_source_to_object()
	- [ ] link_objects_to_binary()
	- [ ] execute_this_binary()
    
## FUTURE ##
- [ ] Build a bank of tests that test the module from start to finish
- [ ] Dynamically determine version of Visual Studio  
- [ ] Find fancy 'Windows' method of locating Visual Studio install path instead of hard-coding install directory
- [ ] Investigate CMake as a generic method of compilation that is compiler-agnostic(?)
- [ ] compile_source_to_object() in Tester_Functions.py
    - [ ] Adapt compile_source_to_object() to handle more than just C source code.  (CMake?)
    - [ ] If an old .obj is found, (store? and...) verify it was newly created
- [ ] execute_this_binary() in Tester_Functions.py
	- [ ] Add a safety check to prevent exceeding max filesize of 255
- [ ] Consider the possibility that Popen() output could be redirected to a websocket instead of a file.
		This may aid in communication between the back-end Windows machine (see: compiler) and the CTEP
		front end (see: IDE)
- [ ] Consider modifying execute_this_binary() to take binary arguments as a function argument.    
		Example: execute_this_binary('toupper.exe', 'string', 'output.txt') executes 'toupper.exe string'
			and saves the output to 'output.txt'.

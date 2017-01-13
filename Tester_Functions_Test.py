# To be less confusing, this runs unit tests against Tester_Functions.py

from Tester_Functions import create_file_list # create_file_list(dir, fileExt)
from Tester_Functions import compile_source_to_object # compile_source_to_object(dir, fileExt)
from Tester_Functions import link_objects_to_binary # link_objects_to_binary(dir, objFiles)
import unittest
import os

class CreateFileListTests(unittest.TestCase):

    def test_dir_TypeError1(self):
        try:
            create_file_list(42, ['.txt', '.c'])
        except TypeError as err:
            self.assertEqual(err.args[0], 'dir is not a string')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_dir_TypeError2(self):
        try:
            create_file_list([os.getcwd(), os.path.dirname(os.getcwd())], '.doc')
        except TypeError as err:
            self.assertEqual(err.args[0], 'dir is not a string')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_dir_ValueError1(self):
        try:
            create_file_list(os.path.join(os.getcwd(),'Nonexistent_Directory'), ['.doc','.docx'])
        except ValueError as err:
            self.assertEqual(err.args[0], 'dir does not exist')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_fileExt_TypeError1(self):
        try:
            create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), {1:'1',2:'2',3:'3'})
        except TypeError as err:
            self.assertEqual(err.args[0], 'fileExt is not a string or a list')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_fileExt_TypeError2(self):
        try:
            create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), 3.14)
        except TypeError as err:
            self.assertEqual(err.args[0], 'fileExt is not a string or a list')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_fileExt_ValueError1(self):
        try:
            create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), ['.doc','.docx', 1337])
        except ValueError as err:
            self.assertEqual(err.args[0], 'fileExt contains a non string')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_fileExt_ValueError2(self):
        try:
            create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), [2,3,5,7,11,13])
        except ValueError as err:
            self.assertEqual(err.args[0], 'fileExt contains a non string')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_fileExt_ValueError3(self):
        try:
            create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), [])
        except ValueError as err:
            self.assertEqual(err.args[0], 'fileExt is empty')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_function_Test1(self):
        try:
            result = create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), '.txt')
        except Exception as err:
            print(repr(err))
            self.fail()
        else:
            self.assertEqual(result,[os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt')])

    def test_function_Test2(self):
        try:
            result = create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), ['.txt'])
        except Exception as err:
            print(repr(err))
            self.fail()
        else:
            self.assertEqual(result,[os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt')])

    def test_function_Test3(self):
        try:
            result = create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), ['.txt','.c'])
        except Exception as err:
            print(repr(err))
            self.fail()
        else:
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.c')))

    def test_function_Test4(self):
        try:
            result = create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), '.')
        except Exception as err:
            print(repr(err))
            self.fail()
        else:
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.c')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.py')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_word_document.docx')))            
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_excel_file.xlsx')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_image.bmp')))

    def test_function_Test5(self):
        try:
            result = create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), '')
        except Exception as err:
            print(repr(err))
            self.fail()
        else:
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.c')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.py')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_word_document.docx')))            
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_excel_file.xlsx')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_image.bmp')))


            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.c')))

    def test_function_Test6(self):
        try:
            result = create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), ['.'])
        except Exception as err:
            print(repr(err))
            self.fail()
        else:
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.c')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.py')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_word_document.docx')))            
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_excel_file.xlsx')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_image.bmp')))

    def test_function_Test7(self):
        try:
            result = create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), [''])
        except Exception as err:
            print(repr(err))
            self.fail()
        else:
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.c')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.py')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_word_document.docx')))            
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_excel_file.xlsx')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_image.bmp')))


            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.c')))

    def test_function_Test8(self):
        try:
            result = create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), ['who cares', "what's this", '.'])
        except Exception as err:
            print(repr(err))
            self.fail()
        else:
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.c')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.py')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_word_document.docx')))            
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_excel_file.xlsx')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_image.bmp')))

    def test_function_Test9(self):
        try:
            result = create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), ['who cares', "what's this", ''])
        except Exception as err:
            print(repr(err))
            self.fail()
        else:
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.c')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.py')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_word_document.docx')))            
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_excel_file.xlsx')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_image.bmp')))

    def test_function_Test10(self):
        try:
            result = create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), ['.txt', '.c', ''])
        except Exception as err:
            print(repr(err))
            self.fail()
        else:
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.c')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.py')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_word_document.docx')))            
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_excel_file.xlsx')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_image.bmp')))

    def test_function_Test11(self):
        try:
            result = create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), ['.txt', '.c'])
        except Exception as err:
            print(repr(err))
            self.fail()
        else:
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.c')))
            self.assertEqual(0,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.py')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt')))
            self.assertEqual(0,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_word_document.docx')))            
            self.assertEqual(0,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_excel_file.xlsx')))
            self.assertEqual(0,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_image.bmp')))

    def test_function_Test12(self):
        try:
            result = create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), '.doc')
        except Exception as err:
            print(repr(err))
            self.fail()
        else:
            self.assertEqual(0,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.c')))
            self.assertEqual(0,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.py')))
            self.assertEqual(0,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt')))
            self.assertEqual(0,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_word_document.docx')))            
            self.assertEqual(0,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_excel_file.xlsx')))
            self.assertEqual(0,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_image.bmp')))

    def test_function_Test13(self):
        try:
            result = create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), 'ocx')
        except Exception as err:
            print(repr(err))
            self.fail()
        else:
            self.assertEqual(0,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.c')))
            self.assertEqual(0,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.py')))
            self.assertEqual(0,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_word_document.docx')))            
            self.assertEqual(0,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_excel_file.xlsx')))
            self.assertEqual(0,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_image.bmp')))

class CompileSourceToObjectTests(unittest.TestCase):

    def test_dir_TypeError1(self):
        try:
            compile_source_to_object(42, ['.txt', '.c'])
        except TypeError as err:
            self.assertEqual(err.args[0], 'dir is not a string')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_dir_TypeError2(self):
        try:
            compile_source_to_object([os.getcwd(), os.path.dirname(os.getcwd())], '.doc')
        except TypeError as err:
            self.assertEqual(err.args[0], 'dir is not a string')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_dir_ValueError1(self):
        try:
            compile_source_to_object(os.path.join(os.getcwd(),'Nonexistent_Directory'), ['.doc','.docx'])
        except ValueError as err:
            self.assertEqual(err.args[0], 'dir does not exist')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_fileExt_TypeError1(self):
        try:
            compile_source_to_object(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), {1:'1',2:'2',3:'3'})
        except TypeError as err:
            self.assertEqual(err.args[0], 'fileExt is not a string or a list')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_fileExt_TypeError2(self):
        try:
            compile_source_to_object(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), 3.14)
        except TypeError as err:
            self.assertEqual(err.args[0], 'fileExt is not a string or a list')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_fileExt_ValueError1(self):
        try:
            compile_source_to_object(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), ['.doc','.docx', 1337])
        except ValueError as err:
            self.assertEqual(err.args[0], 'fileExt contains a non string')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_fileExt_ValueError2(self):
        try:
            compile_source_to_object(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), [2,3,5,7,11,13])
        except ValueError as err:
            self.assertEqual(err.args[0], 'fileExt contains a non string')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_fileExt_ValueError3(self):
        try:
            compile_source_to_object(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), [])
        except ValueError as err:
            self.assertEqual(err.args[0], 'fileExt is empty')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_function_Test1(self):
        # Remove any existing .obj files
        for existingFile in os.listdir(os.path.join(os.getcwd(),'Tester_Function_Test_Files')):
            if existingFile.find('.obj') == (existingFile.__len__() - '.obj'.__len__()):
                try:
                    os.remove(os.path.join(os.getcwd(),'Tester_Function_Test_Files', existingFile))
                except Exception as err:
                    print("Unable to remove .obj file:\t{}".format(existingFile))
                    print(repr(err))

        # Attempt to assemble .obj files
        try:
            result = compile_source_to_object(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), '.c')
        except Exception as err:
            print(repr(err))
            self.fail('Raised an exception')
        else:
            # Verify return values
            self.assertTrue(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Test.obj') in result)
            self.assertTrue(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Hello_world.obj') in result)
            self.assertFalse(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Not_A_Source_File.obj') in result)
            
            # Verify the status of .obj files
            self.assertTrue(os.path.exists(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Test.obj')))
            self.assertTrue(os.path.exists(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Hello_world.obj')))
            # Not_A_Source_File.c should *NOT* assemble into an object file!
            self.assertFalse(os.path.exists(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Not_A_Source_File.obj'))) 
        finally:
            # CLEANUP - Remove any existing .obj files because we don't want them in the repository
            for existingFile in os.listdir(os.path.join(os.getcwd(),'Tester_Function_Test_Files')):
                if existingFile.find('.obj') == (existingFile.__len__() - '.obj'.__len__()):
                    try:
                        os.remove(os.path.join(os.getcwd(),'Tester_Function_Test_Files', existingFile))
                    except Exception as err:
                        print("Unable to remove .obj file:\t{}".format(existingFile))
                        print(repr(err))

    def test_function_Test2(self):
        # Remove any existing .obj files
        for existingFile in os.listdir(os.path.join(os.getcwd(),'Tester_Function_Test_Files')):
            if existingFile.find('.obj') == (existingFile.__len__() - '.obj'.__len__()):
                try:
                    os.remove(os.path.join(os.getcwd(),'Tester_Function_Test_Files', existingFile))
                except Exception as err:
                    print("Unable to remove .obj file:\t{}".format(existingFile))
                    print(repr(err))

        # Create a dummy file
        dummyAbsFilename = os.path.join(os.getcwd(),'Tester_Function_Test_Files','DUMMY_OBJECT_FILE.obj')
        dummyFile = open(dummyAbsFilename, 'w')
        dummyFile.write('# This is not actually an object file.')
        dummyFile.close()

        # Attempt to assemble .obj files
        try:
            result = compile_source_to_object(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), '.c')
        except Exception as err:
            print(repr(err))
            self.fail('Raised an exception')
        else:
            # Verify return values
            self.assertTrue(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Test.obj') in result)
            self.assertTrue(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Hello_world.obj') in result)
            # Not_A_Source_File.c should *NOT* assemble into an object file!
            self.assertFalse(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Not_A_Source_File.obj') in result) 
            # DUMMY_OBJECT_FILE.obj should *NOT* be modified so it shouldn't be in the list!
            self.assertFalse(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'DUMMY_OBJECT_FILE.obj') in result) 
            
            # Verify the status of .obj files
            self.assertTrue(os.path.exists(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Test.obj')))
            self.assertTrue(os.path.exists(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Hello_world.obj')))
            self.assertFalse(os.path.exists(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Not_A_Source_File.obj')))
            self.assertTrue(os.path.exists(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'DUMMY_OBJECT_FILE.obj'))) # Should still be here at this point
        finally:
            # Regardless of what happens, get rid of the dummy.obj file
            if os.path.exists(dummyAbsFilename) is True:
                try:
                    os.remove(dummyAbsFilename)
                except Exception as err:
                    print("Unable to remove dummy .obj file:\t{}".format(dummyAbsFilename))
                    print(repr(err))    

            # CLEANUP - Remove any existing .obj files because we don't want them in the repository
            for existingFile in os.listdir(os.path.join(os.getcwd(),'Tester_Function_Test_Files')):
                if existingFile.find('.obj') == (existingFile.__len__() - '.obj'.__len__()):
                    try:
                        os.remove(os.path.join(os.getcwd(),'Tester_Function_Test_Files', existingFile))
                    except Exception as err:
                        print("Unable to remove .obj file:\t{}".format(existingFile))
                        print(repr(err))

    def test_function_Test3(self):
        # Remove any existing .obj files
        for existingFile in os.listdir(os.path.join(os.getcwd(),'Tester_Function_Test_Files')):
            if existingFile.find('.obj') == (existingFile.__len__() - '.obj'.__len__()):
                try:
                    os.remove(os.path.join(os.getcwd(),'Tester_Function_Test_Files', existingFile))
                except Exception as err:
                    print("Unable to remove .obj file:\t{}".format(existingFile))
                    print(repr(err))

        # Attempt to assemble .obj files
        try:
            # Conventional usage of compile_source_to_object()
            result = compile_source_to_object(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), '.c')
        except Exception as err:
            print(repr(err))
            self.fail('Raised an exception')
        else:
            # Verify return values
            self.assertTrue(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Test.obj') in result)
            self.assertTrue(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Hello_world.obj') in result)
            # Not_A_Source_File.c should *NOT* assemble into an object file!
            self.assertFalse(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Not_A_Source_File.obj') in result) 
            # DUMMY_OBJECT_FILE.obj should *NOT* be modified so it shouldn't be in the list!
            self.assertFalse(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'DUMMY_OBJECT_FILE.obj') in result) 
            
            # Verify the status of .obj files
            self.assertTrue(os.path.exists(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Test.obj')))
            self.assertTrue(os.path.exists(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Hello_world.obj')))
            self.assertFalse(os.path.exists(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Not_A_Source_File.obj')))

        # Attempt to assemble Test.obj
        try:
            # Not a conventional use of compile_source_to_object() but this syntax should only assemble Test.c
            result = compile_source_to_object(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), 'Test.c')
        except Exception as err:
            print(repr(err))

            # CLEANUP - Remove any existing .obj files because we don't want them in the repository
            for existingFile in os.listdir(os.path.join(os.getcwd(),'Tester_Function_Test_Files')):
                if existingFile.find('.obj') == (existingFile.__len__() - '.obj'.__len__()):
                    try:
                        os.remove(os.path.join(os.getcwd(),'Tester_Function_Test_Files', existingFile))
                    except Exception as err:
                        print("Unable to remove .obj file:\t{}".format(existingFile))
                        print(repr(err))

            self.fail('Raised an exception')
        else:
            # Verify return values
            self.assertTrue(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Test.obj') in result)
            self.assertFalse(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Hello_world.obj') in result)
            # Not_A_Source_File.c should *NOT* assemble into an object file!
            self.assertFalse(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Not_A_Source_File.obj') in result) 
            # DUMMY_OBJECT_FILE.obj should *NOT* be modified so it shouldn't be in the list!
            self.assertFalse(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'DUMMY_OBJECT_FILE.obj') in result) 
            
            # Verify the status of .obj files
            self.assertTrue(os.path.exists(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Test.obj')))
            self.assertTrue(os.path.exists(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Hello_world.obj')))
            self.assertFalse(os.path.exists(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Not_A_Source_File.obj')))
        finally:
            # CLEANUP - Remove any existing .obj files because we don't want them in the repository
            for existingFile in os.listdir(os.path.join(os.getcwd(),'Tester_Function_Test_Files')):
                if existingFile.find('.obj') == (existingFile.__len__() - '.obj'.__len__()):
                    try:
                        os.remove(os.path.join(os.getcwd(),'Tester_Function_Test_Files', existingFile))
                    except Exception as err:
                        print("Unable to remove .obj file:\t{}".format(existingFile))
                        print(repr(err))
   
    def test_function_Test4(self):
        # Remove any existing .obj files
        for existingFile in os.listdir(os.path.join(os.getcwd(),'Tester_Function_Test_Files')):
            if existingFile.find('.obj') == (existingFile.__len__() - '.obj'.__len__()):
                try:
                    os.remove(os.path.join(os.getcwd(),'Tester_Function_Test_Files', existingFile))
                except Exception as err:
                    print("Unable to remove .obj file:\t{}".format(existingFile))
                    print(repr(err))

        # Attempt to assemble .obj files
        try:
            result = compile_source_to_object(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), '.abc')
        except Exception as err:
            print(repr(err))
            self.fail('Raised an exception')
        else:
            # Verify return values
            self.assertFalse(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Test.obj') in result)
            self.assertFalse(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Hello_world.obj') in result)
            self.assertFalse(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Not_A_Source_File.obj') in result)
            self.assertTrue(result.__len__() == 0)
            
            # Verify the status of .obj files
            self.assertFalse(os.path.exists(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Test.obj')))
            self.assertFalse(os.path.exists(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Hello_world.obj')))
            # Not_A_Source_File.c should *NOT* assemble into an object file!
            self.assertFalse(os.path.exists(os.path.join(os.getcwd(),'Tester_Function_Test_Files', 'Not_A_Source_File.obj'))) 
        finally:
            # CLEANUP - Remove any existing .obj files because we don't want them in the repository
            for existingFile in os.listdir(os.path.join(os.getcwd(),'Tester_Function_Test_Files')):
                if existingFile.find('.obj') == (existingFile.__len__() - '.obj'.__len__()):
                    try:
                        os.remove(os.path.join(os.getcwd(),'Tester_Function_Test_Files', existingFile))
                    except Exception as err:
                        print("Unable to remove .obj file:\t{}".format(existingFile))
                        print(repr(err))

class LinkObjectsToBinaryTests(unittest.TestCase):

    def test_dir_TypeError1(self):
        try:
            link_objects_to_binary(42, ['some.obj', 'some_other.obj'])
        except TypeError as err:
            self.assertEqual(err.args[0], 'dir is not a string')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_dir_TypeError2(self):
        try:
            link_objects_to_binary([os.getcwd(), os.path.dirname(os.getcwd())], 'some.obj')
        except TypeError as err:
            self.assertEqual(err.args[0], 'dir is not a string')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_dir_ValueError1(self):
        try:
            link_objects_to_binary(os.path.join(os.getcwd(),'Nonexistent_Directory'), ['Doc.obj','Holiday.obj'])
        except ValueError as err:
            self.assertEqual(err.args[0], 'dir does not exist')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_dir_ValueError2(self):
        try:
            link_objects_to_binary(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Test.c'), ['Doc.obj','Holiday.obj'])
        except ValueError as err:
            self.assertEqual(err.args[0], 'dir is not a directory')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_fileExt_TypeError1(self):
        try:
            link_objects_to_binary(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), {1:'1',2:'2',3:'3'})
        except TypeError as err:
            self.assertEqual(err.args[0], 'objFiles is not a string or a list')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_fileExt_TypeError2(self):
        try:
            link_objects_to_binary(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), 3.14)
        except TypeError as err:
            self.assertEqual(err.args[0], 'objFiles is not a string or a list')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_fileExt_ValueError1(self):
        try:
            link_objects_to_binary(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), ['some.obj','some_other.obj', 1337])
        except ValueError as err:
            self.assertEqual(err.args[0], 'objFiles contains a non string')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

    def test_fileExt_ValueError2(self):
        try:
            link_objects_to_binary(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), [2,3,5,7,11,13])
        except ValueError as err:
            self.assertEqual(err.args[0], 'objFiles contains a non string')
        except Exception as err:
            print(repr(err))
            self.fail('Raised the wrong exception')

#   Test 0 - link_objects_to_binary() 
#       - Verifies function won't get mixed up with binaries that happen to have words after the filename prepend
#       - Verifies it will skip counting a binary that doesn't belong
#       - Verifies it will properly count filename numbering that is not sequential
    def test_function_Test0(self):
        testDir = 'Linker_Test0'
        testFilenamePrepend = testDir + '-'
        expectedBinaryNumber = '8'
        testPath = os.path.join(os.getcwd(), 'Tester_Function_Test_Files', testDir)
        testFiles = create_file_list(testPath, '.obj') # A bit incestuous but it's a useful function
        testBinary = os.path.join(os.getcwd(), 'Tester_Function_Test_Files', testDir, testFilenamePrepend + expectedBinaryNumber + '.exe')

        try:
            result = link_objects_to_binary(testPath, testFiles)
        except Exception as err:
            print(repr(err))
            self.fail('Raised an exception')
        else:
            self.assertTrue(isinstance(result, str)) # Return value should be a string
            self.assertTrue(result.__len__() > 0) # We're expecting something
            self.assertTrue(os.path.exists(result)) # The function claims it made a binary so it should exist
            self.assertTrue(os.path.isfile(result)) # The function claims it made a binary so it should be a file
            self.assertTrue(os.path.exists(testBinary)) # We're expecting to see this binary
            self.assertTrue(os.path.isfile(testBinary)) # We're expecting to see this binary as a file
        finally:
            checkNextFile = False # Global continue
            # Cleanup any stray binaries of the Linker_Test0-8.exe, Linker_Test0-9.exe, etc variety
            for file in os.listdir(testPath):
                checkNextFile = False # Reset the global continue
                if file.find(testFilenamePrepend) == 0:
                    # Remove prepended filename
                    trimmedFile = file[file.find(testFilenamePrepend) + testFilenamePrepend.__len__():]
                    
                    if trimmedFile.find('.exe') >= 0:
                        trimmedFile = trimmedFile[:trimmedFile.find('.exe')]

                        for char in trimmedFile:
                            if char.isdigit() is False:
#                                os.remove(os.path.join(testPath,file))
                                checkNextFile = True
                                break # This filename has words.  It's part of the test.

                        if checkNextFile == True:
                            continue
                        # Made it through without any non-numbers
                        elif int(trimmedFile) >= int(expectedBinaryNumber):
                            os.remove(os.path.join(testPath,file))

            if os.path.exists(testBinary) is True and os.path.isfile(testBinary):
                os.remove(testBinary)

#   Test 1 - link_objects_to_binary() 
#       - This test merely checks for basic functionality
#       - No tricks, no misplaced binaries, binary numbers are sequential
    def test_function_Test1(self):
        testDir = 'Linker_Test1'
        testFilenamePrepend = testDir + '-'
        expectedBinaryNumber = '4'
        testPath = os.path.join(os.getcwd(), 'Tester_Function_Test_Files', testDir)
        testFiles = create_file_list(testPath, '.obj') # A bit incestuous but it's a useful function
        testBinary = os.path.join(os.getcwd(), 'Tester_Function_Test_Files', testDir, testFilenamePrepend + expectedBinaryNumber + '.exe')

        try:
            result = link_objects_to_binary(testPath, testFiles)
        except Exception as err:
            print(repr(err))
            self.fail('Raised an exception')
        else:
            self.assertTrue(isinstance(result, str)) # Return value should be a string
            self.assertTrue(result.__len__() > 0) # We're expecting something
            self.assertTrue(os.path.exists(result)) # The function claims it made a binary so it should exist
            self.assertTrue(os.path.isfile(result)) # The function claims it made a binary so it should be a file
            self.assertTrue(os.path.exists(testBinary)) # We're expecting to see this binary
            self.assertTrue(os.path.isfile(testBinary)) # We're expecting to see this binary as a file
        finally:
            checkNextFile = False # Global continue
            # Cleanup any stray binaries of the Linker_Test0-8.exe, Linker_Test0-9.exe, etc variety
            for file in os.listdir(testPath):
                checkNextFile = False # Reset the global continue
                if file.find(testFilenamePrepend) == 0:
                    # Remove prepended filename
                    trimmedFile = file[file.find(testFilenamePrepend) + testFilenamePrepend.__len__():]
                    
                    if trimmedFile.find('.exe') >= 0:
                        trimmedFile = trimmedFile[:trimmedFile.find('.exe')]

                        for char in trimmedFile:
                            if char.isdigit() is False:
#                                os.remove(os.path.join(testPath,file))
                                checkNextFile = True
                                break # This filename has words.  It's part of the test.

                        if checkNextFile == True:
                            continue
                        # Made it through without any non-numbers
                        elif int(trimmedFile) >= int(expectedBinaryNumber):
                            os.remove(os.path.join(testPath,file))

            if os.path.exists(testBinary) is True and os.path.isfile(testBinary):
                os.remove(testBinary)

#   Test 2 - link_objects_to_binary() 
#       - Tests the ability to properly distinguish between binaries that belong here and binaries that don't
#       - Tests the ability to properly handle single digit and double digit binary numbers
    def test_function_Test2(self):
        testDir = 'Linker_Test2'
        testFilenamePrepend = testDir + '-'
        expectedBinaryNumber = '11'
        testPath = os.path.join(os.getcwd(), 'Tester_Function_Test_Files', testDir)
        testFiles = create_file_list(testPath, '.obj') # A bit incestuous but it's a useful function
        testBinary = os.path.join(os.getcwd(), 'Tester_Function_Test_Files', testDir, testFilenamePrepend + expectedBinaryNumber + '.exe')

        try:
            result = link_objects_to_binary(testPath, testFiles)
        except Exception as err:
            print(repr(err))
            self.fail('Raised an exception')
        else:
            self.assertTrue(isinstance(result, str)) # Return value should be a string
            self.assertTrue(result.__len__() > 0) # We're expecting something
            self.assertTrue(os.path.exists(result)) # The function claims it made a binary so it should exist
            self.assertTrue(os.path.isfile(result)) # The function claims it made a binary so it should be a file
            self.assertTrue(os.path.exists(testBinary)) # We're expecting to see this binary
            self.assertTrue(os.path.isfile(testBinary)) # We're expecting to see this binary as a file
        finally:
            checkNextFile = False # Global continue
            # Cleanup any stray binaries of the Linker_Test0-8.exe, Linker_Test0-9.exe, etc variety
            for file in os.listdir(testPath):
                checkNextFile = False # Reset the global continue
                if file.find(testFilenamePrepend) == 0:
                    # Remove prepended filename
                    trimmedFile = file[file.find(testFilenamePrepend) + testFilenamePrepend.__len__():]
                    
                    if trimmedFile.find('.exe') >= 0:
                        trimmedFile = trimmedFile[:trimmedFile.find('.exe')]

                        for char in trimmedFile:
                            if char.isdigit() is False:
#                                os.remove(os.path.join(testPath,file))
                                checkNextFile = True
                                break # This filename has words.  It's part of the test.

                        if checkNextFile == True:
                            continue
                        # Made it through without any non-numbers
                        elif int(trimmedFile) >= int(expectedBinaryNumber):
                            os.remove(os.path.join(testPath,file))

            if os.path.exists(testBinary) is True and os.path.isfile(testBinary):
                os.remove(testBinary)

#   Test 3 - link_objects_to_binary() 
#       - Tests the ability to link two object files
#       - Tests the ability to count a binary file that has no number as one (1)
    def test_function_Test3(self):
        testDir = 'Linker_Test3'
        testFilenamePrepend = testDir + '-'
        expectedBinaryNumber = '2'
        testPath = os.path.join(os.getcwd(), 'Tester_Function_Test_Files', testDir)
        testFiles = create_file_list(testPath, '.obj') # A bit incestuous but it's a useful function
        testBinary = os.path.join(os.getcwd(), 'Tester_Function_Test_Files', testDir, testFilenamePrepend + expectedBinaryNumber + '.exe')

        try:
            result = link_objects_to_binary(testPath, testFiles)
        except Exception as err:
            print(repr(err))
            self.fail('Raised an exception')
        else:
            self.assertTrue(isinstance(result, str)) # Return value should be a string
            self.assertTrue(result.__len__() > 0) # We're expecting something
            self.assertTrue(os.path.exists(result)) # The function claims it made a binary so it should exist
            self.assertTrue(os.path.isfile(result)) # The function claims it made a binary so it should be a file
            self.assertTrue(os.path.exists(testBinary)) # We're expecting to see this binary
            self.assertTrue(os.path.isfile(testBinary)) # We're expecting to see this binary as a file
        finally:
            checkNextFile = False # Global continue
            # Cleanup any stray binaries of the Linker_Test0-8.exe, Linker_Test0-9.exe, etc variety
            for file in os.listdir(testPath):
                checkNextFile = False # Reset the global continue
                if file.find(testFilenamePrepend) == 0:
                    # Remove prepended filename
                    trimmedFile = file[file.find(testFilenamePrepend) + testFilenamePrepend.__len__():]
                    
                    if trimmedFile.find('.exe') >= 0:
                        trimmedFile = trimmedFile[:trimmedFile.find('.exe')]

                        for char in trimmedFile:
                            if char.isdigit() is False:
#                                os.remove(os.path.join(testPath,file))
                                checkNextFile = True
                                break # This filename has words.  It's part of the test.

                        if checkNextFile == True:
                            continue
                        # Made it through without any non-numbers
                        elif int(trimmedFile) >= int(expectedBinaryNumber):
                            os.remove(os.path.join(testPath,file))

            if os.path.exists(testBinary) is True and os.path.isfile(testBinary):
                os.remove(testBinary)

#   Test 4 - link_objects_to_binary() 
#       - Tests the ability to link three object files
#       - Tests the ability to increment an executable number from two digits to three (99 to 100)
#       - Tests the ability to ignore .obj files that exist but weren't included
    def test_function_Test4(self):
        testDir = 'Linker_Test4'
        testFilenamePrepend = testDir + '-'
        expectedBinaryNumber = '100'
        testPath = os.path.join(os.getcwd(), 'Tester_Function_Test_Files', testDir)
#        testFiles = create_file_list(testPath, '.obj') # A bit incestuous but it's a useful function
        # Leave out all other .obj files... namely Do_Not_Link_This.obj
        testFiles = [os.path.join(testPath, 'main.obj'), os.path.join(testPath, 'myHeader.obj'), os.path.join(testPath, 'myOtherHeader.obj')]
        testBinary = os.path.join(os.getcwd(), 'Tester_Function_Test_Files', testDir, testFilenamePrepend + expectedBinaryNumber + '.exe')

        try:
            result = link_objects_to_binary(testPath, testFiles)
        except Exception as err:
            print(repr(err))
            self.fail('Raised an exception')
        else:
            self.assertTrue(isinstance(result, str)) # Return value should be a string
            self.assertTrue(result.__len__() > 0) # We're expecting something
            self.assertTrue(os.path.exists(result)) # The function claims it made a binary so it should exist
            self.assertTrue(os.path.isfile(result)) # The function claims it made a binary so it should be a file
            self.assertTrue(os.path.exists(testBinary)) # We're expecting to see this binary
            self.assertTrue(os.path.isfile(testBinary)) # We're expecting to see this binary as a file
        finally:
            checkNextFile = False # Global continue
            # Cleanup any stray binaries of the Linker_Test0-8.exe, Linker_Test0-9.exe, etc variety
            for file in os.listdir(testPath):
                checkNextFile = False # Reset the global continue
                if file.find(testFilenamePrepend) == 0:
                    # Remove prepended filename
                    trimmedFile = file[file.find(testFilenamePrepend) + testFilenamePrepend.__len__():]
                    
                    if trimmedFile.find('.exe') >= 0:
                        trimmedFile = trimmedFile[:trimmedFile.find('.exe')]

                        for char in trimmedFile:
                            if char.isdigit() is False:
#                                os.remove(os.path.join(testPath,file))
                                checkNextFile = True
                                break # This filename has words.  It's part of the test.

                        if checkNextFile == True:
                            continue
                        # Made it through without any non-numbers
                        elif int(trimmedFile) >= int(expectedBinaryNumber):
                            os.remove(os.path.join(testPath,file))

            if os.path.exists(testBinary) is True and os.path.isfile(testBinary):
                os.remove(testBinary)

if __name__ == '__main__':
    # Necessary test files (doesn't matter if they're empty, they merely need to exist)
    testFiles = []
    testFiles.append(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Test.c'))
    testFiles.append(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Not_A_Source_File.c'))
    testFiles.append(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.c'))
    testFiles.append(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.py'))
    testFiles.append(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt'))
    testFiles.append(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_word_document.docx'))          
    testFiles.append(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_excel_file.xlsx'))
    testFiles.append(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_image.bmp'))

    # Verify they're present
    for file in testFiles:
        if os.path.exists(file) is False:
            newFile = open(file,'w')

            if file.find('Hello_world.c') >= 0:
                newFile.write('# This file has been created by the CompileSourceToObjectTests class in Tester_Functions_Test.py\n#include <stdio.h>\nint main(void)\n{\n\tputs("Hello world");\n\treturn 0\n;}')
            elif file.find('Test.c') >= 0:
                newFile.write('# This file has been created by the CompileSourceToObjectTests class in Tester_Functions_Test.py\n#include <stdio.h>\nint main(void)\n{\n\tputs("This is a test");\n\tputs("This is only a test");\n\n\treturn 0;\n}\n') 
            elif file.find('Not_A_Source_File.c') >= 0:
                newFile.write('# This file has been created by the CompileSourceToObjectTests class in Tester_Functions_Test.py\n# This is not a C source file\n# It should not be compiled\n')
            elif file.find('.py') >= 0:
                newFile.write('# This file has been created by the CompileSourceToObjectTests class in Tester_Functions_Test.py\nprint("Hellow world")')

            newFile.close()

    # CompileSourceToObjectTests class tests take too long
    # Change Tester_Functions_Test.py back to unittest.main() prior to final commit/push
    #unittest.main(verbosity=2) 

    linkerSuite = unittest.TestLoader().loadTestsFromTestCase(LinkObjectsToBinaryTests)
    unittest.TextTestRunner(verbosity=2).run(linkerSuite)

    print("Done Testing")



# To be less confusing, this runs unit tests against Tester_Functions.py

from Tester_Functions import create_file_list # create_file_list(dir, fileExt)
import unittest
import os

class CreateFileList(unittest.TestCase):

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

    def test_fileExt_Test1(self):
        try:
            result = create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), '.txt')
        except Exception as err:
            print(repr(err))
            self.fail()
        else:
            self.assertEqual(result,[os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt')])

    def test_fileExt_Test2(self):
        try:
            result = create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), ['.txt'])
        except Exception as err:
            print(repr(err))
            self.fail()
        else:
            self.assertEqual(result,[os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt')])

    def test_fileExt_Test3(self):
        try:
            result = create_file_list(os.path.join(os.getcwd(),'Tester_Function_Test_Files'), ['.txt','.c'])
        except Exception as err:
            print(repr(err))
            self.fail()
        else:
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt')))
            self.assertEqual(1,result.count(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.c')))

    def test_fileExt_Test4(self):
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

    def test_fileExt_Test5(self):
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

    def test_fileExt_Test6(self):
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

    def test_fileExt_Test7(self):
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

    def test_fileExt_Test8(self):
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

    def test_fileExt_Test9(self):
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

    def test_fileExt_Test10(self):
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

    def test_fileExt_Test11(self):
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

    def test_fileExt_Test12(self):
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

    def test_fileExt_Test13(self):
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

if __name__ == '__main__':
    # Necessary test files (doesn't matter if they're empty, they merely need to exist)
    testFiles = []
    testFiles.append(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.c'))
    testFiles.append(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'Hello_world.py'))
    testFiles.append(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_text_file.txt'))
    testFiles.append(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_a_word_document.docx'))          
    testFiles.append(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_excel_file.xlsx'))
    testFiles.append(os.path.join(os.getcwd(), 'Tester_Function_Test_Files', 'This_is_an_image.bmp'))

    # Verify their present
    for file in testFiles:
        if os.path.exists(file) is False:
            newFile = open(file,'w')
            newFile.close()

    unittest.main()
    print("Done Testing")
def main():
    #open file in write mode('w')
    with open("my_file.text", "w")as file:
        #write line of text to the file
        file.write("This is line 2.\n")
        file.write("12345.\n") #writing a mixture of strings and numbers
        file.write("Another line with some text.\n")

     #open file in read mode('r')
        with open("my_file.text","r")as file:
        #read and display the contents of the file
            contents=file.read()
            print("contents of my_file.text:")
            print(contents)

     #open file in append mode('a')
            with open("my_file.text","a")as file:
               # append additional line of text to the file
                file.write("This is an appended line.\n")
                file.write("67890.\n") #Appending a mixtute of strings and numbers
                file.write("One more line appended.\n")

      #open file in read mode('r')
                with open("my_file.text","r")as file:
                    #Read and display the updated contents of the file
                    contents=file.read()
                    print("contents of my_file.text after appending:")
                    print(contents)


Except:FileNotFoundError
print("Error:The specified file was not found.")
Except:PermissionError
print("Error: Permission denied wile tring to access this file.")
Except:Exception
print("An error occured:")
Finally:print
print("script excecution complete")



                          

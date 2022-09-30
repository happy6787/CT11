#permanant store of data (unless delete),update share read files 

### File read operation

# Goto file path/folder, locate file with name 
# Open file
# Read content/write from/to file       
# save in case of write 
# print/copy content 
# Close 

############################################################################################

# file=open("D:/SUCCESS/ACADEMICS/CREDENCE TESTING/SAGAR/CT11_FILE.TXT",'r')
# filecontent=file.read()
# print(filecontent)
# file.close()   

##################################################################################################

# try:
#     filePath = "D:/SUCCESS/ACADEMICS/CREDENCE TESTING/SAGAR/CT11_FILE.txt"
#     ##filePath = "D:/SUCCESS/ACADEMICS/CREDENCE TESTING/SAGAR/CT11_FILE.TXT"

#     fileVariable = open(filePath)      # Opening file
#     content = fileVariable.read()         # read file content
#     print("File content  : ", content)      # printing content from file
# except FileNotFoundError as e:
#     print(f"File not found : {filePath}", e)
# except Exception as e:
#     print("Something went wrong...", e)

# finally:
#     try:
#         fileVariable.close()        # Closing file
#     except:
#         print("File never been opened")

#############################################################################################

# when we open a file using with statement there is no need to close the file explicitly


# file="D:/SUCCESS/ACADEMICS/CREDENCE TESTING/SAGAR/CT11_FILE.TXT"
# with open(file,'r') as filevariable:
#     isReadable=filevariable.readable()
#     if isReadable:
#         filecontent=filevariable.read()
#         print(filecontent)  #### file will be automatically get closed once this "with" block gets executed
#     else:
#         print('file is not readable')

#############################################################################################

# write >>> open for writing, creates a new file if it does not exist or truncates the file if it exists.

# NEW FILE >>> USING W

# newfile=open('new file using w.txt', 'w')
# content=newfile.write("Happy is a good boy")
# newfile.close()

#################################################

# NEW FILE >>> WRITE >>> REOPEN USING W

# newfile=open('new file using w.txt', 'w+')
# content=newfile.write("Happy is a good boy")
# newfile=open("new file using w.txt",'r')
# filecontent=newfile.read()
# print(filecontent) 
# newfile.close()

#################################################

#OPEN>>>WRITE>>>OPEN USING W

# file="D:/SUCCESS/ACADEMICS/CREDENCE TESTING/SAGAR/CT11/OPEN WRITE OPEN USING W.TXT"
# filecontent='Happy is very Smart'
# with open(file,'w') as filevariable:  
#         temp=filevariable.write(filecontent)
#         print(temp)     
# file1=open(file,'r')
# fileread=file1.read()
# print(fileread)
# file1.close()   

#################################################

# TRUNCATE

# file="D:/SUCCESS/ACADEMICS/CREDENCE TESTING/SAGAR/CT11_FILE.TXT"
# filecontent='update file new content'
# with open(file,'w') as filevariable:  
#         temp=filevariable.write(filecontent)
#         print(temp)  
#         print(filecontent)

#################################################

#x - Opens a file for exclusive creation. If the file already exists, the operation fails.

#new file

# newfile=open('new file using x.txt', 'x')
# newfile.close()

#file if already exist

# newfile=open('new file using x.txt', 'x')
# newfile.close()   ### FileExistsError: [Errno 17] File exists: 'new file using x.txt'

#################################################

#a – Opens a file for appending at the end of the file without truncating it. 
                        #Creates a new file if it does not exist.


# f=open('new file using a','a')
# f.write("\nAbhinav is also good boy")
# f.close()

#################################################

#r+ read and write

# f=open('existing file using r+.txt','r+')
# data=f.read()
# f.write("\nAbhinav is also good boy")
# print(data)
# f.close()

#################################################

#w+ write and read. overwwrite existing data

# f=open('existing file using w+.txt','w+')
# f.write("har har mahadev")
# data=f.read()
# print(data)   #### as in case of write mode the cursor will be at the end of the string so we will not get be albe to read the file
# f.close()

# #################################################

# # seek

# f=open('existing file using w+.txt','w+')
# f.write("har har mahadev")
# f.seek(0)    #### as we have applied function we command program to grt the cursor at 0 index so that we can read the file
# data=f.read()
# print(data)  
# f.close()

#################################################
#a+ append and then read

# f=open('existing file using a+.txt','a+')
# f.write("har har shanbhu")
# f.seek(0)
# data=f.read()
# print(data)  
# f.close()










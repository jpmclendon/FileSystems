import os
import os.path

chunk = 50
smallfile = None
smallno = 0
#Hard Coded for testing purposes, needs to be changed for offical product
OriginalStorage = 'C:/Users/jpmcl/Desktop/Chunk/'
fat = open(OriginalStorage + 'fat_table.txt', 'w')
fat.write('File' + '\t' + '\t' + 'Node #' + '\n')
fat.close()
while True:
    option = input("Enter command: \n printfat \n add <Filename> with filetype(.txt) \n delete <Filename> without filetype \n exit \n")
#shows current fat table in compressed form for python
    if option == "printfat":
        fat = open(OriginalStorage +'fat_table.txt', 'r')
        showfat = fat.readlines()
        print(showfat)
#exits the program
    elif option == "exit":
        exit()
#for add and delete options, it requires two arguments
    else:
        option = option.split()
        if(len(option) > 2):
            print('Too many words, please choose from the designated list(Make sure filename is one word')
        elif option[0] == 'add':
            if os.path.exists(option[1]):
                fat = open(OriginalStorage + 'fat_table.txt', 'a+')
                fileName = option[1]
                with open(OriginalStorage + fileName) as bigfile:
                    for lineno, line in enumerate(bigfile):
                        if lineno % chunk == 0:
                            if smallfile:
                                smallfile.close()
                            smallno +=1
                            small_filename = fileName + '_B{}.txt'.format(smallno)
                            smallfile = open(OriginalStorage + small_filename, "w")
                            smallfile.write(line)
                            fat.write(option[1] +'\t' + f'N{smallno}\n')
                        if smallfile:
                            smallfile.close()
                    fat.close()
            else:
                print("File Not Found")
            
        elif option[0] == 'delete':
            if os.path.exists(option[1]):
                file_to_delete = option[1]
                for filename in os.listdir(OriginalStorage):
                    if filename.startswith(file_to_delete):
                        os.remove(filename)
                fat = open(OriginalStorage + 'fat_table.txt', 'r')
                fatLines = fat.readlines()
                fat.close()
                fat = open(OriginalStorage + 'fat_table.txt', 'w')
                for line in fatLines:
                    if file_to_delete not in line:
                        fat.write(line)
            else:
                print("File not Found")

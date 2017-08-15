#meant to add quotation marks to words in a list
def file_parse():
    #Acquire desired file to open.
    text_dir = input("Please type directory of the file you want to convert: ")
    #open file for reading and appending.
    f_o = open(text_dir, 'r')
    
    for line in f_o:
        if "\n" in line:
            #Replace all new lines.
            replaced = line.replace("\n", ' ')
        #Pass file content to formatting_function
        formatted = formatting_function(replaced)
        #Display for user
        print(formatted)
        
    #Parsing complete, close file. 
    f_o.close()
    
#Actual formatting takes place here    
def formatting_function(q_word):
    end_result = '"'+q_word+'",'

    #Return result so we may print it in file_parse
    return end_result

file_parse()


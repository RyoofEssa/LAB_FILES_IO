# LAB_FILES_IO

## Using what you learned about Python File I/O , we want to make a progeram called To-Do List , 
# this program should do the following:

'''- Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
- If the user answers yes , then ask the user to type in his new To-Do item .
Then save that To-Do item inside the a file to_do.txt on a new line.'''

'''- If the user answers no, then ask the user : do you want to list your To-Do items ? 
 - If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item 
per line.'''

'''- Then return again to ther first question and ask again, you coninue this untill the user 
types in "exit" , then you exit the program.
and print to the user "thank you for using the To-Do program, come back again soon"'''


yes,no='y','n'
exit='exit'
while True:
    user_answer=(input(f"do you want to add a new To-Do item? answer by {yes} for yes and {no} for n:"))
    file = open("To-Do List.txt", "a+", encoding="utf-8")

    if user_answer == yes:
        user_write_list=(input("Please write your new To-Do item:"))
        file.write(user_write_list+"\n")
        continue
    elif user_answer == no:
        user_ask_to_print_list=(input("do you want to list your To-Do items? answer by yes or no:"))
        if user_ask_to_print_list == yes:
            file.seek(0)
            content=file.read()
            for line in content:
                print(content) 
                break 
    elif user_answer.lower() == "exit":
        break
print("thank you for using the To-Do program, come back again soon")
file.close()





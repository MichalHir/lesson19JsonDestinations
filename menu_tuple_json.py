my_contacts = [("ran", "05055555", 44)]
import json


FILE_NAME = 'menu.json'

import os


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def add_contact(my_arr, name, phone,age):  # adds contacts
    new_contact =(name, phone,age)
    my_arr.append(new_contact)
    clear_terminal()
    print("the contact has been added\n")
    list_contact(my_arr)


def edit_contact(my_arr):  # edits contacts
    list_contact(my_arr)
    delete_contact(my_arr)
    contact_name = input("please enter name of new contact:\n")
    contact_phone = input("please enter phone of new contact:\n")
    contact_age = input("please enter age of new contact:\n")
    add_contact(my_arr,contact_name,contact_phone,contact_age)
    clear_terminal()
    print("the contact has been edited\n")
    list_contact(my_arr)


def delete_contact(my_arr):  # deletes contacts
    list_contact(my_arr)
    # contact = input("Please enter name of contact\n")
    index_of_contact = simple_search(my_arr)
    while index_of_contact == -1:
        contact = input(
            "The name is not valid,Please enter another name or enter 7 to return to menu\n"
        )
        if contact == "7":
            menu()
            break
        index_of_contact = simple_search(my_arr)
    my_arr.remove(my_arr[index_of_contact])
    clear_terminal()
    print("the contact has been deleted\n")
    list_contact(my_arr)


def list_contact(my_arr):  # prints contacts
    clear_terminal()
    if my_arr == []:
        print("there no contacts to display")
    # my_arr.sort()
    for index, item in enumerate(my_arr):
        print(index, item[0], item[1],item[2])


def simple_search(my_arr):  # searches for full contact name
    index_of = -1
    contact_name = input("please enter name of contact:\n")
    for index, item in enumerate(my_arr):
        # if contact_name.lower()==item.lower()
        if contact_name.lower() == item[0].lower(): 
            index_of = index
            # print(index, item) - used for testing
    return index_of


def search_part_word(my_arr):  # search for contacts that contain the expression
    # casefold()	Converts string into lower case
    # lower()	Converts a string into lower case
    # find()	Searches the string for a specified value and returns the position of where it was found
    index_of = -1
    if_contains = False
    clear_terminal()
    contact_search = input("please enter what you are searching:\n")
    for index, item in enumerate(my_arr):
        if (contact_search.lower() in item[0].lower()  
            or contact_search.lower() in item[1].lower()  
            or contact_search.lower() in item[2]): 
            if_contains = True
            index_of = index
            print(index, item)
    if if_contains == False:
        print("no search results\n")


# def add_contact_fav(my_arr, my_arr_fav): # adds contact to favorites (adds * before the name)
def add_contact_fav(my_arr):
    list_contact(my_arr)
    # contact = input("Please enter name of contact\n")
    index_of_contact = simple_search(my_arr)
    while index_of_contact == -1:
        contact = input(
            "The name is not valid,Please enter another name or enter 7 to return to menu\n"
        )
        if contact == "7":
            menu()
            clear_terminal()
            break
        index_of_contact = simple_search(my_arr)
    # add_contact(my_arr_fav, contact) - used for testing
    original_tuple = my_arr[index_of_contact]
    new_tuple = ("*" + original_tuple[0], original_tuple[1],original_tuple[2])
    my_arr[index_of_contact] = new_tuple
    # my_arr[index_of_contact][0] = "*" + my_arr[index_of_contact][0]
    clear_terminal()
    print("the contact has been added to favorites\n")
    list_contact(my_arr)


def list_contact_fav(my_arr):  # prints favorites
    clear_terminal()
    # my_arr.sort()
    if_fav = False
    count = 0
    for index, item in enumerate(my_arr):
        if_fav = item[0].startswith("*")
        if  if_fav == True:
            count += 1
            print(index, item[0], item[1],item[2])
            if_fav = False
    if count == 0:
        print("there are no favorites")


def search_part_word_fav(my_arr,): # search for favorite contacts that contain the expression
    # casefold()	Converts string into lower case
    # lower()	Converts a string into lower case
    # find()	Searches the string for a specified value and returns the position of where it was found
    index_of = -1
    if_contains = False
    clear_terminal()
    contact_search = input("please enter name of new contact:\n")
    if_fav = False
    for index, item in enumerate(my_arr):
        if_fav = item[0].startswith("*")
        # if (item.lower()).find(contact.lower()) >= 0 and if_fav == True:
        if (contact_search.lower() in item[0].lower()  
            or contact_search.lower() in item[1].lower()  
            or contact_search.lower() in item[2]) and if_fav == True:
            if_fav = False
            if_contains = True
            index_of = index
            print(index, item)
    if if_contains == False:
        print("no search results\n")
def load():
    global my_contacts
    try:
        with open(FILE_NAME, 'r') as f:
            my_contacts = json.load(f)
    except:
        print("no file found. continuing..")
        my_contacts = []

def save():
    with open(FILE_NAME, 'w') as f:   # f=open()
        json.dump(my_contacts, f)

def menu():  # menu
    load()
    while True:
        print("1 - Add Contact")
        print("2 - Edit Contact")
        print("3 - Delete Contact")
        print("4 - List of all contacts")
        print("5 - Search")
        print("6 - Add to favorites")
        print("7 - List favorites")
        print("8 - Search favorites")
        print("9 - clear terminal")
        print("10 - Exit")
        selection = input("please enter command:\n")
        if selection == "1":
            new_contact_name = input("please enter name of new contact:\n")
            new_contact_phone = input("please enter phone of new contact:\n")
            new_contact_age = input("please enter age of new contact:\n")
            add_contact(my_contacts,new_contact_name,new_contact_phone,new_contact_age)
        if selection == "2":
            edit_contact(my_contacts)
        if selection == "3":
            delete_contact(my_contacts)
        if selection == "4":
            list_contact(my_contacts)
        if selection == "5":
            search_part_word(my_contacts)
        if selection == "6":
            # add_contact_fav(my_contacts, my_contacts_fav) - used for testing
            add_contact_fav(my_contacts)
        if selection == "7":
            # list_contact(my_contacts_fav) - used for testing
            list_contact_fav(my_contacts)
        if selection == "8":
            search_part_word_fav(my_contacts)
        if selection == "9":
            clear_terminal()
            # print("the terminal has been cleared")
        if selection == "10":
            print("Goodbye")
            save()
            break


menu()

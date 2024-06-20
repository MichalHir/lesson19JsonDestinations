# My destination - name, description,grade save to jason , do search ability
import json


FILE_NAME = "destinations.json"
my_destinations = [
    {"name": "Argentina", "description": "Argentina", "grade": 8.5},
    {"name": "London", "description": "London", "grade": 9},
    {"name": "New York", "description": "Ney York", "grade": 7},
]


import os


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def add_destination(my_arr, name, description, grade):  # adds destinations
    new_destination = dict(name=name, description=description, grade=grade)
    my_arr.append(new_destination)
    clear_terminal()
    print("the destination has been added\n")
    list_destination(my_arr)


def edit_destination(my_arr):  # edits destinations
    list_destination(my_arr)
    index_edit = simple_search(my_arr)
    while index_edit==-1:
        print("the destination's name doesn't exist\n")
        index_edit = simple_search(my_arr)
    destination_name = input("please enter new name of destination:\n")
    destination_description = input("please enter new description of destination:\n")
    destination_grade = input("please enter new grade of destination:\n")
    my_arr[index_edit] = {
        "name": destination_name,
        "description": destination_description,
        "grade": destination_grade,
    }
    clear_terminal()
    print("the destination has been edited\n")
    list_destination(my_arr)


def delete_destination(my_arr):  # deletes destinations
    list_destination(my_arr)
    index_of_destination = simple_search(my_arr)
    while index_of_destination == -1:
        destination = input(
            "The name is not valid,Please enter another name or enter 7 to return to menu\n"
        )
        if destination == "7":
            menu()
            break
        index_of_destination = simple_search(my_arr)
    my_arr.remove(my_arr[index_of_destination])
    clear_terminal()
    print("the destination has been deleted\n")
    list_destination(my_arr)


def list_destination(my_arr):  # prints destinations
    clear_terminal()
    if my_arr == []:
        print("there no destinations to display")
    for index, item in enumerate(my_arr):
        print(index, item["name"], item["description"], item["grade"])


def simple_search(my_arr):  # searches for full destination name
    index_of = -1
    destination_name = input("please enter name of destination:\n")
    for index, item in enumerate(my_arr):
        if destination_name.lower() == item["name"].lower():
            index_of = index
    return index_of


def search_part_word(my_arr):  # search for destinations that contain the expression
    index_of = -1
    if_contains = False
    clear_terminal()
    destination_search = input("please enter what you are searching:\n")
    for index, item in enumerate(my_arr):
        if (
            destination_search.lower() in item["name"].lower()
            or destination_search.lower() in item["description"].lower()
            or destination_search in str(item["grade"])
        ):
            if_contains = True
            index_of = index
            print(index, item["name"], item["description"], item["grade"])
    if if_contains == False:
        print("no search results\n")


def add_destination_fav(
    my_arr,
):  # adds destination to favorites (adds * before the name)
    list_destination(my_arr)
    index_of_destination = simple_search(my_arr)
    while index_of_destination == -1:
        destination = input(
            "The name is not valid,Please enter another name or enter 7 to return to menu\n"
        )
        if destination == "7":
            menu()
            clear_terminal()
            break
        index_of_destination = simple_search(my_arr)
    my_arr[index_of_destination]["name"] = "*" + my_arr[index_of_destination]["name"]
    clear_terminal()
    print("the destination has been added to favorites\n")
    list_destination(my_arr)


def list_destination_fav(my_arr):  # prints favorites
    clear_terminal()
    if_fav = False
    count = 0
    for index, item in enumerate(my_arr):
        if_fav = item["name"].startswith("*")
        if if_fav == True:
            count += 1
            print(index, item["name"], item["description"], item["grade"])
            if_fav = False
    if count == 0:
        print("there are no favorites")


def search_part_word_fav(
    my_arr,
):  # search for favorite destinations that contain the expression
    index_of = -1
    if_contains = False
    clear_terminal()
    destination_search = input("please enter name of new destination:\n")
    if_fav = False
    for index, item in enumerate(my_arr):
        if_fav = item["name"].startswith("*")
        if (
            destination_search.lower() in item["name"].lower()
            or destination_search.lower() in item["description"].lower()
            or destination_search in str(item["grade"])
        ) and if_fav == True:
            if_fav = False
            if_contains = True
            index_of = index
            print(index, item["name"], item["description"], item["grade"])
    if if_contains == False:
        print("no search results\n")


def load():
    global my_contacts
    try:
        with open(FILE_NAME, "r") as f:
            my_destinations = json.load(f)
    except:
        print("no file found. continuing..")
        my_destinations = []


def save():
    with open(FILE_NAME, "w") as f:  # f=open()
        json.dump(my_destinations, f)


def menu():  # menu
    load()
    while True:
        print("1 - Add destination")
        print("2 - Edit destination")
        print("3 - Delete destination")
        print("4 - List of all destinations")
        print("5 - Search")
        print("6 - Add to favorites")
        print("7 - List favorites")
        print("8 - Search favorites")
        print("9 - clear terminal")
        print("10 - Exit")
        selection = input("please enter command:\n")
        if selection == "1":
            new_destination_name = input("please enter name of new destination:\n")
            new_destination_description = input(
                "please enter description of new destination:\n"
            )
            new_destination_grade = input("please enter grade of new destination:\n")
            add_destination(
                my_destinations,
                new_destination_name,
                new_destination_description,
                new_destination_grade,
            )
        if selection == "2":
            edit_destination(my_destinations)
        if selection == "3":
            delete_destination(my_destinations)
        if selection == "4":
            list_destination(my_destinations)
        if selection == "5":
            search_part_word(my_destinations)
        if selection == "6":
            add_destination_fav(my_destinations)
        if selection == "7":
            list_destination_fav(my_destinations)
        if selection == "8":
            search_part_word_fav(my_destinations)
        if selection == "9":
            clear_terminal()
        if selection == "10":
            print("Goodbye")
            save()
            break


menu()

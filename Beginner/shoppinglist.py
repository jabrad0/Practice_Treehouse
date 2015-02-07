

shoppinglist = []

def show_help():
    print("******* SHOPPING LIST CREATOR ******* ")
    print("Enter DONE when done.")
    print("Enter HELP for this help.")
    print("Enter SHOW to see current list.")
    print("Enter MOVE to move an item.")
    print("Enter REMOVE to remove an item from the list")
    print("Enter CLEAR to start over.")
    print("*************************************")
    print("What should we pick up?")

def remove_item(idx):
    index = idx - 1
    item = shoppinglist.pop(index)
    print("Remove {}.".format(item))

def move_item(idx, new_idx):
    index = idx - 1
    new_index = new_idx - 1
    movethisitem = shoppinglist.pop(index)
    shoppinglist.insert(new_index, movethisitem)
    print("Moved {} to #{}".format(movethisitem, new_idx))


def add_to_list(item):
    shoppinglist.append(item)
    if (len(shoppinglist)) == 1:
        print("Added! List has {} item.".format(len(shoppinglist)))
    else:
        print("Added! List has {} items.".format(len(shoppinglist)))

def show_list():
    count = 1
    for item in shoppinglist:
        print("{}: {}".format(count, item))
        count += 1

def do_not_add():
    print("I think that was a mistake...")

def clear_list():
    del shoppinglist[:]
    print("Your shopping list is now empty!")

show_help()   

while True:
    new_item = raw_input("> ")
    if new_item == "":
        do_not_add()
        continue
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    elif new_item == "REMOVE":
        show_list()
        idx = raw_input("Which item? Tell me the number. ")
        remove_item(int(idx))
        continue
    elif new_item == "CLEAR":
        clear_list()
        continue
    elif new_item == "MOVE":
        show_list()
        idx = raw_input("Move what item? Tell me the number ")
        new_idx = raw_input("Tell me the number where you want this item? ")
        move_item(int(idx), int(new_idx))
        continue

    add_to_list(new_item)
    continue

show_list()
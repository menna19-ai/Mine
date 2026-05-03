names=[]
def add_names():
    while True:
        name = input("Enter names or done: ").strip()
        if name == "":
            print("Please enter a name!")
            continue
        if name.lower() == "done":
            break
        names.append(name)
def data_cleaning():
    clean_names = list(set(n.strip().capitalize() for n in names))
    return clean_names
def show_names(clean_names):
    if len(clean_names)==0:
        print("There is no names to display!")
        return
    for name in clean_names:
        print(name,end=" ")
def search_name(clean_names,name):
    if len(clean_names)==0:
        print("There is no names!")
        return
    if name.capitalize() in clean_names:
        print("Name exists")
    else:
        print("Name does not exist")
def delete_name(clean_names,name):
    if len(clean_names)==0:
        print("There is no names!")
        return
    name = name.capitalize()
    if name in clean_names:
        clean_names.remove(name)
        print("Name deleted")
    else:
        print("Name does not exist")
def show_analysis(clean_names):
    if len(clean_names) == 0:
        print("There is no names!")
        return
    print(f"Total number of names is: {len(clean_names)}")
    longest = clean_names[0]
    shortest = clean_names[0]
    total_length = 0
    for nme in clean_names:
        if len(nme) > len(longest):
            longest = nme
        if len(nme) < len(shortest):
            shortest = nme
        total_length += len(nme)
    avg = total_length / len(clean_names)
    print("Longest name is:", longest)
    print("Shortest name is:", shortest)
    print("Average name length:", round(avg, 2))
def filter_names(clean_names):
    if not clean_names:
        print("No names!")
        return
    min_len = int(input("Min length: "))
    start = input("Start letter (optional): ").capitalize()
    for name in clean_names:
        if len(name) < min_len:
            continue
        if start and name[0] != start:
            continue
        print(name)
def main():
    add_names()
    while True:
        print("""
1- Show Names
2- Search Name
3- Delete Name
4- Show Analysis
5- Filter Names
0- Exit
""")
        choice = input("Enter choice: ")
        clean = data_cleaning()
        if choice == "1":
            show_names(clean)
        elif choice == "2":
            name = input("Enter name to search: ")
            search_name(clean, name)
        elif choice == "3":
            name = input("Enter name to delete: ")
            delete_name(clean, name)
        elif choice == "4":
            show_analysis(clean)
        elif choice == "5":
            filter_names(clean)
        elif choice == "0":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!")
main()
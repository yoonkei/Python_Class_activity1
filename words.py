words = []

def save_words():
    global words
    print("Enter word to save. (To finish press 'Enter' key)")
    print(" ")
    while True:
        word = input("word : ")
        if len(word) == 0 :
            break
        elif word in words:
            print("Already Exist")
            continue
        words.append(str(word))

def delete_words():
    global words
    print(" ")
    print("Enter word to delte")
    print(" ")
    while True:
        word = input("Word : ")
        if word in words:

            words.remove(word)
            print("Deletion complete")
            break
        else:
            print("No Exist")
            continue

            
def print_words():
    print(" ")
    for i in words:
        print(i, sep='\n')

menu = 0

while menu != 4:
    print(" ")
    print("********************************")
    print("*          Sookmyung Dictionary            *")
    print("********************************")
    print(" ")
    print("             1. Save words")
    print("             2. Delete words")
    print("             3. Print all words")
    print("             4. Exit")
    print(" ")
    print("================================")
    menu = int(input("Select >> "))
    if menu ==1:
        save_words()
    elif menu == 2:
        delete_words()
    elif menu == 3:
        print_words()
    elif menu == 4: break
    else :
        print("You enterd wrong menu!")

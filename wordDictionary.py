dictionary = { }

def save_words(dictionary):
    print("Enter word to save. Press 'Enter' to finish")
    print(" ")
    while True:
        word = input("Word :")
        if len(word) == 0 :
            break
        elif word in dictionary:
            print("Already Exist")
            continue
        mean = input("Mean : ")
        dictionary[word] = mean

def delete_words(dictionary):
    print(" ")
    print("Enter word to delte")
    print(" ")
    while True:
        word = input("Word :")
        if word in dictionary:
            del dictionary[word]
            print("Deletion is completed")
            break
        else:
            print("No such words")
            continue

def print_words(dictionary):
    print(" ")
    for word in dictionary:
        print(word, '\t', dictionary[word])

def search_words(dictionary):
    print("Enter word to search")
    print(" ")
    word = input("Word : ")
    if word in dictionary:
        print(word, '\t', dictionary[word])
    else:
        print(word,"is not found")

def word_test(dictionary):
    win = 0 
    for i in dictionary:
        user_input = input(f"{i} : ")
        if user_input == dictionary[i]:
            print("Correct!")
            print(" ")
            win += 1
        else:
            print("Wrong...")
            print(" ")
    print("You got {} answers".format(win))
    global scores
    score = win
    scores.append(score)

def test_score(dictionary):
    print("      ScoreBord        ")
    print("================")
    rank = 1
    scores.sort(reverse = True)
    for score in scores:
        print("{} rank   {} answers".format(rank, score))
        rank += 1

win = 0    
scores = []


choice = 0
menu = 0

while menu != 7:
    
    print(" ")
    print("********************************")
    print("*          Sookmyung Dictionary            *")
    print("********************************")
    print(" ")
    print("             1. Save words")
    print("             2. Delete words")
    print("             3. Print all words")
    print("             4. Search word")
    print("             5. Word Test")
    print("             6. Show Test score")
    print("             7. Exit")
    print(" ")
    print("================================")
    menu = int(input("Select >> "))
    if menu ==1:
        save_words(dictionary)
    elif menu == 2:
        delete_words(dictionary)
    elif menu == 3:
        print_words(dictionary)
    elif menu == 4:
        search_words(dictionary)
    elif menu == 5:
        word_test(dictionary)
    elif menu == 6:
        test_score(dictionary)
    elif menu == 7:
        print("Thanks for using dictionary")
        break
    else :
        print("You enterd wrong menu!")

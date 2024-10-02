def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    count_words(file_contents)
    count_characters(file_contents)

def count_words(file_contents): #takes in a str
    words = file_contents.split() #using .split() to split a string on whitespace into a list
    count = 0
    for word in words:
        count += 1
    print(count)

def count_characters(file_contents): #takes in a str
    characters = {} #Using a dictionary where String -> Integer (Key -> Value, aka Key:Value pair)
    lowered_string = file_contents.lower() #Using .lower() to convert str to lowercase. Easier to parce through for dictionary
    for i in lowered_string: #loop through the string character by character
        if i not in characters:
            characters[i] = 1
        else:
            characters[i] += 1
    print(characters)

main()

def main():
    with open("books/frankenstein.txt") as f:
        text = f.read() #string
    words = count_words(text) #integer

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print()
    count_characters(text) #printing dictionary of character count
    print("--- End report ---")

    

def count_words(text): #takes in a str
    words = text.split() #using .split() to split a string on whitespace into a list
    count = 0
    for word in words:
        count += 1
    return count

def count_characters(text): #takes in a str
    chars = {} #Using a dictionary where String -> Integer (Key -> Value, aka Key:Value pair)
    for c in text: #loop through the string
        lowered = c.lower()
        if lowered not in chars: #initialize a Value if this is the first time looping through a specific character in string
            chars[lowered] = 1
        else:
            chars[lowered] += 1
    
    #Now to print the count of each character
    for i in chars:
        print(f"The '{i}' character was found {chars[i]} times")

main()

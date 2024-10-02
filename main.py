def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    count_words(file_contents)

def count_words(file_contents):
    #using .split() to split a string on whitespace
    words = file_contents.split()
    
    count = 0
    for word in words:
        count += 1
    
    print(count)

main()

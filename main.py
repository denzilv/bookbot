
def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        words = file_contents.split()

    dict = {}

    for word in words:
        for letter in word.lower():
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1
    
    dictlist = []

    for key, value in dict.items():
        if key.isalpha():
            temp = {"letter": key, "count": value}
            dictlist.append(temp)

    def sort_on(dict):
        return dict["count"]

    dictlist.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(len(words), "words found in the document\n")
    for each in dictlist:
        print(f'The \'{each['letter']}\' character was found {each['count']} times')
    print("--- End report ---")

main()

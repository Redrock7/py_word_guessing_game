word = input("Please type in the word: ")
print('The length of the word is', len(word))
missing_word = list(len(word)*'*')
tries = len(word)

letters = [chr(i) for i in range(ord('а'), ord('Z')+1)]
while missing_word != list(word) and tries > 0:
    print(''.join(missing_word))
    print('Insert a letter: ')
    attempt = input()[0]

    if attempt in letters or not attempt.isalpha():
        print('The input is not accepted, try again')
        continue

    if attempt in word:
        for i in range(len(word)):
            if attempt == word[i]:
                missing_word[i] = attempt
    else:
        tries -= 1
        print('The letter "', attempt, '" does not match, number of tries left is ', tries, '. Try again...')


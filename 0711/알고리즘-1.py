word = input().upper()

alphabets = {}

for letter in word:
    if letter in alphabets:
        alphabets[letter] += 1
    else:
        alphabets[letter] = 1

# alphabets.items가 return해 주는 것? ex) [("A":1),('B':2)] 이런 형태
alphabets = sorted(alphabets.items(), key=(lambda x: x[1]), reverse=True)

if len(word)>1 and alphabets[0][1] == alphabets[1][1]:
    print("?")
else:
    print(alphabets[0][0])
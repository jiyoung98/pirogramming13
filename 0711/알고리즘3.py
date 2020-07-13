count = int(input())

def check_group(word):
    last_alphabet = ""
    alphabets = []

    for letter in word:
        if letter == last_alphabet:
            continue
        else:
            if letter in alphabets:
                return False

            alphabets.append(letter)
            last_alphabet = letter
    return True

for _ in range(count): # for in 문에서, list에 해당하는 아이템값이 주어지는데 이를 안 쓰겠다고 처리하기 위해 i대신 _를 사용
    word =input()

    if check_group(word):
        result += 1

print(result)
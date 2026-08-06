#vowel_count.py
word = str("Programming is something I'm relearning so I must be paitient with myself")
v_count = 0
c_count = 0
vowels = ['a','e','i','o','u','y']

for letter in word:
    #print(letter)
    #print("----------")
    for vowel in vowels:
        #print(f"-{vowel}-")
        if letter == vowel:
            #print(f"{vowel} = {letter}")
            print(letter)
            v_count += 1
        else:
            #print(letter)
            c_count += 1
print(f"Vowel Count: {v_count}")
print(f"Constanant Count: {c_count}")
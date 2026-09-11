str = "JSS University csds 1"
uppercase = 0
lowercase = 0 
digit = 0
space = 0
vowel = 0
constant = 0
for ch in str:
    if ch.isupper():
        uppercase+=1
    if ch.islower():
        lowercase+=1
    if ch.isdigit():
        digits+=1
    if ch.isspace():
        spaces+=1
    if ch.isvowel():
        vowel+=1
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels+=1
        else:
            consonants+=1

        print("uppercase is",uppercase)
        print("lowercase is",lowercase)
        print("digits is",digits)
        print("spaces is",spaces)
        print("vowels is",vowels)
        print("constants is",constants)


    
    
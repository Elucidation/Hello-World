from random import choice

consonents = "bcdfghjklmnpqrstvwxyz" # includes y
vowels = "aeiou" # not including y

def randShortName():
    " Returns 3 letter word w/ consonent+vowel+consonent format"
    return (choice(consonents)+ choice(vowels) + choice(consonents)).capitalize()

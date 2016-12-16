__author__ = 'jc449767'


vowels = ['a','e','i','o','u']

vowel_count = 0

name = input("enter your name:")

for c in name:
    if c.lower() in vowels:
     vowel_count += 1


#print(vowel_count)

print('out of {} 16 letters, {} has 4 vowels'.format(len(name), name, vowel_count))
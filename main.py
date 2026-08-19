user = input('Enter your word here:')
if user == user[::-1]:
    print('Pallindrome.')
else:
    print('not a pallindrome.')
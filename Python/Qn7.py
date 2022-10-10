email = str(input('Enter your email id: '))
count = 0
l=len(email)

if email[0].isalpha() and email[l-1].isalpha() is True:

    if ('@') in email and (email.count('@')==1) is True:

           if ('.') in email and (email.count('.') == 1) is True:
             print('Email is valid')
           else:
             print('The email address you entered is not valid.')
    else:
        print('The email address you entered is not valid.')
else:
    print('Enter a valid email id')


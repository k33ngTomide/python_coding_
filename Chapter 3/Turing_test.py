problem = input('What is your problem? : ')

quiz = input('Have you have this problem before (yes or no)? : ')

if quiz == 'yes' or quiz == 'Yes' or quiz == 'YES':
    print('Well, you have it again')
elif quiz == 'no' or quiz == 'No' or quiz == 'NO':
    print('Well, you have it now')

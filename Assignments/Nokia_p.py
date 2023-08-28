print('''Menu List
        1. Phone book
        2. Messages
        3. Chat
        4. Call register
        5. Tones
        6. Settings
        7. Call divert
        8. Games
        9. Calculator
        10. Remainders
        11. Clock
        12. Profiles
        13. SIM services''')
user_entry = int(input("Menu list: "))

if user_entry == 1:
    print('''Phone book
    1. Services
    2. Service Nos.
    3. Add name
    4. Erase
    5. Edit
    6. Assign tone
    7. Send b"card
    8. Options
    9. Speed dials
    10. Voice tags''')
    user_entry_2 = int(input())

    if user_entry_2 == 8:
        print('''Options
        1. Types of view
        2. Memory status''')
    if user_entry_2 > 10 or user_entry_2 < 0:
        print("Invalid entry, try again")
        exit()

elif user_entry == 2:
    print('''Messages
    1. Write Messages
    2. Inbox 
    3. Outbox
    4. Picture Messages
    5. Templates
    6. Smileys
    7. Message Settings
    8. Info service 
    9. Voice mailbox number
    10. Services command editor''')
    user_entry_3 = int(input())

    if user_entry_3 == 7:
        print('''Message Settings
        1. Set 1
        2. Common''')
        user_entry_4 = int(input())
        if user_entry_4 == 1:
            print('''Set 1
            1. Message center number
            2. Message sent as 
            3. Message validity''')
        elif user_entry_4 == 2:
            print('''Common
            1. Delivery reports
            2. reply via same centre
            3. Character support''')
        elif user_entry_3 < 0 or user_entry_3 > 10:
            print('invalid entry, try again')
            exit()

elif user_entry == 3:
    print("Chat")
elif user_entry == 4:
    print('''Call register
    1. Missed calls
    2. Received calls 
    3. Dialled numbers
    4. Erase recent call lists
    5. Show call duration
    6. Show call costs
    7. Call cost settings
    8. Prepaid credit''')
    user_entry_5 = int(input())

    if user_entry_5 == 5:
        print('''Show call duration
        1. Last call duration
        2. All calls' duration
        3. Received call's duration
        4. Dialled calls' duration
        5. Clear times''')
    elif user_entry_5 == 6:
        print('''Show call costs
        1. Last call cost
        2. All call's cost
        3. clear counters''')
    elif user_entry_5 == 7:
        print('''Call cost settings
        1. Call cost limit
        2. Show cost in''')
    elif user_entry_5 < 0 or user_entry_5 > 8:
        print('Invalid entry, try again!')
        exit()

elif user_entry == 5:
    print('''Tones
    1. Ringing Tone
    2. Ringing volume
    3. Incoming call alert
    4. Composer
    5. Message alert tone
    6. Keypad tones
    7. Warning and game tones
    8. Vibrating alert
    9. Screen saver''')

elif user_entry == 6:
    print('''Settings
    1. Call settings
    2. Phone settings
    3. Security settings
    4. Restore factory settings''')
    user_entry_6 = int(input())

    if user_entry_6 == 1:
        print('''Call Settings
        1. Automatic redial 
        2. Speed dialing
        3. Call waiting 
        4. Own number sending
        5. Phone line in use
        6. Automatic answer''')
    elif user_entry_6 == 2:
        print('''Phone Settings
        1. Language 
        2. Cel info display
        3. Welcome note
        4. Network selection
        5. Lights
        6. Confirm SIM service actions''')
    elif user_entry_6 == 3:
        print('''Security Settings
        1. PIN code request
        2. Call barring service
        3. Fixed dialing
        4. Closed user group
        5. Phone security
        6. Change access codes''')
    elif user_entry_6 < 0 or user_entry_6 > 4:
        print('Invalid entry, try again!')
        exit()

elif user_entry == 7:
    print("Call divert")

elif user_entry == 8:
    print("Games")

elif user_entry == 9:
    print("Calculator")

elif user_entry == 10:
    print("Reminders")

elif user_entry == 11:
    print('''Clock
    1. Alarm clock
    2. Clock Settings
    3. Date settings
    4. Stop Watch
    5. Countdown timer
    6. Auto update of date and time''')
else:
    print("Invalid Input")

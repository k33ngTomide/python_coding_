def main_menu():
    print('''___Menu List___
            1. Phone book
            2. Messages
            3. Chat
            4. Call register
            5.Tones
            6. Settings
            7. Call divert
            8. Games
            9. Calculator
            10. Remainders
            11. Clock
            12. Profiles
            13. SIM services
            0. Off''')
    user_entry = input("Enter Menu List:  ")
    if user_entry == "1":
        phone_book()
    elif user_entry == "2":
        messages()
    elif user_entry == "3":
        chat()
    elif user_entry == "4":
        call_register()
    elif user_entry == "5":
        tones()
    elif user_entry == "6":
        settings()
    elif user_entry == "7":
        call_divert()
    elif user_entry == "8":
        games()
    elif user_entry == "9":
        calculator()
    elif user_entry == "10":
        remainder()
    elif user_entry == "11":
        clock()
    elif user_entry == "12":
        profile()
    elif user_entry == "13":
        sim_services()
    elif user_entry == "0":
        off()
    else:
        invalid()


def off():
    exit()


def call_divert():
    print('''___Call divert___
            0. Back''')
    user_entry_15 = input('Enter:  ')
    if user_entry_15 == "0":
        main_menu()
    else:
        print("Invalid Entry")
        call_divert()


def games():
    print('''___Games___
            0. Back''')
    user_entry_16 = input('Enter:  ')
    if user_entry_16 == "0":
        main_menu()
    else:
        print("Invalid entry")
        games()


def profile():
    print('''___Profile___
            0. Back''')
    user_entry_19 = input('Enter:  ')
    if user_entry_19 == "0":
        main_menu()
    else:
        print("Invalid Entry")
        profile()


def calculator():
    print('''___Calculator___
            0. Back''')
    user_entry_17 = input('Enter:  ')
    if user_entry_17 == "0":
        main_menu()
    else:
        print("Invalid Entry")
        calculator()

def remainder():
    print('''___Reminder___
            0. Back''')
    user_entry_18 = input('Enter:  ')
    if user_entry_18 == "0":
        main_menu()
    else:
        iprint("Invalid Entry")
        remainder()


def sim_services():
    print('''___SIM services___
                    0. Back''')
    user_entry_20 = input('Enter:  ')
    if user_entry_20 == "0":
        main_menu()
    else:
        print("Invalid Entry")
        sim_services()


def phone_book():
    print('''___Phone Book___
        1. Services
        2. Service Nos.
        3. Add name
        4. Erase
        5. Edit
        6. Assign tone
        7. Send B"card
        8. Options
        9. Speed dials
        10. Voice tags
        0. Back''')
    user_entry_2 = input("Enter: ")
    if user_entry_2 == "1":
        print('___Services___')
        back_phonebook()
    elif user_entry_2 == "3":
        print('___Add name___')
        back_phonebook()
    elif user_entry_2 == "4":
        print('___Erase___')
        back_phonebook()
    elif user_entry_2 == "5":
        print('___Edit___')
        back_phonebook()
    elif user_entry_2 == "6":
        print('___Assign tone___')
        back_phonebook()
    elif user_entry_2 == "7":
        print('___Send b"card___')
        back_phonebook()
    elif user_entry_2 == "2":
        print('___Services Nos___')
        back_phonebook()
    elif user_entry_2 == "9":
        print('___Speed dials___')
        back_phonebook()
    elif user_entry_2 == "10":
        print('___Voice tags___')
        back_phonebook()
    elif user_entry_2 == "8":
        options()
    elif user_entry_2 == "0":
        main_menu()
    else:
        print("Invalid Entry")
        phone_book()


def back_phonebook():
    print('''0. Back
    1. Main menu''')
    user_entry_cr = input('Enter:  ')
    if user_entry_cr == "0":
        phone_book()
    elif user_entry_cr == "1":
        main_menu()
    elif user_entry_cr < "0" or user_entry_cr > "1":
        print("Invalid Entry")
        back_phonebook()


def options():
    print('''___Options___
            1. Types of view
            2. Memory status
            0. Back''')
    user_entry_22 = int(input("Enter: "))
    if user_entry_22 == "1":
        print('''___Types of view___
        0. Back''')
        user_entry_20 = input("Enter: ")
        if user_entry_20 == "0":
            options()
    elif user_entry_22 == "2":
        print('''___Memory status___
        0. Back''')
        user_entry_21 = int(input("Enter: "))
        if user_entry_21 == "0":
            options()
    elif user_entry_22 == "0":
        phone_book()
    else:
        print("Invalid Entry")
        options()


def messages():
    print('''___Messages___
        1. Write Messages
        2. Inbox 
        3. Outbox
        4. Picture Messages
        5. Templates
        6. Smileys
        7. Message Settings
        8. Info service 
        9. Voice mailbox number
        10. Services command editor
        0. Back''')
    user_entry_3 = input('Enter:  ')
    if user_entry_3 == "7":
        messages_settings()
    elif user_entry_3 == "1":
        print('''___Write Messages___
        0. Back''')
        user_entry_31 = input('Enter:  ')
        if user_entry_31 == "0":
            messages()
    elif user_entry_3 == "2":
        print('''___Inbox___
        0. Back''')
        user_entry_32 = input('Enter:  ')
        if user_entry_32 == "0":
            messages()
    elif user_entry_3 == "3":
        print('''___Outbox___
        0. Back''')
        user_entry_33 = input('Enter:  ')
        if user_entry_33 == "0":
            messages()
    elif user_entry_3 == "4":
        print('''___Pictures Messages___
        0. Back''')
        user_entry_34 = input('Enter:  ')
        if user_entry_34 == "0":
            messages()
    elif user_entry_3 == "5":
        print('''___Templates___
        0. Back''')
        user_entry_35 = input('Enter:  ')
        if user_entry_35 == "0":
            messages()
    elif user_entry_3 == "6":
        print('''___Smileys___
               0. Back''')
        user_entry_36 = input('Enter:  ')
        if user_entry_36 == "0":
            massages()
    elif user_entry_3 == "8":
        print('''___Info Settings___
        0. Back''')
        user_entry_38 = input('Enter:  ')
        if user_entry_38 == "0":
            messages()
    elif user_entry_3 == "9":
        print('''___Voice Mailbox Number___
        0. Back''')
        user_entry_39 = input('Enter:  ')
        if user_entry_39 == "0":
            messages()
    elif user_entry_3 == "10":
        print('''___Services Command Editor___
        0. Back''')
        user_entry_310 = int(input('Enter:  '))
        if user_entry_310 == "0":
            messages()
    elif user_entry_3 == "0":
        main_menu()
    else:
        print("Invalid Entry")
        messages()


def messages_settings():
    print('''___Message Settings___
            1. Set 1
            2. Common
            0. Back
            99. Main menu''')
    user_entry_4 = input("Enter: ")
    if user_entry_4 == "1":
        set_1()
    elif user_entry_4 == "2":
        common()
    elif user_entry_4 == "0":
        messages()
    elif user_entry_4 == "99":
        main_menu()
    else:
        print("Invalid Entry")
        messages_settings()


def set_1():
    print('''___Set 1___
            1. Message center number
            2. Message sent as 
            3. Message validity
            0. Back''')
    user_entry_set = int(input("Enter: "))
    if user_entry_set == "0":
        messages_settings()
    elif user_entry_set == "1":
        print('''___Message center number___
                0. Back
                1. Main menu''')
        user_entry_set1 = input('Enter: ')
        if user_entry_set1 == "0":
            set_1()
        elif user_entry_set1 == "1":
            main_menu()
        else:
            print("Invalid Entry")
            set_1()
    elif user_entry_set == "2":
        print('''___Message sent as___
                0. Back
                1. Main menu''')
        user_entry_set2 = input('Enter: ')
        if user_entry_set2 == "0":
            set_1()
        elif user_entry_set2 == "1":
            main_menu()
        else:
            print("Invalid Entry")
            set_1()

    elif user_entry_set == "3":
        print('''___Message validity___
                0. Back
                1. Main menu''')
        user_entry_set3 = input('Enter: ')
        if user_entry_set3 == "0":
            set_1()
        elif user_entry_set3 == "1":
            main_menu()
        else:
            print("Invalid Entry")
            set_1()
    else:
        print("Invalid Entry")
        set_1()


def back_common():
    print('''0. Back
    1. Main menu''')
    user_entry_c = input('Enter:  ')
    if user_entry_c == "0":
        common()
    elif user_entry_c == "1":
        main_menu()
    else:
        print("Invalid Entry")
        back_common()


def common():
    print('''___Common___
            1. Delivery reports
            2. Reply via same centre
            3. Character support
            0. Back''')
    user_entry_c = input("Enter: ")
    if user_entry_c == "1":
        print('___Delivery reports___')
        back_common()
    elif user_entry_c == "2":
        print('___Reply via same centre___')
        back_common()
    elif user_entry_c == "3":
        print('___Character support___')
        back_common()
    elif user_entry_c == "0":
        messages_settings()
    else:
        print("Invalid Entry")
        common()

def chat():
    print("___Chat___"
          "\n0. Back")
    user_entry_chat = input("Enter: ")
    if user_entry_chat == "0":
        main_menu()
    else:
        print("Invalid Entry")
        chat()


def invalid():
    print('Invalid entry, try again!!!')
    main_menu()


def back_cr():
    print('''0. Back
    1. Main menu''')
    user_entry_cr = input('Enter:  ')
    if user_entry_cr == "0":
        call_register()
    elif user_entry_cr == "1":
        main_menu()
    else:
        print("Invalid Entry")
        back_cr()


def call_register():
    print('''___Call register___
        1. Missed calls
        2. Received calls 
        3. Dialled numbers
        4. Erase recent call lists
        5. Show call duration
        6. Show call costs
        7. Call cost settings
        8. Prepaid credit
        0. Back
        ''')
    user_entry_5 = input("Enter: ")
    if user_entry_5 == "1":
        print('''___Missed calls___''')
        back_cr()
    elif user_entry_5 == "3":
        print('''___Dialled numbers___''')
        back_cr()
    elif user_entry_5 == "2":
        print('''___Received calls___''')
        back_cr()
    elif user_entry_5 == "4":
        print('''___Erase recent call lists___''')
        back_cr()
    elif user_entry_5 == "6":
        show_call_cost()
    elif user_entry_5 == "8":
        print('''___Prepaid credit___''')
        back_cr()
    elif user_entry_5 == "5":
        show_call_duration()
    elif user_entry_5 == "7":
        call_cost_settings()
    else:
        print("Invalid Entry")
        call_register()


def back_scd():
    print('''0. Back
    1. Main menu''')
    user_entry_scd1 = input('Enter:  ')
    if user_entry_scd1 == "0":
        show_call_duration()
    elif user_entry_scd1 == "1":
        main_menu()
    else:
        print("Invalid Entry")
        back_scd()


def show_call_duration():
    print('''___Show call duration___
            1. Last call duration
            2. All calls' duration
            3. Received call's duration
            4. Dialled calls' duration
            5. Clear times
            0. Back''')
    user_entry_scd = input("Enter: ")
    if user_entry_scd == "0":
        call_register()
    elif user_entry_scd == "1":
        print('''___Last call duration___''')
        back_scd()
    elif user_entry_scd == "2":
        print('''___All calls' duration___''')
        back_scd()
    elif user_entry_scd == "3":
        print('''___Received call's duration___''')
        back_scd()
    elif user_entry_scd == "4":
        print('''___Dialled calls' duration___''')
        back_scd()
    elif user_entry_scd == "5":
        print('''___Clear times___''')
        back_scd()
    else:
        print("Invalid Entry")
        show_call_duration()


def back_scc():
    print('''0. Back
    1. Main menu''')
    user_entry_scc1 = input('Enter:  ')
    if user_entry_scc1 == "0":
        show_call_cost()
    elif user_entry_scc1 == "1":
        main_menu()
    else:
        print("Invalid Entry")
        back_scc()


def show_call_cost():
    print('''___Show call costs___
            1. Last call cost
            2. All call's cost
            3. Clear counters
            0. Back''')
    user_entry_scc = input("Enter:")
    if user_entry_scc == "0":
        call_register()
    elif user_entry_scc == "1":
        print('''___Last call cost___''')
        back_scc()
    elif user_entry_scc == "2":
        print('''___All call's cost___''')
        back_scc()
    elif user_entry_scc == "3":
        print('''___Clear counters___''')
        back_scc()
    else:
        print("Invalid Entry")
        show_call_cost()


def call_cost_settings():
    print('''___Call cost settings___
            1. Call cost limit
            2. Show cost in
            0. Back''')
    user_entry_ccs = input('Enter: ')
    if user_entry_ccs == "0":
        call_register()
    elif user_entry_ccs == "1":
        print('''___Call cost limit___''')
        back_cr()
    elif user_entry_ccs == "2":
        print('''___Show cost in___''')
        back_cr()
    else:
        print("Invalid Entry")
        call_cost_settings()


def back_tones():
    print('''0. Back
    1. Main menu''')
    user_entry_cs1 = input('Enter:  ')
    if user_entry_cs1 == "0":
        tones()
    elif user_entry_cs1 == "1":
        main_menu()
    else:
        print("Invalid Entry")
        back_tones()


def tones():
    print('''___Tones___
        1. Ringing Tone
        2. Ringing volume
        3. Incoming call alert
        4. Composer
        5. Message alert tone
        6. Keypad tones
        7. Warning and game tones
        8. Vibrating alert
        9. Screen saver
        0. Back''')
    user_entry_12 = input("Enter: ")
    if user_entry_12 == "0":
        main_menu()
    elif user_entry_12 == "1":
        print('___Ringing Tone___')
        back_tones()
    elif user_entry_12 == "2":
        print('___Ringing volume___')
        back_tones()
    elif user_entry_12 == "3":
        print('___Incoming call alert___')
        back_tones()
    elif user_entry_12 == "4":
        print('___Composer___')
        back_tones()
    elif user_entry_12 == "5":
        print('___Message alert tone___')
        back_tones()
    elif user_entry_12 == "6":
        print('___Keypad tones___')
        back_tones()
    elif user_entry_12 == "7":
        print('___Warning and game tones___')
        back_tones()
    elif user_entry_12 == "8":
        print('___ Vibrating alert___')
        back_tones()
    elif user_entry_12 == "9":
        print('___Screen saver__')
        back_tones()
    else:
        print("Invalid Entry")
        tones()


def settings():
    print('''___Settings___
       1. Call settings
       2. Phone settings
       3. Security settings
       4. Restore factory settings
       0. Back''')
    user_entry_6 = input("Enter: ")
    if user_entry_6 == "1":
        call_settings()
    elif user_entry_6 == "2":
        phone_settings()
    elif user_entry_6 == "3":
        security_settings()
    elif user_entry_6 == "4":
        print('''___Restore factory settings___
        0. Back''')
        user_input = int(input('Enter:'))
        if user_input == "0":
            settings()
        elif user_input == "1":
            main_menu()
        else:
            settings()
    elif user_entry_6 == "0":
        main_menu()
    else:
        print("Invalid Entry")
        settings()


def back_cs():
    print('''0. Back
    1. Main menu''')
    user_entry_cs1 = input('Enter:  ')
    if user_entry_cs1 == "0":
        call_settings()
    elif user_entry_cs1 == "1":
        main_menu()
    else:
        print("Invalid Entry")
        back_cs()


def call_settings():
    print('''___Call Settings___
            1. Automatic redial 
            2. Speed dialing
            3. Call waiting 
            4. Own number sending
            5. Phone line in use
            6. Automatic answer
            0. Back''')
    user_entry_cs = input('Enter: ')
    if user_entry_cs == "0":
        settings()
    elif user_entry_cs == "1":
        print('___Automatic redial___')
        back_cs()
    elif user_entry_cs == "2":
        print('___Speed dialing___')
        back_cs()
    elif user_entry_cs == "3":
        print('___Call Waiting___')
        back_cs()
    elif user_entry_cs == "4":
        print('___Own number sending___')
        back_cs()
    elif user_entry_cs == "5":
        print('___Phone line in use___')
        back_cs()
    elif user_entry_cs == "6":
        print('___Automatic answer___')
        back_cs()
    else:
        print("Invalid Entry")
        call_settings()


def back_ps():
    print('''0. Back
    1. Main menu''')
    user_entry_ps1 = int(input('Enter:  '))
    if user_entry_ps1 == "0":
        phone_settings()
    elif user_entry_ps1 == "1":
        main_menu()
    else:
        print("Invalid Entry")
        back_ps()


def phone_settings():
    print('''___Phone Settings___
            1. Language 
            2. Cell info display
            3. Welcome note
            4. Network selection
            5. Lights
            6. Confirm SIM service actions
            0. Back''')
    user_entry_ps = input('Enter: ')
    if user_entry_ps == "0":
        settings()
    elif user_entry_ps == "1":
        print('___Language___')
        back_ps()
    elif user_entry_ps == "2":
        print('___Cell info display___')
        back_ps()
    elif user_entry_ps == "3":
        print('___Welcome Note___')
        back_ps()
    elif user_entry_ps == "4":
        print('___Network Selection___')
        back_ps()
    elif user_entry_ps == "5":
        print('___Light___')
        back_ps()
    elif user_entry_ps == "6":
        print('___Confirm SIM service actions___')
        back_ps()
    else:
        print("Invalid Entry")
        phone_settings()


def back_ss():
    print('''0. Back
    1. Main menu''')
    user_entry_ss1 = input('Enter:  ')
    if user_entry_ss1 == "0":
        security_settings()
    elif user_entry_ss1 == "1":
        main_menu()
    else:
        print("Invalid Entry")
        back_ss()


def security_settings():
    print('''___Security Settings___
            1. PIN code request
            2. Call barring service
            3. Fixed dialing
            4. Closed user group
            5. Phone security
            6. Change access codes
            0. Back''')
    user_entry_ss = input('Enter: ')
    if user_entry_ss == "0":
        settings()
    elif user_entry_ss == "1":
        print('___PIN code request___')
        back_ss()
    elif user_entry_ss == "2":
        print('___Call barring service___')
        back_ss()
    elif user_entry_ss == "3":
        print('___Fixed dialing___')
        back_ss()
    elif user_entry_ss == "4":
        print('___Closed user group___')
        back_ss()
    elif user_entry_ss == "5":
        print('___Phone security___')
        back_ss()
    elif user_entry_ss == "6":
        print('___Change access codes___')
        back_ss()
    else:
        print("Invalid Entry")
        security_settings()


def back_clock():
    print('''0. Back
    1. Main menu''')
    user_entry_ss1 = input('Enter:  ')
    if user_entry_ss1 == "0":
        clock()
    elif user_entry_ss1 == "1":
        main_menu()
    else:
        print("Invalid Entry")
        back_clock()


def clock():
    print('''___Clock___
        1. Alarm clock
        2. Clock Settings
        3. Date settings
        4. Stop Watch
        5. Countdown timer
        6. Auto update of date and time
        0. Back''')
    user_entry_clock = input('Enter:  ')
    if user_entry_clock == "0":
        main_menu()
    elif user_entry_clock == "1":
        print('''___Alarm Clock___''')
        back_clock()
    elif user_entry_clock == "2":
        print('''___Clock Settings__''')
        back_clock()
    elif user_entry_clock == "3":
        print('''___Date settings___''')
        back_clock()
    elif user_entry_clock == "4":
        print('''___ Stop Watch___''')
        back_clock()
    elif user_entry_clock == "5":
        print('''___Countdown timer___''')
        back_clock()
    elif user_entry_clock == "6":
        print('''___Auto update of date and time___''')
        back_clock()
    else:
        print("Invalid Entry")
        clock()

if __name__ == "__main__":
    main_menu()
import pickle
keep_running = True
while keep_running == True:
    print "======================="
    print "|Electronic Phone Book|"
    print "======================="
    print "1. Look up an entry"
    print "2. Set an entry"
    print "3. Delete an entry"
    print "4. List all entries"
    print "5. Quit"
    response = raw_input('What do you want to do? (1-5): ')

    phone_book = []

    myfile = open('phonebook.pickle', 'r')
    myData = pickle.load(myfile)
    phone_book.append(myData)

    # phone_book = [
    #     {
    #         'first_name': 'Elijah',
    #         'last_name': 'Allstrom-Luttrell',
    #         'email': 'elieel@gmail.com',
    #         'phone': {
    #             'work': '(678)662-7020',
    #             'cell': '(678)662-7020'
    #         }
    #     }
    # ]
    #
    def opt_1():
        run = True
        while run == True:
            look_up = raw_input("What is the name you would like to look up? ").lower().capitalize()
            for i in phone_book:
                if look_up == i['first_name']:
                    print i['phone']
                    run = False
                else:
                    answer = raw_input("Entry not found. Would you like to add it as a new entry? (Y or N)\n").upper()
                    if answer == "Y" or answer == "YES":
                        opt_2
                    else:
                        run = False
    def opt_2():
        n_first_name = raw_input('What is the first name of the person you would like to add?\n').lower().capitalize()
        n_last_name = raw_input('What is their last name?\n').lower().capitalize()
        n_email = raw_input('What is their email? If no email put "none".\n')
        cell_phone = raw_input('What is their cell phone number?\n')
        work_phone = raw_input('What is their work phone number? If same as cell phone put "same".\n')
        if work_phone == 'same' or work_phone == 'Same':
            work_phone = cell_phone
        new_entry = {
            'first_name': n_first_name,
            'last_name': n_last_name,
            'email': n_email,
            'phone': {
                'work': work_phone,
                'cell': cell_phone
            }
        }
        myfile = open('phonebook.pickle', 'w')
        pickle.dump(new_entry, myfile)
        myfile = open('phonebook.pickle', 'r')
        myData = pickle.load(myfile)
        print myData
    def opt_3():
        pass
    def opt_4():
        pass






    if response == "1":
        opt_1()
    elif response == "2":
        opt_2()
    elif response == "3":
        opt_3()
    elif response == "4":
        opt_4()
    elif response == "5":
        break
    else:
        print "???"




































#

print "======================="
print "|Electronic Phone Book|"
print "======================="
print "1. Look up an entry"
print "2. Set an entry"
print "3. Delete an entry"
print "4. List all entries"
print "5. Quit"
response = raw_input('What do you want to do? (1-5): ')



phone_book = [
    {
        'first_name': 'Elijah',
        'last_name': 'Allstrom-Luttrell',
        'email': 'elieel@gmail.com',
        'phone': {
            'work': '(678)662-7020',
            'cell': '(678)662-7020'
        }
    }
]

def opt_1():
    run = True
    look_up = raw_input("What is the name you would like to look up? ").lower().capitalize()
    while run == True:
        for i in phone_book:
            if look_up == i['first_name']:
                print i['phone']
            else:
                answer = raw_input("Entry not found. Would you like to add it? (Y or N)\n").upper()
                if answer == "Y" or answer == "YES":
                    pass
def opt_2():
    new_entry = raw_input('What name would you like to add?\n')
    
def opt_3():

def opt_4():

def opt_5():






if response == "1":
    opt_1()
elif response == "2":
    opt_2()
elif response == "3":
    opt_3()
elif response == "4":
    opt_4
elif response == "5":
    opt_5
else:
    print "???"




































#

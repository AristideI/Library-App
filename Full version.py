from BOOKS import booka, bookb, bookc

""" 
Classes:
    one for BOOK:
        - id: str/id
        - title: str
        - pages: int
        - last page: int(remeber off by one)
    one for library:
        - collection of books: {id: Book()}
        - active book: variable collesp to id
"""


class Book():

    """ we initialise it with id, title, content and turn_page = 0 
    and will increase as the user reads the book"""
    
    def __init__(self, id, title, author, content): 
        self.id = id
        self.title = title
        self.author = author
        self.content = content
        self.last_page = 300
        
    def display_page(self):
        
        # this define where the read() func starts off
        
        return ' '.join(self.content[(self.last_page - 300):self.last_page])
    
    def turn_page(self):
        
        # turning pages will increment last page by 1 and return new display
        
        self.last_page += 300
        return self.display_page()
    
    def restart(self):
        # restarting from the start
        
        self.last_page = 300
        return self.display_page()
    
    
    def __str__(self):
        
        #func to pront the book and its pages and author
        
        return f"The book {self.title} by {self.author} has {len(self.content)} pages"
    
    
class Library:
    
    def __init__(self):
        self.collection = dict()
        self.active_book = None
        self.id_counter = 0
        
    def add_to_collection(self, title, content):
        new_book = Book(id, title, content)
        self.collection[new_book.id] = new_book
        self.id_counter += 1
        
book1 = Book(1, "The Role of Leaders Motivation", "Brian Karno ", booka)
book2 = Book(2, "A mom's Test", "Firts Patrick", bookb)
book3 = Book(3, "ML for SE", "Charles Isbell", bookc)
        
        
def loggedin():
    print("\nLog in Successfull")

    print("\nchoose your faculty\n")
        
    print('(1) BEL')
    print('(2) BSE')
    print('(3) BIT')
    print('(4) BGC')
    print('(5) BCS')
    print('(6) Log out')
    
    facultychoice = 'no'
    
    while facultychoice not in [1, 2, 3, 4, 5, 6]:
    
        facultychoice = int(input('choose your faculty: '))
    
        print('\n')
        
        print('_' * 70)
        
        pro = True
        
        while pro:
            if facultychoice == 1:
                print("Available books: \n")
                print("(1) The Role of Leaders Motivation")
                print("(2) A mom's Test")
                print("(3) Log out")
                   
                choice1 = 'no'
                while choice1 not in [1, 2, 3]:
                    choice1 = int(input("choose a book: "))
                
                if choice1 == 1:
                    print(f"\n {book1} \n")
                    
                    print(f"{book1.display_page()}\n")
                    
                    choice2 = 'no'
                    while choice2 not in [1, 2, 3, 4]:
                        choice2 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                    
                    if choice2 == 1:
                        print(f"\n{book1.turn_page()}\n")
                        
                        choice3 = 'no'
                        while choice3 not in [1, 2, 3, 4]:
                            choice3 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                        
                        if choice3 == 1:
                            print(f"\n{book1.turn_page()}\n")
                            
                        elif choice3 == 2:
                            pass
                        
                        elif choice3 == 3:
                            print(f"{book1.restart()}\n")
                            continue
                        
                        else:
                            print("\nLogged out\n")
                            break
                    
                        
                    elif choice2 == 2:
                        pass
                    
                    elif choice2 == 3:
                        print(f"{book1.restart()}\n")
                        continue
                    
                    
                    else:
                        print("\nLogged out\n")
                        break
                    
                elif choice1 == 2:
                    print(f"\n {book1} \n")
                    
                    print(f"{book1.display_page()}\n")
                    
                    choice2 = 'no'
                    while choice2 not in [1, 2, 3, 4]:
                        choice2 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                    
                    if choice2 == 1:
                        print(f"\n{book1.turn_page()}\n")
                        
                        choice3 = 'no'
                        while choice3 not in [1, 2, 3, 4]:
                            choice3 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                        
                        if choice3 == 1:
                            print(f"\n{book1.turn_page()}\n")
                            
                        elif choice3 == 2:
                            pass
                        
                        elif choice3 == 3:
                            print(f"{book1.restart()}\n")
                            continue
                        
                        else:
                            print("\nLogged out\n")
                            break
                    
                        
                    elif choice2 == 2:
                        pass
                    
                    elif choice2 == 3:
                        print(f"{book1.restart()}\n")
                        continue
                    
                    
                    else:
                        print("\nLogged out\n")
                        break
                    
                
                else:
                    print("\nLogged out\n")
                    
                    break
                    
                
           
            elif facultychoice == 2:
                
                print("Available books: \n")
                print("(1) ML for SE")
                print("(2) Python for machine learning")
                print("(3) Log out")
                   
                choice1 = 'no'
                while choice1 not in [1, 2, 3]:
                    choice1 = int(input("choose a book: "))
                
                if choice1 == 1:
                    print(f"\n {book1} \n")
                    
                    print(f"{book1.display_page()}\n")
                    
                    choice2 = 'no'
                    while choice2 not in [1, 2, 3, 4]:
                        choice2 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                    
                    if choice2 == 1:
                        print(f"\n{book1.turn_page()}\n")
                        
                        choice3 = 'no'
                        while choice3 not in [1, 2, 3, 4]:
                            choice3 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                        
                        if choice3 == 1:
                            print(f"\n{book1.turn_page()}\n")
                            
                        elif choice3 == 2:
                            pass
                        
                        elif choice3 == 3:
                            print(f"{book1.restart()}\n")
                            continue
                        
                        else:
                            print("\nLogged out\n")
                            break
                    
                        
                    elif choice2 == 2:
                    
                        pass
                    
                    elif choice2 == 3:
                        print(f"{book1.restart()}\n")
                        continue
                    
                    
                    else:
                        print("\nLogged out\n")
                        break
                    
                elif choice1 == 2:
                    print(f"\n {book1} \n")
                    
                    print(f"{book1.display_page()}\n")
                    
                    choice2 = 'no'
                    while choice2 not in [1, 2, 3, 4]:
                        choice2 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                    
                    if choice2 == 1:
                        print(f"\n{book1.turn_page()}\n")
                        
                        choice3 = 'no'
                        while choice3 not in [1, 2, 3, 4]:
                            choice3 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                        
                        if choice3 == 1:
                            print(f"\n{book1.turn_page()}\n")
                            
                        elif choice3 == 2:
                            pass
                        
                        elif choice3 == 3:
                            print(f"{book1.restart()}\n")
                            continue
                        
                        else:
                            print("\nLogged out\n")
                            break
                    
                        
                    elif choice2 == 2:
                        pass
                    
                    elif choice2 == 3:
                        print(f"{book1.restart()}\n")
                        continue
                    
                    
                    else:
                        print("\nLogged out\n")
                        break
                    
                    
                
                else:
                    print("\nLogged out\n")
                    
                    break
                
            
                
            elif facultychoice == 3:
                print("Available books: \n")
                print("(1) The Role of Leaders Motivation")
                print("(2) A mom's Test")
                print("(3) Log out")
                   
                choice1 = 'no'
                while choice1 not in [1, 2, 3]:
                    choice1 = int(input("choose a book: "))
                
                if choice1 == 1:
                    print(f"\n {book1} \n")
                    
                    print(f"{book1.display_page()}\n")
                    
                    choice2 = 'no'
                    while choice2 not in [1, 2, 3, 4]:
                        choice2 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                    
                    if choice2 == 1:
                        print(f"\n{book1.turn_page()}\n")
                        
                        choice3 = 'no'
                        while choice3 not in [1, 2, 3, 4]:
                            choice3 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                        
                        if choice3 == 1:
                            print(f"\n{book1.turn_page()}\n")
                            
                        elif choice3 == 2:
                            pass
                        
                        elif choice3 == 3:
                            print(f"{book1.restart()}\n")
                            continue
                        
                        else:
                            print("\nLogged out\n")
                            break
                    
                        
                    elif choice2 == 2:
                        pass
                    
                    elif choice2 == 3:
                        print(f"{book1.restart()}\n")
                        continue
                    
                    
                    else:
                        print("\nLogged out\n")
                        break
                    
                elif choice1 == 2:
                    print(f"\n {book1} \n")
                    
                    print(f"{book1.display_page()}\n")
                    
                    choice2 = 'no'
                    while choice2 not in [1, 2, 3, 4]:
                        choice2 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                    
                    if choice2 == 1:
                        print(f"\n{book1.turn_page()}\n")
                        
                        choice3 = 'no'
                        while choice3 not in [1, 2, 3, 4]:
                            choice3 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                        
                        if choice3 == 1:
                            print(f"\n{book1.turn_page()}\n")
                            
                        elif choice3 == 2:
                            pass
                        
                        elif choice3 == 3:
                            print(f"{book1.restart()}\n")
                            continue
                        
                        else:
                            print("\nLogged out\n")
                            break
                    
                        
                    elif choice2 == 2:
                        pass
                    
                    elif choice2 == 3:
                        print(f"{book1.restart()}\n")
                        continue
                    
                    
                    else:
                        print("\nLogged out\n")
                        break
                    
                    
                
                else:
                    print("\nLogged out\n")
                    break
                    
                
            elif facultychoice == 4:
                print("Available books: \n")
                print("(1) C programming for beginner")
                print("(2) python for machine learning")
                print("(3) Log out")
                   
                choice1 = 'no'
                while choice1 not in [1, 2, 3]:
                    choice1 = int(input("choose a book: "))
                
                if choice1 == 1:
                    print(f"\n {book1} \n")
                    
                    print(f"{book1.display_page()}\n")
                    
                    choice2 = 'no'
                    while choice2 not in [1, 2, 3, 4]:
                        choice2 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                    
                    if choice2 == 1:
                        print(f"\n{book1.turn_page()}\n")
                        
                        choice3 = 'no'
                        while choice3 not in [1, 2, 3, 4]:
                            choice3 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                        
                        if choice3 == 1:
                            print(f"\n{book1.turn_page()}\n")
                            
                        elif choice3 == 2:
                            pass
                        
                        elif choice3 == 3:
                            print(f"{book1.restart()}\n")
                            continue
                        
                        else:
                            print("\nLogged out\n")
                            break
                    
                        
                    elif choice2 == 2:
                        pass
                    
                    elif choice2 == 3:
                        print(f"{book1.restart()}\n")
                        continue
                    
                    
                    else:
                        print("\nLogged out\n")
                        break
                    
                elif choice1 == 2:
                    print(f"\n {book1} \n")
                    
                    print(f"{book1.display_page()}\n")
                    
                    choice2 = 'no'
                    while choice2 not in [1, 2, 3, 4]:
                        choice2 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                    
                    if choice2 == 1:
                        print(f"\n{book1.turn_page()}\n")
                        
                        choice3 = 'no'
                        while choice3 not in [1, 2, 3, 4]:
                            choice3 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                        
                        if choice3 == 1:
                            print(f"\n{book1.turn_page()}\n")
                            
                        elif choice3 == 2:
                            pass
                        
                        elif choice3 == 3:
                            print(f"{book1.restart()}\n")
                            continue
                        
                        else:
                            print("\nLogged out\n")
                            break
                    
                        
                    elif choice2 == 2:
                        pass
                    
                    elif choice2 == 3:
                        print(f"{book1.restart()}\n")
                        continue
                    
                    
                    else:
                        print("\nLogged out\n")
                        break
                    
                    
                
                else:
                    print("\nLogged out\n")
                    break
                
            elif facultychoice == 5:
                
                print("Available books: \n")
                print("(1) OOP in Java")
                print("(2) Python for ML")
                print("(3) Log out")
                   
                choice1 = 'no'
                while choice1 not in [1, 2, 3]:
                    choice1 = int(input("choose a book: "))
                
                if choice1 == 1:
                    print(f"\n {book1} \n")
                    
                    print(f"{book1.display_page()}\n")
                    
                    choice2 = 'no'
                    while choice2 not in [1, 2, 3, 4]:
                        choice2 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                    
                    if choice2 == 1:
                        print(f"\n{book1.turn_page()}\n")
                        
                        choice3 = 'no'
                        while choice3 not in [1, 2, 3, 4]:
                            choice3 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                        
                        if choice3 == 1:
                            print(f"\n{book1.turn_page()}\n")
                            
                        elif choice3 == 2:
                            pass
                        
                        elif choice3 == 3:
                            print(f"{book1.restart()}\n")
                            continue
                        
                        else:
                            print("\nLogged out\n")
                            break
                    
                        
                    elif choice2 == 2:
                        pass
                    
                    elif choice2 == 3:
                        print(f"{book1.restart()}\n")
                        continue
                    
                    
                    else:
                        print("\nLogged out\n")
                        break
                    
                elif choice1 == 2:
                    print(f"\n {book1} \n")
                    
                    print(f"{book1.display_page()}\n")
                    
                    choice2 = 'no'
                    while choice2 not in [1, 2, 3, 4]:
                        choice2 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                    
                    if choice2 == 1:
                        print(f"\n{book1.turn_page()}\n")
                        
                        choice3 = 'no'
                        while choice3 not in [1, 2, 3, 4]:
                            choice3 = int(input("(1) next, (2) stop, (3) restart (4) log out: "))
                        
                        if choice3 == 1:
                            print(f"\n{book1.turn_page()}\n")
                            
                        elif choice3 == 2:
                            pass
                        
                        elif choice3 == 3:
                            print(f"{book1.restart()}\n")
                            continue
                        
                        else:
                            print("\nLogged out\n")
                            break
                    
                        
                    elif choice2 == 2:
                        pass
                    
                    elif choice2 == 3:
                        print(f"{book1.restart()}\n")
                        continue
                    
                    
                    else:
                        print("\nLogged out\n")
                        break
                    
                    
                
                else:
                    print("\nLogged out\n")
                    break
                
            elif facultychoice == 6:
                print("\nLogged out\n")
                pro = False
                break
    


users = ['sample']
passwords = ['sample']


while True:
    print("Select an option (l)ogin | (s)ign up")
    answer = input("")

    if answer == "s":
        
        global user
        global password 
        
        while True:
            user = input("Create user name: ")
    
            if user in users:
                print("Username already exists")
                continue
        
            else:
                users.append(user)
                break
        
        password = input("Create user password: ")
        passwords.append(password)
        print("\nAccount created successfully!\n")
        continue
        
        
    
    elif answer == "l":
        
        username = input("Enter user name: ")
    
        while username not in users:
            print("\nUser not found")
            username = input("Enter user name: ")
    
            
    
        user_password = input("Enter user password: ")
    
        while user_password not in passwords:
            print("\nPassword incorrect")
            user_password = input("Enter user password: ")
            
        loggedin()
                   
    
    else:
         print("Error Select either l or s")
         continue


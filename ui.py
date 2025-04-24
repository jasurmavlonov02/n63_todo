from service import login ,register, logout,todo_list


def menu():
    print('Login => 1')
    print('Register => 2')
    print('Logout => 3')
    print('Todo List => 4')
    print('Todo Add => 5')
    print('Quit => q')
    return input('say ...')



def login_response():
    username = input('Username : ')
    password = input('Password : ')
    response = login(username,password)
    print(response.message)
    
    

def register_response():
    username = input('Username : ')
    password = input('Password : ')
    response = register(username,password)
    print(response.message)
    
    
    

def logout_response():
    response = logout()
    print(response.message)
    
    
    

def run():
    while True:
        choice = menu()
        if choice == '1':
            login_response()
        
        elif choice == '2':
            register_response()
        
        elif choice == '3':
            logout_response()
        
        elif choice == '4':
            todo_list()
            
            
        elif choice == 'q':
            break
        
        
if __name__ == '__main__':
    run()
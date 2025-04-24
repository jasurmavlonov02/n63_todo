from service import login ,register, logout,todo_list,todo_add,login_required,is_admin

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
    

@login_required
@is_admin  
def create_todo():
    title = input('Title : ')
    user_id = int(input('USER ID : '))
    response = todo_add(title,user_id)
    return response
    
    
    

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
        
        elif choice == '5':
            response = create_todo()
            print(response.message)
            
        elif choice == 'q':
            break
        
        
if __name__ == '__main__':
    run()
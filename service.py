from sessions import Session
from models import User,UserRole,TodoType
from utils import Response,match_password,hash_password
from database import cursor,commit
from validations import check_validations
from forms import UserForm



session = Session()

# =========================== Decorator ========================

def login_required(func):
    def wrapper(*args,**kwargs):
        if not session.session:
            return Response('You must login firstly',status_code=401)
        result = func(*args,**kwargs)
        return result
    return wrapper



def is_admin(func):
    def wrapper(*args,**kwargs):
        if session.session:
            if session.session.role != 'admin':
                return Response('You dont have any permisson for admin role',status_code=401)
        result = func(*args,**kwargs)
        return result
    
    return wrapper
                

# =============================================================



@commit
def login(username:str,password:str):
    user : Session | None = session.check_session()
    if user:
        return Response(message='You already logged in',status_code=401)
    get_user_by_username_query = '''
        select * from users where username = %s;
    '''
    data = (username,)
    cursor.execute(get_user_by_username_query,data)
    user_data = cursor.fetchone()
    if not user_data:
        return Response('User not Found',status_code=404)
    
    user = User.from_tuple(user_data)
    if not match_password(password,user.password):
        update_login_try_count_field = '''
            UPDATE users set login_try_count = login_try_count + 1
            where username = %s;
        '''
        cursor.execute(update_login_try_count_field,data)
        return Response('Password did not match')
    session.add_session(user)
    return Response('You successfully logged in ✅✅✅')
    


# response = login('ADMIN','admin1234')
# print(response.message)


@commit
def register(username,password):
    form = UserForm(username,password)
    check_validations(form)
    user_query= '''
        select * from users where username = %s;
    '''
    cursor.execute(user_query,(username,))
    user_data = cursor.fetchone()
    if user_data:
        return Response('You already registered',status_code=404)
    create_user_query = '''
        insert into users(username,password,role,email,login_try_count)
        values(%s,%s,%s,%s,%s);
    '''
    data = (username,hash_password(password),UserRole.USER.value,None,0)
    cursor.execute(create_user_query,data)
    return Response('Successfully registered✅✅',status_code=201)
    
    
# response = register('jasur','123')
# print(response.message)

def logout():
    if session.session:
        # session.session = None
        session.remove_session()
        return Response('You Successfully Logged Out✅✅')
    
    return Response('You must login firstly')


def todo_list():
    select_todo_list_query = '''select * from todo;'''
    cursor.execute(select_todo_list_query)
    todos = cursor.fetchall()
    for todo in todos:
        print(todo)
        
        

@login_required
@is_admin
@commit
def todo_add(title,user_id):
    insert_todo_query = '''insert into todo(title,description,todo_type,user_id) values (%s,%s,%s,%s);'''
    todo_data = (title,None,TodoType.PERSONAL.value,user_id)
    cursor.execute(insert_todo_query,todo_data)
    return Response('Todo Succesfully created ✅✅')
    
    

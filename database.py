import psycopg2
from utils import hash_password
from models import UserRole


db_config = {
    "host": "localhost",
    "database": "testing_db",
    "user":"postgres",
    "password":"123",
    "port": 5432
}

conn = psycopg2.connect(**db_config)
cursor = conn.cursor()


def create_table_user():
    create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(100) ,
            role varchar(20) DEFAULT 'USER',
            login_try_count int DEFAULT 0
        );
    """
    cursor.execute(create_table_query)


def create_table_todo():
    create_table_query = """
        CREATE TABLE IF NOT EXISTS todo(
            id SERIAL PRIMARY KEY,
            title VARCHAR(120) NOT NULL,
            description TEXT ,
            todo_type varchar(25) NOT NULL DEFAULT 'PERSONAL',
            created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
            user_id INT REFERENCES users(id)
                on delete SET NULL
        );
    """
    cursor.execute(create_table_query)


def init():
    create_table_user()
    create_table_todo()
    conn.commit()
    print('Table Successfully created')
    

# init()


def commit(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        conn.commit()
        return result
    return wrapper


@commit
def insert_admin_user():
    insert_user_query = '''
        insert into users(username,password,role)
        values (%s,%s,%s);
    '''
    admin_data = ('ADMIN',hash_password('admin123'),UserRole.ADMIN.value)
    cursor.execute(insert_user_query,admin_data)
    print('Admin created ! ')
    
# insert_admin_user()

from forms import UserForm

def check_validations(form:UserForm):
    if form.username is None:
        raise Exception('username cannot be None')
    if form.password is None:
        raise Exception('password cannot be None')

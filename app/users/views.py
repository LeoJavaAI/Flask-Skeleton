from flask import Blueprint, render_template, request,flash, redirect, url_for
from app.users.models import Users, UsersSchema

users = Blueprint('users', __name__)
#http://marshmallow.readthedocs.org/en/latest/quickstart.html#declaring-schemas
schema = UsersSchema()

#Users
@users.route('/' )
def user_index():
    users = Users.query.all()
    results = schema.dump(users, many=True).data
    return render_template('/users/index.html', results=results)

@users.route('/add' , methods=['POST', 'GET'])
def user_add():
    if request.method == 'POST':
        #Validate form values by de-serializing the request, http://marshmallow.readthedocs.org/en/latest/quickstart.html#validation
        form_errors = schema.validate(request.form.to_dict())
        if not form_errors:        
            name=request.form['name']
            email=request.form['email']
            user=Users(email, name)
            return add(user, success_url = 'users.user_index', fail_url = 'users.user_add')
        else:
           flash(form_errors)        

    return render_template('/users/add.html')

@users.route('/update/<int:id>' , methods=['POST', 'GET'])

def user_update (id):
    #Get user by primary key:
    user=Users.query.get_or_404(id)
    if request.method == 'POST':
        form_errors = schema.validate(request.form.to_dict())
        if not form_errors:
           user.name = request.form['name']
           user.email = request.form['email']
           return update(user , id, success_url = 'users.user_index', fail_url = 'users.user_update')
        else:
           flash(form_errors)

    return render_template('/users/update.html', user=user)


@users.route('/delete/<int:id>' , methods=['POST', 'GET'])
def user_delete (id):
     user = Users.query.get_or_404(id)
     return delete(user, fail_url = 'users.user_index')
     
     
#CRUD FUNCTIONS
#Arguments  are data to add, function to redirect to if the add was successful and if not
def add (data, success_url = '', fail_url = ''):
    add = data.add(data)
    #if does not return any error
    if not add :
       flash("Add was successful")
       return redirect(url_for(success_url))
    else:
       message=add
       flash(message)
       return redirect(url_for(fail_url))


def update (data, id, success_url = '', fail_url = ''):

            update=data.update()
            #if does not return any error
            if not update :
              flash("Update was successful")
              return redirect(url_for(success_url))
            else:
               message=update
               flash(message)
               return redirect(url_for(fail_url, id=id))



def delete (data, fail_url=''):
     delete=data.delete(data)
     if not delete :
              flash("Delete was successful")

     else:
          message=delete
          flash(message)
     return redirect(url_for(fail_url))
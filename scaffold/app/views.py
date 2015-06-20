#resource, resources, Resources
from flask import Blueprint, render_template, request,flash, redirect, url_for
from app.{resources}.models import {Resources}, {Resources}Schema

{resources} = Blueprint('{resources}', __name__)
#http://marshmallow.readthedocs.org/en/latest/quickstart.html#declaring-schemas
schema = {Resources}Schema()

#{Resources}
@{resources}.route('/' )
def {resource}_index():
    {resources} = {Resources}.query.all()
    results = schema.dump({resources}, many=True).data
    return render_template('/{resources}/index.html', results=results)

@{resources}.route('/add' , methods=['POST', 'GET'])
def {resource}_add():
    if request.method == 'POST':
        #Validate form values by de-serializing the request, http://marshmallow.readthedocs.org/en/latest/quickstart.html#validation
        form_errors = schema.validate(request.form.to_dict())
        if not form_errors:
            {resource}={Resources}({add_fields})
            return add({resource}, success_url = '{resources}.{resource}_index', fail_url = '{resources}.{resource}_add')
        else:
           flash(form_errors)

    return render_template('/{resources}/add.html')

@{resources}.route('/update/<int:id>' , methods=['POST', 'GET'])

def {resource}_update (id):
    #Get {resource} by primary key:
    {resource}={Resources}.query.get_or_404(id)
    if request.method == 'POST':
        form_errors = schema.validate(request.form.to_dict())
        if not form_errors:
           {update_fields}
           return update({resource} , id, success_url = '{resources}.{resource}_index', fail_url = '{resources}.{resource}_update')
        else:
           flash(form_errors)

    return render_template('/{resources}/update.html', {resource}={resource})


@{resources}.route('/delete/<int:id>' , methods=['POST', 'GET'])
def {resource}_delete (id):
     {resource} = {Resources}.query.get_or_404(id)
     return delete({resource}, fail_url = '{resources}.{resource}_index')


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

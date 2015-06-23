#resource, resources, Resources
from flask import Blueprint, render_template, request,flash, redirect, url_for
from app.customers.models import Customers, CustomersSchema

customers = Blueprint('customers', __name__, template_folder='templates')
#http://marshmallow.readthedocs.org/en/latest/quickstart.html#declaring-schemas
schema = CustomersSchema()

#Customers
@customers.route('/' )
def customer_index():
    customers = Customers.query.all()
    results = schema.dump(customers, many=True).data
    return render_template('/customers/index.html', results=results)

@customers.route('/add' , methods=['POST', 'GET'])
def customer_add():
    if request.method == 'POST':
        #Validate form values by de-serializing the request, http://marshmallow.readthedocs.org/en/latest/quickstart.html#validation
        form_errors = schema.validate(request.form.to_dict())
        if not form_errors:
            customer=Customers(
                                request.form['name'],
                                request.form['address'],
                                request.form['is_active'],
                                request.form['mobile'],
                                request.form['email'],
                                request.form['url'],
                                request.form['timestamp'],
                                request.form['date'],
                                request.form['pricing'],)
            return add(customer, success_url = 'customers.customer_index', fail_url = 'customers.customer_add')
        else:
           flash(form_errors)

    return render_template('/customers/add.html')

@customers.route('/update/<int:id>' , methods=['POST', 'GET'])

def customer_update (id):
    #Get customer by primary key:
    customer=Customers.query.get_or_404(id)
    if request.method == 'POST':
        form_errors = schema.validate(request.form.to_dict())
        if not form_errors:
           
            customer.name = request.form['name']
            customer.address = request.form['address']
            customer.is_active = request.form['is_active']
            customer.mobile = request.form['mobile']
            customer.email = request.form['email']
            customer.url = request.form['url']
            customer.timestamp = request.form['timestamp']
            customer.date = request.form['date']
            customer.pricing = request.form['pricing']

            return update(customer , id, success_url = 'customers.customer_index', fail_url = 'customers.customer_update')
        else:
           flash(form_errors)

    return render_template('/customers/update.html', customer=customer)


@customers.route('/delete/<int:id>' , methods=['POST', 'GET'])
def customer_delete (id):
     customer = Customers.query.get_or_404(id)
     return delete(customer, fail_url = 'customers.customer_index')


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

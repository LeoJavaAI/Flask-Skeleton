Flask-Scaffold allows you to quickly prototype a CRUD application in python 3.4 with Flask, FLask-SQLAlchemy,  and PostgreSQL.

Please ensure PostgreSQL is installed with the development libraries. Steps are available [here](http://techarena51.com/index.php/flask-sqlalchemy-postgresql-tutorial/)


![](https://travis-ci.org/Leo-g/Flask-Scaffold.svg?branch=master)
###Installation Steps
####Step 1:Clone the project to your application folder.

    git clone git@github.com:Leo-g/Flask-Scaffold.git YourAppFolderName

####Step 2: Activate the virtual environment and install the requirements.
 
    cd YourAppFolderName
    virtualenv -p /usr/bin/python3.4 venv-3.4
    source venv-3.4/bin/activate
    pip install -r requirements.txt 
    
    
#### Step 3 : Create a Scaffold with the fields you require.

For a list of supported fields please see the wiki

    vim scaffold/module.yaml
    customers:
     - name:String
     - address:Text
     - is_active:Boolean
     - mobile:Integer
     - email:Email
     - url:URL
     - timestamp:DateTime
     - date:Date
     - pricing:Decimal
    
    python scaffold.py scaffold/module.yaml
    

#### Step 4 : Update the config file with your Database Username, Database Password, Database Name and Database Hostname

    vim config.py

#### Step 5 : Run migrations 
   
    python db.py db init
    python db.py db migrate
    python db.py db upgrade
   
####  Step 5 : Start the server.
    python run.py


**You should be able to see the App at  http://localhost:5000/customers**


####Tests
To run tests for all modules

      bash tests.bash
To run tests for a specific module

     python app/customers/test.py


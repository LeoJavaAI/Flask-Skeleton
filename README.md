Flask-Skeleton allows you to quickly build a Skeleton CRUD application  in python 3.4 with Flask, FLask-SQLAlchemy, marshmallow and PostgreSQL.

Please ensure PostgreSQL is installed with the development libraries. Steps are available [here](http://techarena51.com/index.php/flask-sqlalchemy-postgresql-tutorial/)

For Complete Documentation with screenshots and troubleshooting please see the [wiki](https://github.com/Leo-g/Flask-Skeleton/wiki)

###Installation Steps
####Step 1:Clone the project to your application folder.

    git clone git@github.com:Leo-g/Flask-Skeleton.git YourAppFolderName

####Step 2: Activate the virtual environment.
 
    cd YourAppFolderName
    source venv-3.4/bin/activate

#### Step 3 : Update the config file with your Database Username, Database Password, Database Name and Database Hostname

    vim config.py

#### Step 4 : Run migrations 
   
    python db.py db init
    python db.py db migrate
    python db.py db upgrade
   
####  Step 5 : Start the server.
    python run.py

Crud operations are performed on a user resource.

**You should be able to see the App at  http://localhost:5000/users**

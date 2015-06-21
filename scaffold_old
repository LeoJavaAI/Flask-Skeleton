import os
import shutil
import sys
import inflect

#Get name of the resource
input = sys.argv[1]

def make_plural (resource):
    #https://pypi.python.org/pypi/inflect
    p = inflect.engine()
    if p.singular_noun(resource):
       resources = resource
       resource = p.singular_noun(resource)       
       return resource, resources
    else:
       resources =  p.plural(resource)
       return resource, resources

       
resource, resources = make_plural(input)

#Get paths
app_resource_path = os.path.join('app',resources)
app_files = ['__init__.py', 'views.py', 'models.py']
template_resource_path = os.path.join('app/templates',resources)
template_files = ['add.html', '_form.html', 'index.html', 'update.html']

#replace template content with new resource content 
def generate(resource_path, file):
    with open(os.path.join(resource_path, file), 'a') as new_file:
        with open(os.path.join('scaffold/app/', file), 'r') as old_file:
               for line in old_file:
                   new_file.write(line.format(resource=resource, resources=resources, Resources=resources.title()))


#create the files for the resource
def create_files(resource_path, files):

    if not os.path.isdir(resource_path):
          try:  
              os.mkdir(resource_path)
              for file in files:                
                   generate(resource_path, file)
                  
              print('{} created successfully'.format(resource_path))
              return True
          except  OSError as e:         
             print(e)
             return False
               
    else:
       print('{} already exists'.format(resource_path))
       return False       
       
 
#register blueprints
def blueprint_register():
    string_to_insert_after = '#Blueprints'
    new_blueprint = """
    #Blueprints
    from app.{resources}.views import {resources}
    app.register_blueprint({resources}, url_prefix='/{resources}')""".format(resources=resources)
        
    filedata = None
    app_file = 'app/__init__.py'
    with open(app_file, 'r+') as file:    
        filedata = file.read()
    if string_to_insert_after  in filedata:
      #replace the first occurrence
      filedata = filedata.replace(string_to_insert_after, new_blueprint,1)
      with open(app_file, 'w') as file:
        file.write(filedata)
        print("Registered Blueprints for ",resources)
        return True
    else:
      print("""Cannot find string #Blueprints in app/__init.py__", please ensure this file is similar to \n
               https://github.com/Leo-g/Flask-Skeleton/blob/master/app/__init__.py""")
      return False
               
      


if create_files(app_resource_path, app_files) and create_files(template_resource_path, template_files) and blueprint_register() :
    print ("created", resources)
    sys.exit(0)
else:
    print("running rm")
    for path in [app_resource_path, template_resource_path]:
      if os.path.isdir(path):
        shutil.rmtree(path)
 

#

       

    
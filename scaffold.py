import os
import shutil
import sys
import inflect

#Get name of the resource
input = input("Enter resource name: ")

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
template_files = ['_form.html', 'index.html', 'update.html', 'add.html']

def generate(file):
    with open(os.path.join('app',resources, file), 'a') as new_file:
        with open(os.path.join('scaffold/app/', file), 'r') as old_file:
               for line in old_file:
                   new_file.write(line.format(resource=resource, resources=resources, Resources=resources.title()))


def create_files(resource_path, files):

    if not os.path.isdir(resource_path):
          try:  
              os.mkdir(resource_path)
              for file in files:                
                   generate(file)
                  
              print('{} created successfully'.format(resource_path))
              return True
          except  OSError as e:         
             print(e)
               
    else:
       print('{} already exists'.format(resource_path))  
       
       
#Create the files
if create_files(app_resource_path, app_files):
    sys.exit(0)
else:
    for path in [app_resource_path, template_resource_path]:
      if os.path.isdir(path):
        shutil.rmtree(path)
 

#

       

    
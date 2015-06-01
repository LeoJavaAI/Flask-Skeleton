import os
import shutil
import sys

resource = input("Enter name of the resource to create: ")
app_resource_path = os.path.join('app',resource)
app_files = ['__init__.py', 'views.py', 'models']
template_resource_path = os.path.join('app/templates',resource)
template_files = ['_form.html', 'index.html', 'update.html', 'add.html']


def create_files(resource_path, files):

    if not os.path.isdir(resource_path):
          try:  
              os.mkdir(resource_path)
              for file in files:
                file_path = os.path.join(resource_path, file)
                with open(file_path, 'w') as file:
                  file.close()
              print('{} created successfully'.format(resource_path))
              return True
          except  OSError as e:         
             print(e)
               
    else:
       print('{} already exists'.format(resource_path))  
       
       

if create_files(app_resource_path, app_files) and create_files(template_resource_path, template_files):
    sys.exit(0)
else:
    for path in [app_resource_path, template_resource_path]:
      if os.path.isdir(path):
        shutil.rmtree(path)
    
       

    
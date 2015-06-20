#!/usr/bin/env python
import yaml
import inflect
import os
import shutil


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

def generate_files (module_path):

    app_files = ['views.py', 'models.py', '__init__.py','_form.html', 'add.html', 'update.html']

    for file in app_files:

        #Generate App files
        if file == "views.py":
            with open( os.path.join(module_path,'views.py') , "w") as new_file:
                with open( "scaffold/app/views.py" , "r") as old_file:
                            for line in old_file:
                                new_file.write(line.format(resource=resource, resources=resources,
                                                           Resources=resources.title(),
                                                           add_fields=add_fields,
                                                           update_fields=update_fields))



        elif file == "models.py":
            with open( os.path.join(module_path,'models.py'), "w") as new_file:
                with open( "scaffold/app/models.py" , "r") as old_file:
                     for line in old_file:
                         new_file.write(line.format(resource=resource, resources=resources,
                                                    Resources=resources.title(), db_rows=db_rows,
                                                     schema=schema, meta=meta, init_self_vars=init_self_vars,
                                                     init_args=init_args))

        elif file == "__init__.py":
            with open( os.path.join(module_path,'__init__.py'), "w") as new_file:
                with open( "scaffold/app/__init__.py" , "r") as old_file:
                     for line in old_file:
                         new_file.write(line)

        #Generate Template Files
        ## Need to add template resourc path
        elif file == "_form.html":
             with open( os.path.join(module_path,'templates','_form.html'), "w") as new_file:
                 with open( "scaffold/app/_form.html" , "r") as old_file:
                      for line in old_file:
                          new_file.write(line.format(resource=resource, resources=resources,
                                                     Resources=resources.title(), form_args=form_args,
                                                     form_fields =form_fields))

        elif file == "add.html":
            with open( os.path.join(module_path,'templates','add.html'), "w") as new_file:
                with open( "scaffold/app/add.html" , "r") as old_file:
                     for line in old_file:
                         new_file.write(line.format(resource=resource, resources=resources,
                                                    Resources=resources.title()))
        elif file == "update.html":
            with open( os.path.join(module_path, 'templates','update.html'), "w") as new_file:
                with open( "scaffold/app/update.html" ,  "r") as old_file:
                     for line in old_file:
                         new_file.write(line.format(resource=resource, resources=resources,
                                                    Resources=resources.title(),
                                                    update_form_args=update_form_args))

    return True


def clean_up(module_path):
          if os.path.isdir(module_path):
            shutil.rmtree(module_path)

#Parse YAML file
with open( "scaffold/app/module.yaml" , "r") as yaml_file:

    yaml_data = yaml.load(yaml_file)

    for module, fields in yaml_data.items():
        #make module name plural
        resource, resources = make_plural(module)

        # Start strings to insert into models
        db_rows = ""
        schema = ""
        meta = ""
        init_self_vars = ""
        init_args = ""
        #End strings to insert into models

        #Start strings to insert into views
        add_fields =""
        update_fields =""

        #strings to insert into _form.html
        form_args = ""
        form_fields =""

        #stings to insert into update.html
        update_form_args =""



        for f in fields:
            field, field_type = f.split(':')
            if field_type == "string":
                   db_rows += """
    {} = db.Column(db.String(250), nullable=False)""".format(field)
                   schema += """
    {} = fields.String(validate=not_blank)""".format(field)
                   meta += """ '{}', """.format(field)
                   init_args += """ {}, """.format(field)
                   init_self_vars += """
        self.{field} = {field}""".format(field=field)
                   #Views
                   add_fields +="""'request.form['{}']',""".format(field)
                   update_fields +="""
           {resource}.{field} = request.form['{field}'] """.format(resource=resource, field=field)
                   #_form.html
                   form_args += """{resource}_{field} = '',""".format(resource=resource, field=field)
                   form_fields +="""
        <label>{Field}
         <small>required</small><input type="text" name="{field}" value="{{{{ {resource}_{field} }}}}"  required/>
        </label> """.format(Field=field.title(), field=field, resource=resource)
                   update_form_args += """{resource}_{field} = {resource}.{field}, """.format(resource=resource,
                                                                                             field=field)



        #Generate files with the new fields
        module_dir = os.path.join('test/app',resources)


        try:
             os.mkdir(module_dir)
             try:
                 os.mkdir('{}/templates'.format(module_dir))
                 generate_files(module_dir)

                 print('{} created successfully'.format(module_dir))
             except:
                 clean_up(module_dir)
                 raise

        except:
            raise

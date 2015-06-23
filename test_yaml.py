#!/usr/bin/env python
import yaml
import inflect
import os
import shutil
from scaffold.custom_fields import boolean_form_string,integer_form_string,email_form_string,\
url_form_string, datetime_form_string, date_form_string, decimal_form_string, text_form_string

blueprint_file = 'app/__init__.py'

#Error classes
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class BlueprintError(Error):

    def __init__(self):
        self.msg = "Cannot register Blueprints"

    def __str__(self):
        return repr(self.msg)


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

    app_files = ['views.py', 'models.py', '__init__.py','_form.html', 'add.html', 'update.html',
                 'index.html']

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
             with open( os.path.join(module_path,'templates', resources, '_form.html'), "w") as new_file:
                 with open( "scaffold/app/_form.html" , "r") as old_file:
                      for line in old_file:
                          new_file.write(line.format(resource=resource, resources=resources,
                                                     Resources=resources.title(),
                                                     form_args=','.join(form_args),
                                                     form_fields =form_fields))

        elif file == "add.html":
            with open( os.path.join(module_path,'templates', resources,'add.html'), "w") as new_file:
                with open( "scaffold/app/add.html" , "r") as old_file:
                     for line in old_file:
                         new_file.write(line.format(resource=resource, resources=resources,
                                                    Resources=resources.title()))
        elif file == "update.html":
            with open( os.path.join(module_path, 'templates', resources,'update.html'), "w") as new_file:
                with open( "scaffold/app/update.html" ,  "r") as old_file:
                     for line in old_file:
                         new_file.write(line.format(resource=resource, resources=resources,
                                                    Resources=resources.title(),
                                                    update_form_args=update_form_args))
        elif file == "index.html":
            with open( os.path.join(module_path, 'templates', resources,'index.html'), "w") as new_file:
                with open( "scaffold/app/index.html" ,  "r") as old_file:
                     for line in old_file:
                         new_file.write(line.format(resource=resource, resources=resources,
                                                    Resources=resources.title(),
                                                    field_table_headers=field_table_headers,
                                                    index_fields=index_fields))


def register_blueprints():
    string_to_insert_after = '#Blueprints'
    new_blueprint = """
    #Blueprints
    from app.{resources}.views import {resources}
    app.register_blueprint({resources}, url_prefix='/{resources}')""".format(resources=resources)



    with open(blueprint_file, 'r+') as old_file:
        filedata = old_file.read()
    if string_to_insert_after  in filedata:
      #replace the first occurrence
      new_filedata = filedata.replace(string_to_insert_after, new_blueprint,1)
      with open(blueprint_file, 'w') as new_file:
        new_file.write(new_filedata)
        print("Registered Blueprints for ",resources)
    else:
      raise BlueprintError()


def clean_up(module_path):
          if os.path.isdir(module_path):
            shutil.rmtree(module_path)

#Parse YAML file
with open( "scaffold/module.yaml" , "r") as yaml_file:

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
        form_args = []
        form_fields =""

        #stings to insert into update.html
        update_form_args =""

        #stings to insert into index.html
        field_table_headers =""
        index_fields=""



        for f in fields:
            field, field_type = f.split(':')
            if field_type == "String":
                   db_rows += """
    {} = db.Column(db.String(250), nullable=False)""".format(field)
                   schema += """
    {} = fields.String()""".format(field)

                   form_fields +="""
           <label>{Field}
           <small>required</small><input type="text" name="{field}" value="{{{{ {resource}_{field} }}}}"  required/>
           </label> """.format(Field=field.title(), field=field, resource=resource)

            elif field_type == "Boolean":
                         db_rows += """
    {} = db.Column(db.Boolean, nullable=False)""".format(field)
                         schema += """
    {} = fields.Boolean()""".format(field)
                         form_fields +=boolean_form_string.format(Field=field.title(),
                                                                  field=field, resource=resource)
            elif field_type == "Integer":
                     db_rows += """
    {} = db.Column(db.Integer, nullable=False)""".format(field)
                     schema += """
    {} = fields.Integer()""".format(field)
                     form_fields +=integer_form_string.format(Field=field.title(),
                                                              field=field, resource=resource)
            elif field_type == "Email":
                             db_rows += """
    {} = db.Column(db.String(250), nullable=False)""".format(field)
                             schema += """
    {} = fields.Email()""".format(field)
                             form_fields +=email_form_string.format(Field=field.title(),
                                                                      field=field, resource=resource)
            elif field_type == "URL":
                                     db_rows += """
    {} = db.Column(db.String(250), nullable=False)""".format(field)
                                     schema += """
    {} = fields.URL()""".format(field)
                                     form_fields +=url_form_string.format(Field=field.title(),
                                                                              field=field, resource=resource)
            elif field_type == "DateTime":
                     db_rows += """
    {} = db.Column(db.TIMESTAMP,server_default=db.func.current_timestamp(),nullable=False)""".format(field)
                     schema += """
    {} = fields.DateTime()""".format(field)
                     form_fields +=datetime_form_string.format(Field=field.title(),
                                                              field=field, resource=resource)
            elif field_type == "Date":
                     db_rows += """
    {} = db.Column(db.Date, nullable=False)""".format(field)
                     schema += """
    {} = fields.Date()""".format(field)
                     form_fields +=date_form_string.format(Field=field.title(),
                                                              field=field, resource=resource)

            elif field_type == "Decimal":
                     db_rows += """
    {} = db.Column(db.Numeric, nullable=False)""".format(field)
                     schema += """
    {} = fields.Decimal()""".format(field)
                     form_fields +=decimal_form_string.format(Field=field.title(),
                                                              field=field, resource=resource)

            elif field_type == "Text":
                     db_rows += """
    {} = db.Column(db.Text, nullable=False)""".format(field)
                     schema += """
    {} = fields.String()""".format(field)
                     form_fields +=text_form_string.format(Field=field.title(),
                                                              field=field, resource=resource)


            #models
            meta += """ '{}', """.format(field)
            init_args += """ {}, """.format(field)
            init_self_vars += """
        self.{field} = {field}""".format(field=field)
            #Views
            add_fields +="""
                                request.form['{}'],""".format(field)
            update_fields +="""
            {resource}.{field} = request.form['{field}']""".format(resource=resource, field=field)
            #_form.html
            form_args.append("""{resource}_{field} = ''""".format(resource=resource, field=field))
            field_table_headers += """ <th>{field}</th> """.format(field=field)
            index_fields += """<td>{{{{ result['{field}'] }}}}</td>""".format(field=field)
            update_form_args += """{resource}_{field} = {resource}.{field}, """.format(resource=resource,
                                                                                      field=field)


        #Generate files with the new fields
        module_dir = os.path.join('app',resources)

        try:
             os.mkdir(module_dir)
             try:
                 os.makedirs('{module_dir}/templates/{resources}'.format(module_dir=module_dir,
                                                                      resources=resources ))
                 generate_files(module_dir)
                 print('{} created successfully'.format(module_dir))
                 register_blueprints()
             except:
                 clean_up(module_dir)
                 raise

        except:
            raise

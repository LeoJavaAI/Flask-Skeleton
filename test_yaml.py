#!/usr/bin/env python
import yaml
import inflect

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


#Parse YAML file
with open( "scaffold/app/module.yaml" , "r") as yaml_file:

    yaml_data = yaml.load(yaml_file)

    for module, fields in yaml_data.items():
        db_rows = ""
        schema = ""
        meta = ""
        init_self_vars = ""
        init_args = ""


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


        #Generate Models
        resource, resources = make_plural(module)

        with open( "models.py" , "w") as new_file:
            with open( "scaffold/app/models.py" , "r") as old_file:
                        for line in old_file:
                            new_file.write(line.format(resource=resource, resources=resources,
                                                       Resources=resources.title(), db_rows=db_rows,
                                                        schema=schema, meta=meta, init_self_vars=init_self_vars,
                                                        init_args=init_args))

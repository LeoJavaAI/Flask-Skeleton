        elif field_type == "Integer":
                     db_rows += """
    {} = db.Column(db.Integer, nullable=False)""".format(field)
                     schema += """
    {} = fields.Integer(validate=not_blank)""".format(field)
                     form_fields +=integer_form_string.format(field=field, resource=resource)
        elif field_type == "Email":
                             db_rows += """
    {} = db.Column(db.String(250), nullable=False)""".format(field)
                             schema += """
    {} = fields.Email(validate=not_blank)""".format(field)
                             form_fields +=email_form_string.format(field=field, resource=resource)
        elif field_type == "URL":
                                     db_rows += """
    {} = db.Column(db.String(250), nullable=False)""".format(field)
                                     schema += """
    {} = fields.URL(validate=not_blank)""".format(field)
                                     form_fields +=url_form_string.format(field=field, resource=resource)
        elif field_type == "DateTime":
                     db_rows += """
    {} = db.Column(db.TIMESTAMP,server_default=db.func.current_timestamp(),nullable=False)""".format(field)
                     schema += """
    {} = fields.DateTime(validate=not_blank)""".format(field)
                     form_fields +=datetime_form_string.format(field=field, resource=resource)
        elif field_type == "Date":
                     db_rows += """
    {} = db.Column(db.Date, nullable=False)""".format(field)
                     schema += """
    {} = fields.Date(validate=not_blank)""".format(field)
                     form_fields +=date_form_string.format(field=field, resource=resource)

        elif field_type == "Decimal":
                     db_rows += """
    {} = db.Column(db.Decimal, nullable=False)""".format(field)
                     schema += """
    {} = fields.Decimal(validate=not_blank)""".format(field)
                     form_fields +=decimal_form_string.format(field=field, resource=resource)

        elif field_type == "Text":
                     db_rows += """
    {} = db.Column(db.Text, nullable=False)""".format(field)
                     schema += """
    {} = fields.String(validate=not_blank)""".format(field)
                     form_fields +=text_form_string.format(field=field, resource=resource)

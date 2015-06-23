integer_form_string ="""<label>{Field}
    <small>required</small><input type="number" name="{field}" value="{{{{ {resource}_{field} }}}}"  required/>
    </label> """


email_form_string = """<label>{Field}
    <small>required</small><input type="email" name="{field}" value="{{{{ {resource}_{field} }}}}"  required/>
    </label> """

url_form_string = """<label>{Field}
    <small>required</small><input type="url" name="{field}" value="{{{{ {resource}_{field} }}}}"  required/>
    </label> """

datetime_form_string = """<label>{Field}
    <small>required</small><input type="datetime" name="{field}" value="{{{{ {resource}_{field} }}}}"  required/>
    </label> """


date_form_string = """<label>{Field}
    <small>required</small><input type="date" name="{field}" value="{{{{ {resource}_{field} }}}}"  required/>
    </label> """

decimal_form_string = """<label>{Field}
    <small>required</small><input type="number" name="{field}" step="any" value="{{{{ {resource}_{field} }}}}"  required/>
    </label> """

text_form_string = """<label>{Field}
    <small>required</small><textarea type="text" name="{field}" rows="20" > {{{{ {resource}_{field} }}}}
    </textarea>
    </label> """

boolean_form_string = """<!-- START STATUS -->
      <div class="center row">
        {{% if form_name == 'Update' %}}

            <div class="small-6 columns">
            <label>{Field}</label>
              {{% if {resource}_{field} %}}
                <input type="radio" name="{field}" value="True"  checked/><label>True</label>
                <input type="radio" name="{field}" value="False"/><label>False</label>
              {{% else %}}
               <input type="radio" name="{field}" value="True"  /><label>True</label>
               <input type="radio" name="{field}" value="False" checked/><label>False</label>

              {{% endif %}}
                </div>
        <!-- For a new {resource}-->
        {{% else %}}

           <div class="small-6 columns">
             <label>{Field}</label>
               <input type="radio" name="{field}" value="True"  checked/><label>True</label>
               <input type="radio" name="{field}" value="False"/><label>False</label>
                 </div>
       {{% endif %}}
   </div>
           <!-- End STATUS -->"""

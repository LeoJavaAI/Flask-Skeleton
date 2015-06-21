

boolean_form_string = """<!-- START STATUS -->
        {{% if form_name == 'Update' %}}

            <div class="small-6 columns">
            <label>Status</label>
              {{% if {resource}.{field} %}}
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
             <label>Status</label>
               <input type="radio" name="{field}" value="True"  checked/><label>True</label>
               <input type="radio" name="{field}" value="False"/><label>False</label>
                 </div>
       {{% endif %}}

           <!-- End STATUS -- >"""

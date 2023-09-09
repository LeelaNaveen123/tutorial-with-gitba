from django import forms  

class EmpForm(forms.Form):  
    #Employee form 
    emp_identifier = forms.CharField(label="Enter employee Indentifier", max_length=50)  
    
from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpForm
from .models import EmployeeCompensation

# Create your views here.

def index(request):  
    #if reuest method is POST process the request and display pie chart 
    if request.method == "POST":  
        #Form to get the employee identifier
        form = EmpForm(request.POST)  
        #Check whether the form is valid or not
        if form.is_valid():  
            try:  
                #cpature the employee identifier
                emp_id = form.data['emp_identifier']            
                #get the employee details
                emp = EmployeeCompensation.objects.filter(emp_identifier=emp_id)
                context = {}
                #if employee is presented, display pie chart with employee details
                if emp:
                    total_salary=emp[0].total_salary
                    retirement = emp[0].retirement
                    health_dental=emp[0].health_dental
                    other_benefits=emp[0].other_benefits
                    total_benefits=emp[0].total_benefits
                    total_compensation=emp[0].total_compensation
                    avg_tsal = int((total_salary/total_compensation)*100)
                    avg_ret = int((retirement/total_compensation)*100)
                    avg_hd = int((health_dental/total_compensation)*100)
                    avg_oben = int((other_benefits/total_compensation)*100)
                    avg_ben = int((total_benefits/total_compensation)*100)
                    #prepare labels and data to display in piechart
                    labels = ['Benefits','Other Benefits','Health and Dental','Retirement','Total Salary']
                    values = [total_benefits,other_benefits,health_dental, retirement,total_salary]
                    avg = [avg_ben, avg_oben,avg_hd,avg_ret,avg_tsal]
                    context = {'labels':labels,'values':values, 'avg':avg}   
                else:
                    html = "<html><body><h3 style='color:red;'>%s is not present in the system.</h3></body></html>" % emp_id
                    return HttpResponse(html)
                return render(request, 'emp_details.html', context)
            except Exception as e:  
                print('Caught the exception:',e)
    else:  
        #Display Employee form
        emp = EmpForm()  
        return render(request,'index.html',{'form':emp})  
    

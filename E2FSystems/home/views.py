import os
from django.shortcuts import render
from django.db.models import Q
from home.models import Admin, ContactInfo, Program, UserSearch

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    return render(request, 'result.html')

def admin_login(request):
    if request.method == 'GET':
        return render(request, 'admin_login.html')
    else:
        username_=request.POST["username"]
        password_=request.POST["password"]

        try:
            user=Admin.objects.get(username=username_)
        except:
            fail_msg="Username does not exists"
            return render(request,'admin_login.html',{'fail_msg':fail_msg})
        if user is not None and user.password==password_:
            return render(request,'add_program.html')
        else:
            fail_msg="Password is incorrect"
            return render(request,'admin_login.html',{'fail_msg':fail_msg})

def search(request):

    if request.method == 'POST':

        program_type_s = request.POST.get('program_type')
        company_sector_s=request.POST["company_sector"]
        postal_code_s=request.POST["postal_code"]
        employee_count_s=request.POST["employee_count"]
        electricity_budget_s=request.POST["electricity_budget"]
        natural_gas_budget_s=request.POST["natural_gas_budget"]
        company_name_s=request.POST["company_name"]
        company_contact_s=request.POST["company_contact"]


        Program.objects.all()

        if program_type_s=="electricity":
            type_s="SaveOnEnergy"
        else:
            type_s="ENBRIDGE GAS"

        programs = Program.objects.filter(

            Q(funding_stream__contains=type_s)|
            Q(funding_stream__contains=type_s)|

            Q(eligibility__contains=company_sector_s) |
            Q(project_type__contains=company_sector_s) |

            Q(eligibility__contains=employee_count_s) | 

            Q(eligibility__contains=electricity_budget_s) | 

            Q(eligibility__contains=natural_gas_budget_s)
        )

        
        print(programs)

        ##saving search for future 
        new_search=UserSearch(

            funding_stream=program_type_s,
            company_sector=company_sector_s,
            postal_code=postal_code_s,
            employee_count=employee_count_s,
            estimated_annual_electricity_budget=electricity_budget_s,
            estimated_annual_natural_gas_budget=natural_gas_budget_s,
            company_name=company_name_s,
            company_contact=company_contact_s
            )

        new_search.save()
        

        return render(request,'result.html',{"programs":programs})

def add_program(request):

    if request.method == 'GET':
        print("inget")
        return render(request,'add_program.html')
    else:
        
        ## getting data from user
        program_name_user=request.POST["program_name"]
        eligibility_user=request.POST["eligibility"]
        link_user=request.POST["link"]
        project_type_user=request.POST["project_type"]
        uploaded_file=request.FILES["supporting_docs"]
        description_user=request.POST["description"]
        funding_stream_user=request.POST["funding_stream"]

        
        upload_dir = f'./uploads/{program_name_user}/'
        os.makedirs(upload_dir, exist_ok=True)

        with open(os.path.join(upload_dir, uploaded_file.name), 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)


        ##adding data to database
        new_program=Program(
            program_name=program_name_user,
            eligibility=eligibility_user,
            link=link_user,
            project_type=project_type_user,
            supporting_docs=upload_dir+uploaded_file.name,
            description=description_user,
            funding_stream=funding_stream_user
            )

        new_program.save()
        add_success="Program Added Successfully!"
        return render(request,'add_program.html',{'success_msg':add_success})

def contact_us(request):
    if request.method == "GET":
        return render(request,'contact.html')
    else:
        ## getting data from user
        contact_email_c=request.POST["contact_email"]
        contact_company_c=request.POST["contact_company"]
        additional_info_c=request.POST["additional_info"]

        new_inquiry=ContactInfo(
            contact_email=contact_email_c,
            contact_company=contact_company_c,
            additional_info=additional_info_c
            )

        new_inquiry.save()
        add_success="Request Sent Successfully!"
        return render(request,'contact.html',{'success_msg':add_success})
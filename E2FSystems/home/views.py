import os
from django.shortcuts import render

from home.models import Admin, Program

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

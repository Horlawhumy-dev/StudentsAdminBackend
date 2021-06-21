from django.shortcuts import render,redirect
from .models import StudentForm

def Form(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        address= request.POST['address']
        dob = request.POST['dob']
        reg = request.POST['regno']
        phone = request.POST['phone']
        pic = request.FILES['img']
        sex = request.POST['sex']
        status = request.POST['status']

        student = StudentForm(
            firstname=fname,
            lastname=lname,
            email=email,
            address=address,
            date_of_birth=dob,
            reg_no=reg,
            phone_no=phone,
            picture=pic,
            sex=sex,
            status=status
        )
        student.save()
        return redirect('/')
    
    return render(request, 'form/form.html')
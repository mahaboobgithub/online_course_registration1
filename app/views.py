from django.shortcuts import render, redirect

from django.contrib import messages
from app.forms import Courseform,StudentRegiserform
from app.models import Coursemodel,Studentmodel


def home_page(request):
    return render(request,"home_page.html")


def home(request):
    return render(request, 'home.html')


def admin_login_check(request):
    uname = request.POST.get('t1')
    upass = request.POST.get('t2')

    if uname == 'mahaboob' and upass == "mahaboob":
        return redirect("admin_page")
    else:

        messages.error(request, 'invalid_user')
        return redirect('admin_login')


def admin_page(request):
    return render(request, "admin_page.html")


def admin_schedule_class(request):
    return render(request,"admin_schedule_class.html",{"form":Courseform()})


def save_scheduled_class(request):
    coursedata=Courseform(request.POST)
    if coursedata.is_valid():
        coursedata.save()
        messages.success(request,"Data Saved Successfully")
        return redirect("admin_schedule_class")
    else:
        messages.error(request,"Enter Correct Details")
        return render(request,"admin_schedule_class.html",{"form":coursedata})


def admin_view_class(request):
    coursedetails=Coursemodel.objects.all()
    a={"object_list":coursedetails}
    return render(request, "admin_view_scheduled.html",a)


def Student_page(request):
    c_details=Coursemodel.objects.all()
    b={"object_data":c_details}
    return render(request,"student_page.html",b)


def student_register(request):
    return render(request,'student_register.html',{"form":StudentRegiserform})


def studentform_check(request):
    std_details=StudentRegiserform(request.POST)
    if std_details.is_valid():
        std_details.save()
        messages.success(request,"Your Registration is Successful.You can login now")
        return redirect("student_register")
    else:
        messages.error(request,"Enter correct details")
        return render(request,"student_register.html",{"form":std_details})


def student_login(request):
    return render(request,"student_login.html")


def student_login_check(request):
    uname=request.POST.get("s1")

    upass=request.POST.get("s2")
    print(uname,upass)

    a=Studentmodel.objects.get(emailid=uname)
    #a = Studentmodel.objects.get(emailid=uname)
    print(a)

    if uname == a.emailid and upass == a.password:
        b={"obj":a}
        return render(request,'welcome_student.html',b)
    else:
       messages.error(request,"Invalid Username or Password")
       return redirect("student_login.html")



def welcome_student(request):
    return render(request,"welcome_student.html")


def enroll_course(request):
    course_details=Coursemodel.objects.all()
    a={"object_data":course_details}
    return render(request,"enroll_course.html",a)


def enroled_courses(request):
    cno=request.POST.get("s1")
    courses = request.POST.getlist("s2")
    a=Studentmodel.objects.get(contact_no=cno)

    #if cno == a.contact_no:
    sm=Studentmodel.objects.get(contact_no=cno)
    sm.student_course.set(courses)
    messages.success(request,"Courses Enrolled Successfully")
    return redirect("enroll_course")
    # else:
    #     messages.error(request,"Enter Correct Mobile No.")
    #     return redirect("enroll_course")


# a=Studentmodel(contact_no=cno)
    # a.save()
def view_enrolled(request):
    return render(request,"view_enrolled.html")


def enrolled_list(request):
    cno=request.POST.get("s1")
    sm = Studentmodel.objects.get(contact_no=cno)
    courses=sm.student_course.all()
    c={'obj':courses}



    return render(request,"enrolled_list.html",c)


def cancel_course(request):
    # sm = Studentmodel.student_course.objects.all()
    #
    #
    # a = {'data': sm}



    return render(request,"cancel_course.html")


def cancel_course_list(request):
    cno = request.POST.get("s1")
    #courses = request.POST.get("s2")
    sm = Studentmodel.objects.get(contact_no=cno)

    courses = sm.student_course.all()
    a = {'data': courses}



    return render(request,"cancel_course_list.html",a)


def latest_course_list(request):
    cno = request.POST.get("s1")
    courses = request.POST.get("s2")

    sm = Studentmodel.objects.get(contact_no=cno)

    
    sm.student_course.remove(courses)



    new=Studentmodel.objects.get(contact_no=cno)
    b=new.student_course.all()
    d={"data":b}

    return render(request,"latest_course_list.html",d)


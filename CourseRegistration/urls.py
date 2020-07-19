"""CourseRegistration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),path('home_page/',views. home_page,name="home_page"),
    path("home/",views.home,name="home"),
    path("admin_login_check/",views.admin_login_check,name="admin_login_check"),
    path("admin_page/",views.admin_page,name="admin_page"),
    path('admin_scedule_class/',views.admin_schedule_class,name='admin_schedule_class'),
    path('save_scheduled_class/',views.save_scheduled_class,name="save_scheduled_class"),
    path("admin_view_class/",views.admin_view_class,name="admin_view_class"),
    path("student_Page/",views.Student_page,name="student_page"),
    path("student_register/",views.student_register,name="student_register"),
    path("studentform_check",views.studentform_check,name="studentform_check"),
    path("student_login/",views.student_login,name="student_login"),
    path("student_login_check/",views.student_login_check,name="student_login_check"),
    path("welcome_student/",views.welcome_student,name="welcome_student"),
    path("enroll_course/",views.enroll_course,name="enroll_course"),
    path("enroled_courses",views.enroled_courses,name="enroled_courses"),
    path("view_enrolled",views.view_enrolled,name="view_enrolled"),
    path("enrolled_list",views.enrolled_list,name="enrolled_list"),
    path("cancel_course",views.cancel_course,name="cancel_course"),
    path("cancel_course_list",views.cancel_course_list,name='cancel_course_list'),
    path("latest_course_list",views.latest_course_list,name="latest_course_list")
]
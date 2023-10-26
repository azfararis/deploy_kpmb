from django.shortcuts import render
from Registration.models import Course,Student
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request,'index.html')

def new_course(request):
    if request.method =='POST':
        c_code = request.POST['code']
        c_desc = request.POST['desc']
        data = Course(code=c_code,description=c_desc)
        data.save()
        return render(request, 'new_course.html',{'message':'Data Save'})
    else:
        return render(request, 'new_course.html')
    
def course(request):
    allcourse=Course.objects.all()
    dict={
        'allcourse':allcourse
    }
    return render (request,'course.html',dict)

def search_course(request):
    if request.method == 'GET':
        data = Course.objects.filter(code= request.GET.get('c_code'))
        dict = {
            'data':data
        }
        return render(request, 'search_course.html',dict)
    else:
        return render(request,'search_course.html')
    
def update_course(request,code):
    data=Course.objects.get(code=code)
    dict = {
        'data':data

    }

    return render (request, "update_course.html", dict)

def save_update_course(request,code):
    c_desc= request.POST['desc']
    data = Course.objects.get(code=code)
    data.desc = c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))

def delete_course(request,code):
    data = Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse("course"))



#STUDENT

def new_student(request):
    allcourse=Course.objects.all()
    if request.method == 'POST':
        #get the data from html page (New Student)
        Id = request.POST['s_id']
        Name=request.POST['s_name']
        Address=request.POST['s_add']
        Phone=request.POST['s_phone']
        S_Code=request.POST['s_course']

        data_course= Course.objects.get(code=S_Code)

        #assign value data
        data=Student(id=Id, name=Name, address=Address, phone=Phone, course_code=data_course)

        #save data
        data.save()

        dict={
            'allcourse':allcourse,
            'message' : "Data Save"
        }

    else:   
        dict = {
        'allcourse':allcourse
        
        }
    return render(request,'new_student.html',dict)




def searchbystudent(request):
    studentData = ''
    courseData = ''
    dict = {}

    if request.method == 'POST':
        id = request.POST['id']
        try:
            studentData = Student.objects.get(id=id)
            courseData = Course.objects.get(code=studentData.course_code_id)

            dict = {
                'studentData': studentData,
                'courseData': courseData
            }
        except Student.DoesNotExist:
            dict['data_exists'] = False

    return render(request, "searchbystudent.html", dict)


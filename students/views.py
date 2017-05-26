from django.shortcuts import render
from .models import Student
from courses.models import Course

def list_view(request):
    if 'course_id' in request.GET:
        course = Course.objects.get(pk=request.GET['course_id'])
        students = Student.objects.filter(courses=course)
    else:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'students/detail.html', {'student': student})

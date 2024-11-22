from django.shortcuts import render,redirect,get_object_or_404
from organization.models import Student
from .forms import StudentForm
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
#from .serializers import StudentSerializer
from django.urls import reverse,reverse_lazy
from django.db.models import Min,Max,Avg
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
# from rest_framework.parsers import JSONParser
# Create your views here.
# def Student_list(request):#get api
#     students = Student.objects.all()
#     #fetch students age > 18
#     student_over_18=Student.objects.filter(age__gt=18)
#     #students age<20
#     student_under_20=Student.objects.filter(age__lt=20)
#     #get min age student
#     youngest_student=Student.objects.all().aggregate(min_age=Min('age'))
#     #get max age student
#     oldest_student=Student.objects.all().aggregate(max_age=Max('age'))
#     #avg of all students age
#     average_age=Student.objects.all().aggregate(average_age=Avg('age'))
#     #total age of students
#     total_students=Student.objects.count()
#     #order the stds age in ascending order
#     student_order_by_age=Student.objects.all().order_by('age')
#     #order by descending
#     student_order_by_dec=Student.objects.all().order_by('-age')
#     #fetch distict ages of student
#     distinct_ages=Student.objects.values('age').distinct()
#     #to perform muliple aggregate fun
#     aggregates=Student.objects.aggregate(
#         min_age=Min('age'),
#         max_age=Max('age'),
#         average_age=Avg('age')

#     )
#     context={
#         "students":students,
#         "student_over_18":student_over_18,
#         "student_under_20":student_under_20,
#         "youngest_student":youngest_student,
#         "oldest_student":oldest_student,
#         "average_age":average_age,
#         "total_students":total_students,
#         "student_order_by_age":student_order_by_age,
#         "student_order_by_dec":student_order_by_dec,
#         "distinct_ages":distinct_ages,
        
#     }
#     return render(request,"student_list.html",context)

# #create api
# # def StudentCreate(request):
# #     if request.method == 'POST':
# #         form = StudentForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #         return redirect("student_list")
# #     else:
# #         form = StudentForm()
# #     return JsonResponse(form.data)

# def StudentCreate(request):
#     if request.method=="POST":
#         form=StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect("student_list")
#     else:
#         form=StudentForm()
#     return render(request,"student_form.html",{'form':form})
# #update
# def StudentUpdate(request,id):
#     student =get_object_or_404(Student,id=id)
#     if request.method=="POST":
#         form=StudentForm(request.POST,instance=student)
#         if form.is_valid():
#             form.save()
#         redirect("student_list")
#     else:
#         form=StudentForm(instance=student)
#     return render(request,"student_form.html",{'form':form})

# #Delete
# def StudentDelete(request,id):
#     student = get_object_or_404(Student,id=id)
#     if request.method=="POST":
#         student.delete()
#         return redirect("student_list")
#     return render(request,"student_delete.html",{"student":student})


#class based views
class Student_list(ListView):
    model = Student
    template_name = "student_list.html"
    context_object_name = "students"

class StudentCreate(CreateView):
    model=Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url=reverse_lazy("student_list")

class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student_list")

class StudentDelete(DeleteView):
    model = Student
    template_name = "student_delete.html"
    success_url = reverse_lazy("student_list")
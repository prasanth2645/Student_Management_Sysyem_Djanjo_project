from django.urls import path
# from . import views

from .views import Student_list,StudentCreate,StudentUpdate,StudentDelete

urlpatterns=[
    path("studentlist/",Student_list.as_view(),name="student_list"),
    path("studentcreate/",StudentCreate.as_view(),name="student_create"),
    path("studentupdate/<int:pk>/",StudentUpdate.as_view(),name="student_update"),
    path("studentdel/<int:pk>/",StudentDelete.as_view(),name="student_delete")
    
]

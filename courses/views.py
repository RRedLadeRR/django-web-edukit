from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .mixins import OwnerCourseEditMixin, OwnerCourseMixin
from .models import Course

# Create your views here.

class HomeView(TemplateView):
    template_name = "base.html"

class ManageCourseListView(OwnerCourseMixin,ListView):
    model = Course
    template_name = "courses/manage/course/list.html"

class CourseCreateView(OwnerCourseEditMixin, CreateView):
    pass

class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    pass

class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = "courses/manage/course/delete.html"
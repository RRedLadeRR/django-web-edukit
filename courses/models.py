from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Specialization"
        verbose_name_plural = "Specializations"
        ordering = ["title"]

    def __str__(self):
        return self.title
    
class Course(models.Model):
    owner = models.ForeignKey(User, related_name="courses_created", on_delete=models.CASCADE, verbose_name="Teacher")
    subject = models.ForeignKey(Subject, related_name="courses", on_delete=models.CASCADE, verbose_name="Subject")
    title = models.CharField(max_length=500, verbose_name="Title")
    slug = models.SlugField(max_length=500, unique=True)
    overview = models.TextField(verbose_name="Description")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ["-created"]

    def __str__(self):
        return self.title
    
class Module(models.Model):
    course = models.ForeignKey(Course, related_name="Modules", on_delete=models.CASCADE, verbose_name="Course")
    title = models.CharField(max_length=500, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    
    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.title
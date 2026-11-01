from django.db import models

# Create your models here.

# Create your models here.
class Student(models.Model):
    student_Id = models.CharField(max_length=100)
    student_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image',default='noimage.jpg')
    email = models.EmailField(max_length=100)
    Mobile_Number = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=60)
    gpa = models.CharField(max_length=60)
    pass_year = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name
from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)

    def __str__(self):
        return self.firstName

class ContactInfo(models.Model):
    city=models.CharField(max_length=30)
    phone=models.IntegerField()
    sid=models.OneToOneField(StudentInfo,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.phone}"


from django.db import models

class StudentForm(models.Model):
    class Sex(models.TextChoices):
        sex = 'CS', 'Choose sex'
        Male = 'M', 'male'
        Female = 'F', 'female'
        
    class Status(models.TextChoices):
        status = 'CS', 'Choose Status'
        UNDERGRADUATE = 'UG', 'undergraduate'
        POSTGRADUATE = 'PG', 'postgraduate'

    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=200)
    date_of_birth = models.CharField(max_length=200)
    reg_no = models.CharField(max_length=200, unique=True)
    phone_no = models.CharField(max_length=200, unique=True)
    picture = models.ImageField()
    sex = models.CharField(max_length=10, choices=Sex.choices, default=Sex.sex)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.status)

    def __str__(self):
        return self.firstname + " " + self.lastname

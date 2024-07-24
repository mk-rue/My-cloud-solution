from django.db import models # type: ignore

class Company(models.Model):
    name = models.CharField(max_length=255)
    registration_date = models.DateField()
    registration_number = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    contact_person = models.CharField(max_length=255)
    departments = models.TextField()  # or use a ManyToManyField to a Department model
    number_of_employees = models.IntegerField()
    contact_phone = models.CharField(max_length=20)
    email = models.EmailField()

from company.models import Company # type: ignore

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    date_started = models.DateField()
    date_left = models.DateField(blank=True, null=True)
    duties = models.TextField()


    def __str__(self):

        return self.name

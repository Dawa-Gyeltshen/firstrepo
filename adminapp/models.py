from django.db import models

# Create your models here.
class EmployementDetails(models.Model):
	empid=models.IntegerField(primary_key=True)
	empname=models.CharField(max_length=20)
	empdesignation=models.CharField(max_length=25)
	empdepartment=models.CharField(max_length=50)
	Empage=models.IntegerField()
	empbloodgroup=models.CharField(max_length=50)
	empemailid=models.CharField(unique=True,max_length=50)

	class Meta:
		verbose_name="EmployementDetails"
		verbose_name_plural="EmployementDetailss"

def __str__(self):
	return self.empname +" "+ str(self.empid) +" "+ self.empdesignation +" "+ self.empdepartment +" "+ str(self.Empage) +" "+ self.empbloodgroup

from django.contrib import admin
from adminapp.models import EmployementDetails


# Register your models here.
class EmployementDetailsAdmin(admin.ModelAdmin):

	list_display=('empname','empid','empdesignation','empdepartment','Empage','empbloodgroup')

admin.site.register(EmployementDetails,EmployementDetailsAdmin)



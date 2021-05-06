from django.contrib import admin
from .models import Parent, Student, Phone


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ['parent_name', 'created', 'modified', 'is_live']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'created', 'modified', 'is_live']


@admin.register(Phone)
class TelephoneAdmin(admin.ModelAdmin):
    list_display = ['mobile_phone', 'landline_phone', 'created', 'modified', 'is_live']

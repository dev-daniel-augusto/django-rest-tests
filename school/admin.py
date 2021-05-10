from django.contrib import admin
from .models import (
                    Parent,
                    Student,
                    Phone,
                    Subject,
                    Teacher,
                    )


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ['parent_name', 'created', 'modified', 'is_live']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'created', 'modified', 'is_live', 'get_parent_name']

    def get_parent_name(self, obj):
        return ', '.join([parent.parent_name for parent in obj.parent_name.all()])


@admin.register(Phone)
class TelephoneAdmin(admin.ModelAdmin):
    list_display = ['mobile_phone', 'landline_phone', 'created', 'modified', 'is_live']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject', 'created', 'modified', 'is_live']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'created', 'modified', 'is_live']

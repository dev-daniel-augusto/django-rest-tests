from django.db import models
from phone_field import PhoneField


class Core(models.Model):
    created = models.DateTimeField('Created', auto_now_add=True)
    modified = models.DateTimeField('Last Time Modified', auto_now=True)
    is_live = models.BooleanField('Is Active?', default=True)

    class Meta:
        abstract = True


class Parent(Core):
    parent_name = models.CharField('Parent Full Name', max_length=250, help_text='Max digits: 250')
    email = models.EmailField('E-mail', max_length=200, help_text='Max digits: 200')

    class Meta:
        verbose_name = 'Parent'
        verbose_name_plural = 'Parents'

    def __str__(self):
        return self.parent_name


class Phone(Core):
    parents = models.ManyToManyField(Parent)
    mobile_phone = PhoneField('Mobile Phone', blank=True, help_text='Phone number for contact')
    landline_phone = PhoneField('Landline Phone', blank=True, help_text='Phone number for contact')

    class Meta:
        verbose_name = 'Telephone'
        verbose_name_plural = 'Telephones'

    def __str__(self):
        return f'{self.mobile_phone}'


class Student(Core):
    parent_name = models.ManyToManyField(Parent)
    student_name = models.CharField('Student Full Name', max_length=250, help_text='Max digits: 250')
    email = models.EmailField('E-mail', max_length=200, help_text='Max digits: 200')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.student_name

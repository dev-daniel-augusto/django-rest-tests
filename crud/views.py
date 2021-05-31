from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from school.models import (
                    Parent,
                    Phone,
                    Student,
                    Subject,
                    Teacher,
                    )


class ParentView(LoginRequiredMixin, ListView):
    models = Parent
    template_name = 'parents.html'
    queryset = Parent.objects.order_by('id').all()
    paginate_by = 7
    context_object_name = 'parents'


class CreateParentView(LoginRequiredMixin, CreateView):
    model = Parent
    template_name = 'parent_form.html'
    fields = [
        'parent_name',
        'email'
    ]
    success_url = reverse_lazy('parents')


class UpdateParentView(LoginRequiredMixin, UpdateView):
    model = Parent
    template_name = 'parent_update.html'
    fields = [
        'parent_name',
        'email'
    ]
    success_url = reverse_lazy('parents')


class DeleteParentView(LoginRequiredMixin, DeleteView):
    model = Parent
    template_name = 'parent_delete.html'
    success_url = reverse_lazy('parents')


class PhoneView(LoginRequiredMixin, ListView):
    models = Phone
    template_name = 'phones.html'
    queryset = Phone.objects.all()
    context_object_name = 'phones'


class CreatePhoneView(LoginRequiredMixin, CreateView):
    model = Phone
    template_name = 'phone_form.html'
    fields = [
        'parent_name',
        'mobile_phone',
        'landline_phone'
    ]
    success_url = reverse_lazy('phones')


class UpdatePhoneView(LoginRequiredMixin, UpdateView):
    model = Phone
    template_name = 'phone_update.html'
    fields = [
        'parent_name',
        'mobile_phone',
        'landline_phone'
    ]
    success_url = reverse_lazy('phones')


class DeletePhoneView(LoginRequiredMixin, DeleteView):
    model = Phone
    template_name = 'phone_delete.html'
    success_url = reverse_lazy('phones')


class StudentView(LoginRequiredMixin, ListView):
    models = Student
    template_name = 'students.html'
    queryset = Student.objects.all()
    context_object_name = 'students'


class CreateStudentView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'student_form.html'
    fields = [
        'parent_name',
        'student_name',
        'email'
    ]
    success_url = reverse_lazy('students')


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'student_update.html'
    fields = [
        'parent_name',
        'student_name',
        'email'
    ]
    success_url = reverse_lazy('students')


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'student_delete.html'
    success_url = reverse_lazy('students')


class SubjectListView(LoginRequiredMixin, ListView):
    models = Subject
    template_name = 'subjects.html'
    queryset = Subject.objects.all()
    context_object_name = 'subjects'


class CreateSubjectView(LoginRequiredMixin, CreateView):
    model = Subject
    template_name = 'subject_form.html'
    fields = [
        'subject'
    ]
    success_url = reverse_lazy('subjects')


class UpdateSubjectView(LoginRequiredMixin, UpdateView):
    model = Subject
    template_name = 'subject_update.html'
    fields = [
        'subject'
    ]
    success_url = reverse_lazy('subjects')


class DeleteSubjectView(LoginRequiredMixin, DeleteView):
    model = Subject
    template_name = 'subject_delete.html'
    success_url = reverse_lazy('subjects')


class TeacherView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teachers.html'
    queryset = Teacher.objects.all()
    context_object_name = 'teachers'


class CreateTeacherView(LoginRequiredMixin, CreateView):
    model = Teacher
    template_name = 'teacher_form.html'
    fields = [
        'name',
        'subject'
    ]
    success_url = reverse_lazy('teachers')


class UpdateTeacherView(LoginRequiredMixin, UpdateView):
    model = Teacher
    template_name = 'teacher_update.html'
    fields = [
        'name',
        'subject'
    ]
    success_url = reverse_lazy('teachers')


class DeleteTeacherView(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'teacher_delete.html'
    success_url = reverse_lazy('teachers')
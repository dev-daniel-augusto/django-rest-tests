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


class IndexView(LoginRequiredMixin, ListView):
    models = Parent
    template_name = 'index.html'
    queryset = Parent.objects.order_by('id').all()
    context_object_name = 'parents'


class CreateParentView(LoginRequiredMixin, CreateView):
    model = Parent
    template_name = 'parent_form.html'
    fields = [
        'parent_name',
        'email',
    ]


class UpdateParentView(LoginRequiredMixin, UpdateView):
    model = Parent
    template_name = 'parent_update.html'
    fields = [
        'parent_name',
        'email'
    ]
    success_url = reverse_lazy('index')


class DeleteParentView(LoginRequiredMixin, DeleteView):
    model = Parent
    template_name = 'parent_delete.html'
    success_url = reverse_lazy('index')

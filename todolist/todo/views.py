
from django.shortcuts import render, get_object_or_404, reverse
from django.template.context_processors import request

from .models import Uzduotis
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.contrib.auth.forms import User


def uzduotis(request, uzduotis_id):
    uzduotis = get_object_or_404(Uzduotis, pk=uzduotis_id)
    context = {
        'uzduotis': uzduotis
    }
    return render(request, 'uzduotisnew.html', {'uzduotis': uzduotis})


class UzduotisView(generic.ListView):
    model = Uzduotis
    template_name = 'index.html'
    context_object_name = 'uzduotys'


class UzduotisCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Uzduotis
    fields = ['title', 'body', 'data']
    template_name = 'indexnew.html'
    success_url = "/todolist/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class UzduotisEditView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Uzduotis
    fields = ['title', 'body', 'data']
    template_name = 'indexedit.html'
    context_object_name = 'uzduotis'

    def get_success_url(self):
        return reverse('uzduotis', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class UzduotisDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Uzduotis

    template_name = "indexdelete.html"

    def test_func(self):
        uzduotis = Uzduotis.objects.get(pk=self.kwargs['pk'])
        return self.request.user == uzduotis.user

    def get_success_url(self):
        return reverse('uzduotis', kwargs={'pk': self.kwargs['pk']})


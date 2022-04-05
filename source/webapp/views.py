from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from webapp.models import Citation
from webapp.forms import CitationForm
from django.urls import reverse_lazy, reverse

class IndexView(PermissionRequiredMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'citations'
    model = Citation


class CitationCreateView(CreateView):
    model = Citation
    form_class = CitationForm
    template_name = "citation_add.html"

    def form_valid(self, form):
        response = super(CitationCreateView, self).form_valid(form)
        return response

    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.object.pk})



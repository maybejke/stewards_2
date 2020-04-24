from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView

from mainapp.models import Vacancy, Documents
from mainapp.forms import SendContactsForm


# Create your views here.

class IndexView(TemplateView):
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutView(TemplateView):
    template_name = 'mainapp/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContactsView(TemplateView):
    template_name = 'mainapp/contact.html'
    form = SendContactsForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context


class DocumentsView(TemplateView):
    template_name = 'mainapp/documents.html'
    docs = Documents.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['docs'] = self.docs
        return context


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'mainapp/vacancy_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['vacancy'] = Vacancy.objects.all()
        return self.render_to_response(context)

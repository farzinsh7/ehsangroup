from django.shortcuts import render
from django.views.generic import ListView
from .models import SiteInformation, HomeData
from industries.models import Industry
from company.models import Company

# Create your views here.
class Index(ListView):
    model = HomeData
    template_name = 'index.html'
    context_object_name = "home"
    queryset = HomeData.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['industry'] = Industry.objects.filter(status='p')[:4]
        context['company'] = Company.objects.filter(status='p')
        return context


class SiteHeaderView(ListView):
    model = SiteInformation
    template_name = 'base/shared/header.html'
    context_object_name = 'info'
    queryset = SiteInformation.objects.first()


class SiteFooterView(ListView):
    model = SiteInformation
    template_name = 'base/shared/footer.html'
    context_object_name = 'info'
    queryset = SiteInformation.objects.first()
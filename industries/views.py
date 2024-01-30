from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Industry


# Create your views here.
class IndustryListView(ListView):
    queryset = Industry.objects.filter(status="p").order_by('-publish')
    model = Industry
    template_name = 'industry_list.html'
    context_object_name = 'industry'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest'] = Industry.objects.filter(status="p").order_by('-publish')[:5]
        return context

class IndustryDetailView(DetailView):
    model = Industry
    context_object_name = 'industry'
    queryset = Industry.objects.filter(status='p')
    template_name = 'industry_detail.html'
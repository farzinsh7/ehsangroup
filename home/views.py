from django.views.generic import ListView
from .models import SiteInformation, HomeData
from industries.models import Industry
from company.models import Company
from news.models import News
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


# Create your views here.
class Index(ListView):
    model = HomeData
    template_name = 'index.html'
    context_object_name = "home"
    
    def get_queryset(self):
        return HomeData.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['industry'] = Industry.objects.filter(status='p').order_by('-publish')[:4]
        context['company'] = Company.objects.filter(status='p').order_by("-publish")
        context['news'] = News.objects.published()[:3]
        return context


@method_decorator(cache_page(60 * 15), name='dispatch')
class SiteHeaderView(ListView):
    model = SiteInformation
    template_name = 'base/shared/header.html'
    context_object_name = 'info'
    
    def get_queryset(self):
        return SiteInformation.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['industry'] = Industry.objects.filter(status='p').order_by('-publish')[:4]
        return context


@method_decorator(cache_page(60 * 15), name='dispatch')
class SiteFooterView(ListView):
    model = SiteInformation
    template_name = 'base/shared/footer.html'
    context_object_name = 'info'
    
    def get_queryset(self):
        return SiteInformation.objects.first()

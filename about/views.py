from django.views.generic import ListView
from .models import AboutCompany

# Create your views here.
class AboutView(ListView):
    model = AboutCompany
    template_name = 'about.html'
    context_object_name = "about"
    
    def get_queryset(self):
        return AboutCompany.objects.first()

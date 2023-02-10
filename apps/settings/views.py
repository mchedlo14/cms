from django.shortcuts import render
from django.views import View
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import UpdateView,DeleteView
from apps.settings.models import Web_parametres
from apps.settings.forms import WebparaForms



class EditWebParametresView(View):
    def get(self, request, *args, **kwargs):
        settings = Web_parametres.objects.get()
        settings_form = WebparaForms(instance=settings)
        context = {
            'settings_form' : settings_form,
            'settings':settings,
        }
        return render(request, "dashboards/settings/web_settings.html", context)

    def post(self, request, *args, **kwargs):

        settings = Web_parametres.objects.get()
        settings_form = WebparaForms(request.POST,request.FILES,instance=settings)
        
        context = {
            'settings_form' : settings_form,
            'settings':settings,
        }
        if settings_form.is_valid():
            settings_form.save()
            return render(request, "dashboards/settings/web_settings.html",context)



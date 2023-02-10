from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from apps.menus.models import Menu

class MenuFrontView(View):
    def get_menu(self,request):

        Menu_Item = Menu.objects.all()
        context = {
            "Menu_Item": Menu_Item
        }

        return render(request,"front/header.html",context)




class homepage(TemplateView):

    pass


front_homepage = homepage.as_view(template_name="front/pages/index.html")
front_service = homepage.as_view(template_name="front/pages/Servicetype_1.html")
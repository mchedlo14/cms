from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from apps.menus.forms import MenuForm
from apps.menus.models import Menu


class MenuCreateView(View):
    def get(self, request, *args, **kwargs):
        form = MenuForm()
        context = {
            'form': form,
        }
        return render(request, 'Oreon_Components/menus/menu_create.html', context)

    def post(self, request, *args, **kwargs):
        form = MenuForm(request.POST, request.FILES)
        error_message = "Form Is Not Valid,Please Try Again!"
        context = {
            'form': form,
            'error': error_message,
        }
        if form.is_valid():
            form.save()
            return redirect('menu-list')
        return render(request, 'Oreon_Components/menus/menu_create.html', context)


class MenuListView(View):
    def get(self, request, *args, **kwargs):
        menus = Menu.objects.all()
        context = {
            'menus': menus,
        }
        return render(request, 'Oreon_Components/menus/menu_list.html', context)


class EditMenuView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        menu = Menu.objects.get(id=id)
        form = MenuForm(instance=menu)

        context = {
            'form': form
        }

        return render(request, 'Oreon_Components/menus/menu_edit.html', context)

    def post(self, request, *args, **kwargs):
        error_message = "Form Is Not Valid,Please Try Again"
        menu_id = kwargs.get('id')
        menu = Menu.objects.get(id=menu_id)
        form = MenuForm(request.POST, instance=menu)

        context = {
            'form': form,
            'error': error_message,
        }
        if form.is_valid():
            form.save()
            return redirect('menu-list')
        return render(request, 'Oreon_Components/menus/menu_edit.html', context)


class MenuDeleteView(View):
    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')
        menu = get_object_or_404(Menu, id=id)
        menu.delete()
        return redirect('menu-list')

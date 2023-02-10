from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from apps.services.forms import ServiceForm, CategoryForm
from apps.services.models import Service, Category


class ServiceCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ServiceForm()
        context = {
            'form': form,
        }
        return render(request, 'Oreon_Components/services/service_create.html', context)

    def post(self, request, *args, **kwargs):
        form = ServiceForm(request.POST, request.FILES)
        error_message = "Form Is Not Valid,Please Try Again!"
        context = {
            'form': form,
            'error': error_message,
        }
        if form.is_valid():
            form.save()
            return redirect('service-list')
        return render(request, 'Oreon_Components/services/service_create.html', context)


class ServiceListView(View):
    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        context = {
            'services': services,
        }
        return render(request, 'Oreon_Components/services/service_list.html', context)


class EditServiceView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        service = Service.objects.get(id=id)
        form = ServiceForm(instance=service)

        context = {
            'form': form
        }

        return render(request, 'Oreon_Components/services/service_edit.html', context)

    def post(self, request, *args, **kwargs):
        error_message = "Form Is Not Valid,Please Try Again!"
        service_id = kwargs.get('id')
        service = Service.objects.get(id=service_id)
        form = ServiceForm(request.POST, instance=service)

        context = {
            'form': form,
            'error': error_message,
        }
        if form.is_valid():
            form.save()
            return redirect('service-list')
        return render(request, 'Oreon_Components/services/service_edit.html', context)


class ServiceDeleteView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        service = get_object_or_404(Service, id=id)
        service.delete()
        return redirect('service-list')


class CategoryCreateView(View):
    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        context = {
            'form': form,
        }
        return render(request, 'Oreon_Components/Categories/create_category.html', context)

    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST, request.FILES)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()

            return redirect('service-category-list')
        return render(request, 'Oreon_Components/Categories/create_category.html', context)


class CategoryListView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        context = {
            'categories': categories,
        }
        return render(request, 'Oreon_Components/Categories/product_category_list.html', context)


class CategoryDeleteView(View):
    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        category = get_object_or_404(Category, slug=slug)
        category.delete()
        return redirect('service-category-list')


class EditCategoryView(View):
    def get(self, request, *args, **kwargs):
        category_slug = self.kwargs['slug']
        category = Category.objects.get(slug=category_slug)
        form = CategoryForm(instance=category)

        context = {
            'form': form
        }

        return render(request, 'Oreon_Components/Categories/edit_category.html', context)

    def post(self, request, *args, **kwargs):
        category_slug = self.kwargs['slug']
        category = Category.objects.get(slug=category_slug)
        form = CategoryForm(request.POST, request.FILES, instance=category)

        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('service-category-list')
        return render(request, 'Oreon_Components/Categories/edit_category.html', context)

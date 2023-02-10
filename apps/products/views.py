from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from apps.products.forms import ProductForm, CategoryForm
from apps.products.models import Product, Category


class ProductCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ProductForm()
        context = {
            'form': form,
        }
        return render(request, 'Oreon_Components/products/create_product.html', context)

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()

            return redirect('product-list')
        return render(request, 'Oreon_Components/products/create_product.html', context)


class ProductListView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        form = ProductForm()
        count = Product.objects.count()
        categories = Category.objects.all()
        context = {
            'products': products,
            'count': count,
            'categories': categories,
            'form': form,
        }
        return render(request, 'Oreon_Components/products/list_product.html', context)

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()

            return redirect('product-list')
        return render(request, 'Oreon_Components/products/create_product.html', context)


class EditProductView(View):
    def get(self, request, *args, **kwargs):
        product_slug = self.kwargs['slug']
        product = Product.objects.get(slug=product_slug)
        form = ProductForm(instance=product)

        context = {
            'form': form
        }

        return render(request, 'Oreon_Components/products/edit_product.html', context)

    def post(self, request, *args, **kwargs):
        product_slug = self.kwargs['slug']
        product = Product.objects.get(slug=product_slug)
        form = ProductForm(request.POST, request.FILES, instance=product)

        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('product-list')
        return render(request, 'Oreon_Components/products/edit_product.html', context)


class ProductDeleteView(View):
    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)
        product.delete()
        return redirect('product-list')


"""CRUD for Categories"""


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

            return redirect('product-category-list')
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
        return redirect('product-category-list')


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
            return redirect('product-list')
        return render(request, 'Oreon_Components/Categories/edit_category.html', context)

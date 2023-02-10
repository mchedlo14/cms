from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from apps.groups.forms import GroupForm, GroupPermissionForm
from apps.groups.models import Group, GroupPermission


class GroupCreateView(View):
    def get(self, request, *args, **kwargs):
        form = GroupForm()
        context = {
            'form': form,
        }
        return render(request, 'Oreon_Components/groups/group_create.html', context)

    def post(self, request, *args, **kwargs):
        form = GroupForm(request.POST, request.FILES)
        error_message = "Form Is Not Valid,Please Try Again!"
        context = {
            'form': form,
            'error': error_message,
        }
        if form.is_valid():
            form.save()
            return redirect('group-list')
        return render(request, 'Oreon_Components/groups/group_create.html', context)


class GroupListView(View):
    def get(self, request, *args, **kwargs):
        groups = Group.objects.all()
        context = {
            'groups': groups,
        }
        return render(request, 'Oreon_Components/groups/group_list.html', context)


class EditGroupView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        group = Group.objects.get(id=id)
        form = GroupForm(instance=group)

        context = {
            'form': form
        }

        return render(request, 'Oreon_Components/groups/group_edit.html', context)

    def post(self, request, *args, **kwargs):
        error_message = "Form Is Not Valid,Please Try Again!"
        group_id = kwargs.get('id')
        group = Group.objects.get(id=group_id)
        form = GroupForm(request.POST, instance=group)

        context = {
            'form': form,
            'error': error_message,
        }
        if form.is_valid():
            form.save()
            return redirect('group-list')
        return render(request, 'Oreon_Components/groups/group_edit.html', context)


class GroupDeleteView(View):
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, id=kwargs['id'])
        group.delete()
        return redirect('group-list')


class PermissionCreateView(View):
    def get(self, request, *args, **kwargs):
        form = GroupPermissionForm()
        context = {
            'form': form,
        }
        return render(request, 'Oreon_Components/permissions/permission_create.html', context)

    def post(self, request, *args, **kwargs):
        form = GroupPermissionForm(request.POST, request.FILES)
        error_message = "Form Is Not Valid,Please Try Again!"
        context = {
            'form': form,
            'error': error_message,
        }
        if form.is_valid():
            form.save()
            return redirect('permission-list')
        return render(request, 'Oreon_Components/permissions/permission_create.html', context)


class PermissionListView(View):
    def get(self, request, *args, **kwargs):
        permissions = GroupPermission.objects.all()
        context = {
            'permissions': permissions,
        }
        return render(request, 'Oreon_Components/permissions/permission_list.html', context)


class EditPermissionView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        permission = GroupPermission.objects.get(id=id)
        form = GroupPermissionForm(instance=permission)

        context = {
            'form': form
        }

        return render(request, 'Oreon_Components/permissions/permission_edit.html', context)

    def post(self, request, *args, **kwargs):
        error_message = "Form Is Not Valid,Please Try Again!"
        permission_id = kwargs.get('id')
        permission = GroupPermission.objects.get(id=permission_id)
        form = GroupPermissionForm(request.POST, instance=permission)

        context = {
            'form': form,
            'error': error_message,
        }
        if form.is_valid():
            form.save()
            return redirect('permission-list')
        return render(request, 'Oreon_Components/permissions/permission_edit.html', context)


class PermissionDeleteView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        permission = get_object_or_404(GroupPermission, id=id)
        permission.delete()
        return redirect('permission-list')

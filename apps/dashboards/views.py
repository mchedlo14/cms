from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class DashboardView(LoginRequiredMixin,TemplateView):
    pass

dashboard_view = DashboardView.as_view(template_name="dashboards/index.html")
dashboard_analytics_view = DashboardView.as_view(template_name="dashboards/dashboard-analytics.html")
dashboard_crm_view = DashboardView.as_view(template_name="dashboards/dashboard-crm.html")
dashboard_crypto_view = DashboardView.as_view(template_name="dashboards/dashboard-crypto.html")
dashboard_projects_view = DashboardView.as_view(template_name="dashboards/dashboard-projects.html")
dashboard_nft_view = DashboardView.as_view(template_name="dashboards/dashboard-nft.html")
dashboard_job_view = DashboardView.as_view(template_name="dashboards/dashboard-job.html")





class Page_managment(LoginRequiredMixin, TemplateView):

    pass


page_managment = DashboardView.as_view(template_name="page/page_create.html")
page_magment_list = DashboardView.as_view(template_name="page/page_list.html")


class Oreon_Menu(LoginRequiredMixin, TemplateView):

    pass


Menu = Oreon_Menu.as_view(template_name="Oreon_Components/Menu/menu.html")

class Oreon_Categories(LoginRequiredMixin, TemplateView):

    pass


# Categories = Oreon_Categories.as_view(template_name="Oreon_Components/Categories/categories.html")


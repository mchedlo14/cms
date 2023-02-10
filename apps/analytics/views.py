from django.shortcuts import render
from django.views import View

class AnalyticListView(View):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'Oreon_Components/analytic/analytic.html')
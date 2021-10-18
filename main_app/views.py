from django.shortcuts import (render, get_object_or_404)
from django.views.generic import ListView
from django.views.generic.base import View

from .models import ProjectModel


# Create your views here.


class HomeView(View):

    def get(self, request):
        return render(request, 'main_app/home.html')


class SearchListView(ListView):
    model = ProjectModel
    template_name = 'main_app/search-result.html'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = ProjectModel.objects.filter(project_name__icontains=query)
        return object_list

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        return context


class ProjectsListView(ListView):
    model = ProjectModel
    template_name = 'main_app/projects-list.html'
    paginate_by = 5
    queryset = ProjectModel.objects.all().order_by('project_published')


class ProjectView(View):
    def get(self, request, project_id):
        project = get_object_or_404(ProjectModel, pk=project_id)
        context = {'project': project}
        return render(request, 'main_app/project.html', context)
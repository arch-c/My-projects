from django.urls import re_path

from .views import (HomeView, SearchListView, ProjectsListView, ProjectView)

urlpatterns = [
    re_path('^projects/project/(?P<project_id>\d+)/$', ProjectView.as_view(), name='project'),
    re_path('^projects$', ProjectsListView.as_view(), name='projects'),
    re_path('^search$', SearchListView.as_view(), name='search_result'),
    re_path('^$', HomeView.as_view(), name='home')
]
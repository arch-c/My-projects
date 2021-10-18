from django.db import models


class ProjectModel(models.Model):
    project_name = models.CharField(max_length=100, verbose_name='Name')
    project_describe = models.TextField(verbose_name='Describe')
    project_link = models.CharField(max_length=2050, verbose_name='Link')
    project_published = models.DateTimeField(auto_now=True, verbose_name='Published')

    def __str__(self):
        return (f'{self.project_name}')
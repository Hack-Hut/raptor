from .views import ProjectView, BuildView, ResultsView
from django.conf.urls import url


urlpatterns = [
    url('project/(?P<pk>[\w\-]+)/$', ProjectView.as_view(), name="post-rud"),
    url('project/Build/(?P<pk>[\w\-]+)/$', BuildView.as_view(), name="post-rud"),
    url('project/Build/Results/(?P<pk>[\w\-]+)/$', ResultsView.as_view(), name="post-rud")
]

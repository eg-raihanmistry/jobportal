from django.urls import path
from api.v1.views import BasicAPiView, ProjectApiView

urlpatterns = [
    path('', BasicAPiView.as_view(), name="basic"),
    path('get/', ProjectApiView, name="project"),
]

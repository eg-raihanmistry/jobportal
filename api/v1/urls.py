from django.urls import path
from api.v1.views import BasicAPiView, ProjectApiView


# faltu urls
urlpatterns = [
    path('', BasicAPiView.as_view(), name="basic"),
    path('get/', ProjectApiView.as_view(), name="project"),
]

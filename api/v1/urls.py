from django.urls import path
from api.v1.views import BasicAPiView

urlpatterns = [
    path('', BasicAPiView.as_view(), name="basic")
]

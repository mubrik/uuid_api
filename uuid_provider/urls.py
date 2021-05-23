from django.urls import path
from .api.viewsets import ListUuidsViewset

urlpatterns = [
    path('list/', ListUuidsViewset.as_view(), name='list_uuid'),
]
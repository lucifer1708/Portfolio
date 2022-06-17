from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index, name='index'),
    # path('filter/', FilterList.as_view(), name='filter')
]

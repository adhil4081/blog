from django.urls import path
from . import views

# urlpatterns = [
#     path('',views.index,name='index')
# ]  

urlpatterns = [
    # Define your URL patterns and associate them with views.
    # For example:
    path('', views.index, name='index'),
    path('Post/<str:pk>',views.Post,name='Post')
]
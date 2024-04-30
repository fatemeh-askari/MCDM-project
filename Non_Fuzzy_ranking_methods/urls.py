from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_request, name='index'),
    path('data/<int:request_id>/', views.success, name='success'),
    path('save_matrix_data/', views.save_matrix_data, name='save_matrix_data'),
    path('results/<int:request_id>/', views.results, name='results'),
]
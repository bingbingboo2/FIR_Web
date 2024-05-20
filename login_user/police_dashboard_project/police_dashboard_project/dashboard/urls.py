from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_fir/', views.add_fir, name='add_fir'),
    path('search_fir/', views.dashboard, name='search_fir'),  # Add a URL for searching FIRs
    path('update_ipc/<int:fir_id>/', views.update_ipc, name='update_ipc'),  # Add a URL for updating IPC
]

from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name = 'contracts'

urlpatterns = [
    path('contracts/', views.contracts_list, name='contracts_list'),
    path('contracts/create/', views.contracts_create, name='contracts_create'),
    path('contracts/<int:pk>/', views.contracts_detail, name='contracts_detail'),
    path('contracts/<int:pk>/update/', views.contracts_update, name='contracts_update'),
    path('contracts/<int:pk>/delete/', views.contracts_delete, name='contracts_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

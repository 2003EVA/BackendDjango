
from django.contrib import admin
from django.urls import path
from myapp.views import ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfiles/', ProfileView.as_view(), name='perfiles'),
    path('perfiles/<int:pk>/', ProfileView.as_view(), name='perfil_detalle'),
]

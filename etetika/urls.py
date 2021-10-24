
from django.contrib import admin
from django.urls import path, include


from . import views
urlpatterns = [
    path('', views.index),
    path('superadmin/', admin.site.urls),
    path('dashboard/', views.dashboard),
    path('account/', include('account.urls'))
]

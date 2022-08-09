from django.contrib import admin
from django.urls import path, include
from rental import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rental/', include('rental.urls')),
    path('cycle/', views.cycleList.as_view()),
    path('sport/', views.sportList.as_view()),
    path('electronic/', views.sportList.as_view()),
]

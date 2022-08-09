from django.urls import URLPattern, path
from rental import views

urlpatterns = [
    path('cycle/', views.cycleList.as_view()),
    path('sport/', views.sportList.as_view()),
    path('electronic/', views.sportList.as_view()),
]
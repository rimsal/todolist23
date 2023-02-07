from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.UzduotisView.as_view(), name='index'),
    path('uzduotis/<int:uzduotis_id>/', views.Uzduotis, name='uzduotis'),
    path('uzduotis/nauja', views.UzduotisCreateView.as_view(), name='nauja-uzduotis'),
    path('uzduotis/<int:pk>/redaguoti', views.UzduotisEditView.as_view(), name='redaguoti-uzduotis'),
    path('uzduotis/<int:pk>/istrinti', views.UzduotisDeleteView.as_view(), name='istrinti-uzduotis'),
]

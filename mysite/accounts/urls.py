from django.urls import path
from . import views 

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('<username>/', views.AccountDetailView.as_view(), name = 'userdetail'),
]
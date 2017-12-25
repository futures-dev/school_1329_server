from django.urls import path

from school_1329_server.users.views import api as views

urlpatterns = [
    path('generate_password', views.CreateTemporaryPasswordAPIView.as_view()),
    path('validate_password', views.ValidateTemporaryPasswordAPIView.as_view()),
    path('register', views.CreateUserAPIView.as_view()),
    path('generate_admin_password', views.CreateTeacherAdminPasswordAPIView.as_view())
]
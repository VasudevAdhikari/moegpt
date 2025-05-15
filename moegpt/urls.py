"""
URL configuration for moegpt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from chatbot.views import *
from authorization.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('askquestion/', askquestion, name="askquestion"),
    path('chatbot/', show_chatbot, name="chatbot"),
    path('login/', user_login, name="login"),
    path('register/', user_register, name="register"),
    path('logout/', user_logout, name='logout'),
    path('show_history/<int:module_id>/', show_history),
    path('', determine_interface),
    path('delete_history/<int:delete_module_id>/<int:current_module_id>/', delete_history),
    path('invalid_location/', invalid_location),
    path('profile/', show_profile),
    path('check_email/', check_email),
    path('check_username/', check_username),
]

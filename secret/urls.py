"""secret URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from Cryptography.views import MessageView, ReceivedMessage, Login, Logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^success/', ReceivedMessage.as_view(), name='received-message'),
    url(r'^message/', MessageView.as_view(), name='message-view'),
    url(r'^login/', Login, name='login-redirect'),
    url(r'^logout/', Logout, name='logout'),
    url(r'^received/', ReceivedMessage.as_view(), name='receive')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


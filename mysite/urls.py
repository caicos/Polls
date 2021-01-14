"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
#
# urlpatterns += i18n_patterns(
#     # Ces URLs auront comme chemin : /<language_code/ au début pour les différentes langues du site
#     path('polls/', include('polls.urls')),
# )
# §: La vue de redirection set_language de la page https://docs.djangoproject.com/fr/3.1/topics/i18n/translation/

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]

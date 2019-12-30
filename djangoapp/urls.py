from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.autodiscover()

import autobot.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", autobot.views.index, name="index"),
    path("login/", autobot.views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("social-auth/", include('social_django.urls', namespace="social")),
    path("db/", autobot.views.db, name="db"),
    path("admin/", admin.site.urls),
]

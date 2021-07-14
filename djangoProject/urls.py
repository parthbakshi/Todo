"""djangoProject URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from tutorial import views as todolistviews
from django.conf import settings
from users import urls as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',todolistviews.index,name="index"),
    #path('<int:id>', views.v1, name="v1"),
    path('<int:id>/items', todolistviews.get_list, name="get_list"),
    path('<int:id>/new', todolistviews.create_list, name="new_item"),
    path('alllists', todolistviews.get_all_todo_list, name="all list"),
    path('users/', include(user_views))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns


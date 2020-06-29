"""homework02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include   # app（squence）导入
from django.views.static import serve   # serve 导入
from django.conf.urls import url    #url  导入
from homework02 import settings   # settings 导入
urlpatterns = [
    path('admin/', admin.site.urls),
    path('squence/', include("squence.urls")),
    # 指定图片上传的目录
    url(r"^media/(?P<path>.*)", serve, {"document_root": settings.MEDIA_ROOT}),
]

"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
# 对应视图
from goods.views import GoodsListViewSet


from MxShop.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet



# goods_list = GoodsListViewSet.as_view({
#     'get': 'list',
# })
router = DefaultRouter();

#配置goods的url
router.register(r'goods',GoodsListViewSet,basename='goods');


urlpatterns = [
    path('admin/', admin.site.urls),
    path('media/(?P<path>.*))',serve,{"document_root": MEDIA_ROOT}),
    # path('api/goods/',goods_list,name="GoodsListView"),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include((router.urls, 'app_name'))),
    path('docs/',include_docs_urls(title="RestfulApi")),
]

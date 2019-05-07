"""mxshop2 URL Configuration

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
# from django.contrib import admin
from django.urls import path
import xadmin
# xadmin.autodiscover()
# from xadmin.plugins import xversion
# xversion.register_models()

from django.conf import settings

from django.views.static import serve
from django.conf.urls.static import static
from django.conf.urls import include
from rest_framework.documentation import include_docs_urls
# from goods.views_base import GoodsListView
from goods.views import GoodsListView1,GoodsListView2,GoodsListView3

# 方法一
# goods_list=GoodsListView3.as_view({
#     'get':'list'
# })

# 方法二
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('goods3',GoodsListView3,base_name='good3')


urlpatterns = [
    
    path('goods1/', GoodsListView1.as_view(),name='goods_list1'),
    path('goods2/', GoodsListView2.as_view(),name='goods_list2'),
    # path('goods3/', goods_list,name='goods_list3'),
    # path('goods3/', include(router.urls),name='goods_list3'),
    path('', include(router.urls),name='goods_list3'),
    path('docs/',include_docs_urls(title='慕学生鲜')) ,
    path('api-auth/', include('rest_framework.urls')),
    path('', xadmin.site.urls), 

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        path('media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}), # 加一条MEDIA_URL的映射
    ]

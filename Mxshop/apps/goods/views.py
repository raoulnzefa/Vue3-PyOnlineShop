
from .serializers import GoodsSerializer #引入序列化的类
from rest_framework.views import APIView #api文档视图
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination #分页

from .models import Goods

# Create your views here.
class GoodsPagination(PageNumberPagination):
    """
    商品列表页, 分页， 搜索， 过滤， 排序
    """
    page_size = 10;
    page_size_query_param =  'page_size';
    page_query_param = "p";
    max_page_size = 100
class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):

    '''
     商品列表页面
    '''

    queryset = Goods.objects.all()[:10];
    serializer_class = GoodsSerializer;


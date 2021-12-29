
from .serializers import GoodsSerializer #引入序列化的类
from rest_framework.views import APIView #api文档视图
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination #分页
from rest_framework import filters; #过滤器
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter

from .models import Goods
# Create your views here.
class GoodsPagination(PageNumberPagination):
    """
    分页
    """
    page_size = 10;
    page_size_query_param =  'page_size';
    page_query_param = "p";
    max_page_size = 100

class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):

    '''
     商品列表页面
     搜索， 过滤， 排序
    '''

    queryset = Goods.objects.all();# 查询字段
    serializer_class = GoodsSerializer;#字段序列化
    pagination_class = GoodsPagination; #分页器

#     过滤器
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter);
    filter_class = GoodsFilter;
    search_fields = ('=name', 'goods_brief', 'goods_desc');#搜索字段
    ordering_fields = ('sold_num', 'shop_price');#排序字段

    def retrieve(self,request,*args,**kwargs):
        instance = self.get_object();
        instance.click_num += 1;
        instance.save();

        serializer = self.get_serializer(instance)
        return Response(serializer.data);

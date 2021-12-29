# -*- coding: utf-8 -*-
__author__ = 'lifechat'

# 引入对应的依赖包
from rest_framework import serializers
from django.db.models import Q

from goods.models import GoodsImage,Goods,GoodsCategory,HotSearchWords,Banner
from goods.models import GoodsCategoryBrand,IndexAd

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__";

class  GoodsSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(required=True,max_length=100);
    # click_num = serializers.IntegerField(default=0);
    # goods_front_image = serializers.ImageField();
    category = CategorySerializer();

    class Meta:
        model = Goods
        fields = "__all__";
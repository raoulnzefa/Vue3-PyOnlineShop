# Generated by Django 4.0 on 2021-12-23 03:57

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_goodscategorybrand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_sn', models.CharField(default='', max_length=50, verbose_name='商品唯一货号')),
                ('name', models.CharField(max_length=100, verbose_name='商品名')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('sold_num', models.IntegerField(default=0, verbose_name='商品销售量')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('goods_num', models.IntegerField(default=0, verbose_name='库存数')),
                ('market_price', models.FloatField(default=0, verbose_name='市场价格')),
                ('shop_price', models.FloatField(default=0, verbose_name='本店价格')),
                ('goods_brief', models.TextField(max_length=500, verbose_name='商品简短描述')),
                ('goods_desc', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('ship_free', models.BooleanField(default=True, verbose_name='是否承担运费')),
                ('goods_front_image', models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='封面图')),
                ('is_new', models.BooleanField(default=False, verbose_name='是否新品')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热销')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goodscategory', verbose_name='商品类目')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
    ]
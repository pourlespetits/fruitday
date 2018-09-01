from django.db import models
# Create your models here.


class GoodsType(models.Model):
    """docstring for GoodsType"""
    tname = models.CharField(max_length=40, verbose_name='商品类型')
    gpicture = models.ImageField(
        upload_to='upload/goodstype', verbose_name='图片')
    tdesc = models.TextField(verbose_name='商品描述')  # 商品描述

    def __str__(self):
        return self.tname

    def to_dict(self):
        dic = {
            'title': self.tname,
            'picture': self.gpicture.__str__(),
            'tdesc': self.tdesc
        }
        return dic

    class Meta:
        db_table = 'goodType'
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name


# 商品的 Models
class Goods(models.Model):
    """docstring for Goods"""
    title = models.CharField(max_length=30, verbose_name="商品名称")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='商品价格')
    spec = models.CharField(max_length=50, verbose_name='商品规格')  # 商品规格
    picture = models.ImageField(
        upload_to='static/upload/goods', verbose_name='图示')
    isActive = models.BooleanField(default=True, verbose_name='销售状态')
    # 创建与GoodsType的一对多映射
    goodtype = models.ForeignKey(GoodsType, null=True, verbose_name='商品类型')

    def __str__(self):
        return self.title



    class Meta:
        db_table = 'goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name


class Users(models.Model):
    """docstring for ClassName"""
    uname = models.CharField(max_length=30, verbose_name='用户名')
    uphone = models.CharField(max_length=11, verbose_name='电话号码')
    upwd = models.CharField(max_length=20)
    uemail = models.EmailField(verbose_name='邮箱')
    isActive = models.BooleanField(default=True)
    # 创建和Goods的一对多的关系
    hasbuy = models.ManyToManyField(Goods, null=True, verbose_name='已买过')

    def __str__(self):
        return self.uname

    class Meta:
        db_table = 'users'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class CartInfo(models.Model):
    # userid,外键,引用自Users实体
    user = models.ForeignKey(Users, verbose_name='用户ID')
    # goodid,外键,引用自Goods实体
    good = models.ForeignKey(Goods, verbose_name='商品ID')
    # count,整数,表示购买数量
    count = models.IntegerField(verbose_name='购买数量')
                     
    # def __str__(self):
    #     return self.id

    class Meta:
        db_table = 'cartinfo'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        ordering = ('-count',)

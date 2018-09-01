from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from .models import *
from .forms import *
import json
# Create your views here.


# def login_views(request):
#     if request.method == 'GET':
#         if 'phone' in request.COOKIES:
#             return HttpResponse("欢迎" + request.COOKIES['phone'])
#         else:
#             form = LoginForm()
#             return render(request, 'login.html', locals())
#     else:
#         phone = request.POST['phone']
#         pwd = request.POST['pwd']
#         try:
#             obj = Users.objects.get(uphone=phone, upwd=pwd)
#         except:
#             return HttpResponse('用户名或密码错误')
#         # isSaved = request.POST.get('isSaved', '')
#         if 'isSaved' in request.POST:
#             resp = HttpResponse('登录成功,已记住密码')
#             resp.set_cookie('user_id', obj.id, 60 * 60 * 24 * 365)
#             resp.set_cookie('phone', phone, 60 * 60 * 24 * 365)
#             return resp
#         else:
#             return Htt
# Response('登录成功')


def register_views(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        pwd = request.POST['pwd']
        email = request.POST.get('email', '')
        name = request.POST['uname']
        phone = request.POST['phone']

        # 验证手机好是否存在

        ulist = Users.objects.filter(uphone=phone)
        if ulist:
            # 手机号已存在
            return render(request, 'register.html', {'errMsg': '手机号已存在',
                    'sphone':phone,
                    'sname': name,
                    'semail': email
                })
        else:
            obj = Users(uphone=phone, upwd=pwd, uname=name, uemail=email)
            obj.save()
            return HttpResponse("register successfully")


def regverify_views(request):
    phone = request.GET['uphone']
    ulist = Users.objects.filter(uphone=phone)
    if ulist:
        s = 1
        errMsg = "用户名已存在"
    else:
        s = 0
        errMsg = "验证通过"
    dic = {"status": s, "errMsg": errMsg}
    return HttpResponse(json.dumps(dic))


def regmsg_views(request):
    return HttpResponse("data has been got")


def saveinfo_views(request):
    '''将用户数据保存到数据库'''
    # 方式1
    Users.objects.create(uphone='12345678910', upwd='000000',
                         uname='wq', uemail='wq@qq.com')
    # 方式2
    obj = Users(uphone='98745632101', upwd='111111',
                uname='qiqi', uemail='qiqi@qq.com')
    obj.save()
    # 方式3
    udic = {
        'uphone': '85274196303',
        'upwd': '5201314',
        'uname': 'keke',
        'uemail': 'keke@qq.com'
    }
    obj = Users(**udic)
    obj.save()
    return HttpResponse("用户数据已保存到数据库")


def queryinfo_views(request):
    '''查询用户信息'''
    result = Users.objects.values('uname', 'uemail')
    print(result.count())
    string = ''
    for obj in result:
        string += obj['uname'] + "&nbsp;&nbsp;" + obj['uemail'] + '<br>'
    return HttpResponse(string)


def oto_views(request):
    pass


def qfruit_views(request):
    good = Goods.objects.get(id=1)
    goodtype = good.goodstype_set.all()
    return render(request, 'qfruit.html', locals())


def form_views(request):
    if request.method == 'GET':
        # 创建RemarkForm的对象
        form = RemarkForm()
        # 将对象作为变量发送到目标中
        return render(request, 'forms.html', locals())
    else:
        # 接收提交的数据
        # 通过RemarkForm通过构造函数接收post数据
        form = RemarkForm(request.POST)
        # 验证
        if form.is_valid():
            # 通过验证后获取表单的值
            data = form.cleaned_data
            subject = data['subject']
            email = data['email']
            message = data['message']
            print(subject, email, message)
            return HttpResponse('GET ok')
        else:
            return HttpResponse('get faild')


def registerForm_views(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return HttpResponse("get OK")
        else:
            return HttpResponse('get faild')


def login_views(request):
    if request.method == 'GET':
        # 处理GET请求
        # 获取原地址
        url = request.META.get('HTTP_REFERER', '/index/')
        # 通过url构建响应对象
        resp = HttpResponseRedirect(url)
        # 判断session中是否有id 和 uphone
        if 'id' in request.session and 'uphone' in request.session:
            # print('重定向中1')
            return resp
        else:
            # 判断用户是否登录过,选择了记住密码
            if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
                # 将cookie中的登录信息存进session中
                request.session['id'] = request.COOKIES['id']
                request.session['uphone'] = request.COOKIES['uphone']
                # print('重定向中2')
                return resp
            else:
                # 将url保存进cookie
                resp = render(request, 'login.html')
                resp.set_cookie('url', url)
                return resp
    else:  # 处理POST请求
        phone = request.POST['phone']
        pwd = request.POST['pwd']
        ulist = Users.objects.filter(uphone=phone, upwd=pwd)
        # 判断是否登录成功
        if ulist:  # 登录成功
            url = request.META.get('HTTP_REFERER', '/index/')

            resp = HttpResponseRedirect(url)
            # 从cookie中将url删除出去
            if 'url' in request.COOKIES:
                resp.delete_cookie('url')

            expries = 60 * 60 * 24 * 365
            # 将登录信息保存进session
            request.session['uphone'] = phone
            request.session['id'] = ulist[0].id

            # 判断用户是否勾选了记住密码
            if 'isSaved' in request.POST:
                # 将登录信息保存进cookie
                resp.set_cookie('id', ulist[0].id, expries)
                resp.set_cookie('uphone', phone, expries)
            return resp
            # else:
            #     return HttpResponse("未记住密码,前往首页")
        else:  # 登录失败
            # 继续展示登录页面
            return render(request, 'login.html')


def quitlogin_views(request):
    # 记录原地址
    url = request.META.get('HTTP_REFERER', '/index/')
    resp = HttpResponseRedirect(url)
    # 删除session中的登录信息
    if 'id' in request.session and 'uphone' in request.session:
        del request.session['uphone']
        del request.session['id']
    # 删除cookie中的登录信息
    if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
        resp.delete_cookie('uphone')
        resp.delete_cookie('id')
    return resp


def check_login_views(request):
    if 'id' in request.session and 'uphone' in request.session:
        # 已处于登录状态
        loginStatus = 1
        # 从数据库获取uname
        seid = request.session.get('id')
        uname = Users.objects.get(id=seid).uname
        dic = {
            "lgStatus": loginStatus,
            "uname": uname
        }
        return HttpResponse(json.dumps(dic))
    else:  # session 中没有登录信息
        # 判断cookie中是否有登录信息
        if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
            # 将cookie中的登录信息存到session中
            request.session['id'] = request.COOKIES['id']
            request.session['uphone'] = request.COOKIES['uphone']
            loginStatus = 1
            # 从数据库获取uname
            seid = request.COOKIES.get('id')
            uname = Users.objects.get(id=seid).uname
            dic = {
                "lgStatus": loginStatus,
                "uname": uname
            }
            return HttpResponse(json.dumps(dic))
        else:
            # session和cookie中都没有登录信息
            dic = {
                "lgStatus": 0
            }
            return HttpResponse(json.dumps(dic))


def index_views(request):
    # 检测用户的登录状态
    isActive = 0
    if 'uphone' in request.session:
        tip = "欢迎:" + request.session['uphone']
        isActive = 1
    list_types = GoodsType.objects.all()
    return render(request, 'index.html', locals())


def getSource_views(request):
    jsonList = []
    
    # 查询所有的商品类型
    list_types = GoodsType.objects.all()
    # 循环遍历types,
    for obj in list_types:
        typejson = json.dumps(obj.to_dict())
        # print(typejson)
        # 获取每个类型的前5个的商品
        g_list = obj.goods_set.order_by("-id")[0: 10]
        # 将g_list序列化成字符串
        g_list_json = serializers.serialize('json', g_list)
        
        objDic = {}
        objDic['typeobj'] = typejson
        # goods = obj.goods_set.order_by("-id")[0: 5]
        objDic['goods'] = g_list_json

        jsonList.append(objDic)
    jsonData = json.dumps(jsonList)
    # print(jsonData)
    return HttpResponse(jsonData)


# 添加或更新购物车的内容
def add_cart_views(request):
    # 从session中获取用户id
    userid = request.session.get('id')
    # 从请求中获取商品id
    goodid = request.POST['goodid']
    
    # 购买数量默认为1
    gcount = 1
    #查询购物车是否有相同的用户以及商品,如果有,则更新数量,否则
    # 将上述数据插入数据库
    cart_list = CartInfo.objects.filter(user_id=userid,good_id=goodid)
    if cart_list:
        # 购物车已有该商品,更新记录
        cartinfo = cart_list[0]
        cartinfo.count = cartinfo.count + gcount
        cartinfo.save()

        dic = {
            'status': 1,
            'statusText': '更新数量成功'
        }
        return HttpResponse(json.dumps(dic))
    else:
        # 购物车每有该商品,将要添加到购物车的商品信息插入数据库
        cartinfo = CartInfo()
        cartinfo.good_id = goodid
        cartinfo.user_id = userid
        cartinfo.count = gcount
        cartinfo.save()

        dic = {
            'status': 1,
            'statusText': '添加购物车成功'
        }
        return HttpResponse(json.dumps(dic))

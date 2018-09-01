# forms.py
from django import forms
from .models import *

# 为topic下拉列表初始化数据-元组
TOPIC_CHOICE = (
    ('LEVEL1', '好评'),
    ('LEVEL2', '中评'),
    ('LEVEL3', '差评')
)


class RemarkForm(forms.Form):
    # 1.创建一个subject 属性,表示评论的标签-文本框
    # 1.1 label:生成控件前的文本
    subject = forms.CharField(label='标题')

    # 2.创建一个email属性,表示邮箱 -- email框
    email = forms.EmailField(label='邮箱')

    # 3.创建一个message属性,表示评论的内容--多行文本框
    # 3.1 widget:指定生成控件的类型
    message = forms.CharField(label='内容', widget=forms.Textarea)

    # 4.创建一个topic 属性,表示评论级别,对应生成一个下拉列表
    # 4.1 指定下拉列表中的选项的元组
    topic = forms.ChoiceField(label='评价', choices=TOPIC_CHOICE)

    # 5.创建一个isSaved属性,表示是否保存--复选框
    isSaved = forms.BooleanField(label='是否保存?')


class RegisterForm(forms.Form):
    uname = forms.CharField(label='用户名')
    upwd = forms.CharField(label='密码', widget=forms.PasswordInput)
    uage = forms.IntegerField(label='年龄')
    uemail = forms.EmailField(label='邮箱')


class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['uphone', 'upwd']
        labels = {
            'uphone': '手机号',
            'upwd': '密码'
        }
        widgets = {
            'uphone': forms.TextInput(
                attrs={'placeholder': '11位的手机号',
                       'class': 'forms-control'}),
            'upwd': forms.PasswordInput(
                attrs={'placeholder': '6-18位的密码',
                       'class': 'forms-control'})
        }

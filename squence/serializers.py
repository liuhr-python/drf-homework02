from rest_framework import serializers

# 定义序列化器类 和模型moles表对应
from squence.models import Employee
from homework02 import settings  # 获取静态资源


# 创建序列化器
class EmployeeSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()
    # gender = serializers.IntegerField()   # 信息默认为 choices=gender_choices,
    # pic = serializers.ImageField()        # 信息默认为 当前路径 /media/pic/xxx.jpg

    # 自定义性别的返回值
    gender = serializers.SerializerMethodField()

    def get_gender(self, obj):
       # 性别是choices类型  get_字段名_display()直接访问值
        return obj.get_gender_display()

    # # 自定义返回图片的全路径
    pic = serializers.SerializerMethodField()

    def get_pic(self, obj):

    # 将图片的路径替换成全路径
        return "%s%s%s" % ("http://127.0.0.1:8000", settings.MEDIA_URL, str(obj.pic))




from rest_framework import serializers

# 定义序列化器类 和模型moles表对应
from squence.models import Employee
from homework02 import settings  # 获取静态资源


# 创建序列化器
class EmployeeSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()
    phone = serializers.CharField()
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



# 创建反（De）序列化器
class EmployeeDeSerializer(serializers.Serializer):

    # 前端信息反序列化校验规则
    # 用户名长度规划
    username = serializers.CharField(
        max_length=8,
        min_length=2,
        # 为前端提供返回的错误信息 serializer.errors
        error_messages={
            "max_length": "长度过长！",
            "min_length": "长度过短！",
        }
    )
    password = serializers.CharField(required=False)
    phone = serializers.CharField()

    # 新增信息  须重写create()方法
    # 原因：继承自serializer类，没有新增的具体操作实现
    def create(self, validated_data):
        # 新增方法 create(**validated_data)
        return Employee.objects.create(**validated_data)

from rest_framework.views import APIView
from rest_framework.response import Response

from squence.models import Employee
from .serializers import EmployeeSerializer  # 导入序列化器
from .serializers import EmployeeDeSerializer  # 导入反序列化器

class EmployeeAPIView(APIView):

    # 查询信息
    def get(self, request, *args, **kwargs):
        # 通过pk （id）获取
        user_id = kwargs.get("pk")

        if user_id:
            # 查询单个
            emp_obj = Employee.objects.get(pk=user_id)
            # 信息格式问题，需要序列化，通过序列化器（EmployeeSerializer）
            # .data 将序列化器的数据打包成字典
            emp_ser = EmployeeSerializer(emp_obj).data

            return Response({
                "status": 200,
                "msg": "查询单个员工成功",
                "results": emp_ser,
            })

        else:
            # 查询所有
            emp_list = Employee.objects.all()

            # 多个信息序列化  需要指定many=True
            emp_list_ser = EmployeeSerializer(emp_list, many=True).data

            return Response({
                "status": 200,
                "msg": "查询所有员工成功",
                "results": emp_list_ser,
            })

    # 添加信息
    def post(self, request, *args, **kwargs):
        # .data 将序列化的数据转换为 字典类型
        user_data = request.data

        # 不是字典类型 或者 为空   报错
        if not isinstance(user_data, dict) or user_data == {}:
            return Response({
                "status": 501,
                "msg": "数据有误",
            })

        # 从 反序列化器中校规 参数必须由 data=转换为字典类型的值
        serializer = EmployeeDeSerializer(data=user_data)
        # 对序列化的数据进行校验
        # 通过is_valid() 方法对传递过来的参数进行校验
        # 校验合法返回True
        if serializer.is_valid():
            # 调用save()去保存对象  在serializer.py中，反序列化器必须重写create()方法
            emp_obj = serializer.save()
            return Response({
                "status": 201,
                "msg": "用户创建成功",
                "results": EmployeeSerializer(emp_obj).data
            })
        else:
            return Response({
                "status": 501,
                "msg": "用户创建失败",
                # 验证失败后错误信息包含在 .errors中，对应反序列化器中的列值参数error_messages
                "results": serializer.errors
            })

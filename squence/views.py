from rest_framework.views import APIView
from rest_framework.response import Response

from squence.models import Employee
from .serializers import EmployeeSerializer  # 导入序列化器

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
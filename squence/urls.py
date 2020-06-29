from django.urls import path

from squence import views

urlpatterns = [

    path("emp/", views.EmployeeAPIView.as_view()),  # 获取全部信息
    path("emp/<str:pk>/", views.EmployeeAPIView.as_view()),  # 获取单个信息
]

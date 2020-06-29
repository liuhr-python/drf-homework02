from django.db import models

# Create your models here.

class Employee(models.Model):
    gender_choices = (
        (0, "男"),
        (1, "女"),
        (2, "未知"),
    )

    username = models.CharField(max_length=80)
    password = models.CharField(max_length=64)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    phone = models.CharField(max_length=11, null=True, blank=True)
    pic = models.ImageField(upload_to="pic", default="pic/1.jpg")

    class Meta:
        db_table = "employee_list"
        verbose_name = "员工表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

from django.db import models

class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name="사용자명")
    passwords = models.CharField(max_length=32,
                                 verbose_name="비밀번호")
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name="등록시간")
    def __str__(self):
        return self.name

    class Meta:
        db_table = "venduster_fcuser"
        verbose_name = "벤더스터 사용자"
        verbose_name_plural = "벤더스터 사용자"

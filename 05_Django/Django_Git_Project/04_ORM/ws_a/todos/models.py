from django.db import models

# Create your models here.
class Todo(models.Model):
    work = models.CharField(max_length=100)
    content = models.TextField()
    is_completed = models.BooleanField()
    # 상속 받은 Model 클래스에는
    # objects 라는 manager가
    # 정의되어있다.
    def __str__(self):
        return f'{self.pk}번째 할 일은 {self.work}입니다.'

class Comment(models.Model):
    pass
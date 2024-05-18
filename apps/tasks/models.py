from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Task(models.Model):
    TASK_STATUS_CHOICES = [
        ('Выполнить', 'Выполнить'),
        ('В процессе', 'В процессе'),
        ('Завершено', 'Завершено'),
        ('Отменено', 'Отменено'),
    ]

    title = models.CharField(max_length=100, default='Новое задание', verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default='todo',
                              verbose_name='Статус')
    completed = models.BooleanField(default=False, verbose_name='Завершено')
    due_date = models.DateField(default=date.today, verbose_name='Срок выполнения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks',
                                    null=True, blank=True, verbose_name='Назначено')

    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments', verbose_name='Задача')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments',
                             verbose_name='Пользователь')
    content = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name='Исходный комментарий')

    def __str__(self):
        return f'Comment by {self.user} on {self.task}'



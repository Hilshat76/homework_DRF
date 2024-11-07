from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    preview = models.ImageField(upload_to='course/preview', verbose_name="Превью", **NULLABLE)
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f'{self.title}'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    preview = models.ImageField(upload_to='lesson/preview', verbose_name="Превью", **NULLABLE)
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    linc_to_video = models.CharField(max_length=150, verbose_name="Ссылка на видео", **NULLABLE)
    course = models.ForeignKey(Course, verbose_name="Курс", on_delete=models.CASCADE, null=True, related_name="lessons")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f'{self.title}'

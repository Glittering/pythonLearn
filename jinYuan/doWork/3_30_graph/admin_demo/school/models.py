from django.db import models

# Create your models here.


class Teacher(models.Model):
    gender_cho=(
        ('male','男'),
        ('female','女')
    )
    name = models.CharField(max_length=4, verbose_name='教师姓名')
    age = models.IntegerField()
    gender = models.CharField(max_length=4,choices=gender_cho)
    img = models.ImageField(blank=True,null=True,upload_to='images')
    date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '教师表'


class Garden(models.Model):
    name = models.CharField(max_length=4)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '班级'


class Student(models.Model):
    name = models.CharField(max_length=4)
    teacher = models.ManyToManyField(Teacher)
    garden = models.ForeignKey(Garden)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '学生'

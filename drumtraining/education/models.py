from django.contrib.auth import get_user_model
from django.db import models


class Instructor(models.Model):
    instructor = models.OneToOneField(get_user_model(),
                                      on_delete=models.CASCADE,
                                      primary_key=True)
    work = models.CharField(max_length=100,
                            blank=True)
    bio = models.TextField(blank=True)
    student = models.ManyToManyField('Student')
    course = models.ManyToManyField('Course')
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Instructor <{self.instructor}>"

    class Meta:
        verbose_name = "преподаватель"
        verbose_name_plural = "преподаватели"


class Student(models.Model):
    LEVEL_DEL = "DEL"
    LEVEL_BEG = "BEG"
    LEVEL_PRO = "PRO"

    LEVEL_CHOICES = [
        (LEVEL_DEL, "dilettante"),
        (LEVEL_BEG, "beginner"),
        (LEVEL_PRO, "professional")
    ]

    MALE = "M"
    FEMALE = "F"

    GENDER_CHOICES = [
        (MALE, "male"),
        (FEMALE, "female")
    ]

    student = models.OneToOneField(get_user_model(),
                                   on_delete=models.CASCADE,
                                   primary_key=True)
    birthday = models.DateField()
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES)
    level = models.CharField(max_length=3,
                             choices=LEVEL_CHOICES,
                             default=LEVEL_DEL)
    bio = models.TextField(blank=True)
    course = models.ManyToManyField('Course')

    def __str__(self):
        return f"Author <{self.student}>"

    class Meta:
        verbose_name = "студент"
        verbose_name_plural = "студенты"


class Course(models.Model):
    name = models.CharField(max_length=70,
                            blank=False,
                            primary_key=True)
    started_at = models.DateField()
    duration = models.CharField(max_length=30,
                                blank=True)
    description = models.TextField(blank=False)
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f"Course <{self.name}>"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Category(models.Model):
    name = models.CharField(max_length=30,
                            blank=False,
                            primary_key=True)

    def __str__(self):
        return f"Category <{self.name}>"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

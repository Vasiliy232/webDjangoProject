# Generated by Django 3.2 on 2022-08-01 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('started_at', models.DateField()),
                ('duration', models.CharField(blank=True, max_length=30)),
                ('price', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=1)),
                ('level', models.CharField(choices=[('DEL', 'dilettante'), ('BEG', 'beginner'), ('PRO', 'professional')], default='DEL', max_length=3)),
                ('bio', models.TextField(blank=True)),
                ('course', models.ManyToManyField(to='education.Course')),
            ],
            options={
                'verbose_name': 'студент',
                'verbose_name_plural': 'студенты',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('instructor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('work', models.CharField(blank=True, max_length=100)),
                ('bio', models.TextField(blank=True)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ManyToManyField(to='education.Course')),
                ('student', models.ManyToManyField(to='education.Student')),
            ],
            options={
                'verbose_name': 'преподаватель',
                'verbose_name_plural': 'преподаватели',
            },
        ),
    ]
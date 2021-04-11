# Generated by Django 3.2 on 2021-04-11 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=255)),
                ('question_desc', models.TextField(default='')),
                ('correct_attempts', models.IntegerField(default=0)),
                ('total_attempts', models.IntegerField(default=0)),
                ('max_marks', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.JSONField()),
                ('output', models.JSONField()),
                ('time_limit', models.IntegerField()),
                ('memory_limit', models.IntegerField()),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.question')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('submission_time', models.DateTimeField(auto_now=True)),
                ('attempt', models.IntegerField(default=0)),
                ('status', models.CharField(default='NA', max_length=5)),
                ('accuracy', models.FloatField(default=0)),
                ('code', models.TextField(default='')),
                ('language', models.CharField(choices=[('cpp', 'C++'), ('c', 'C'), ('py', 'Python')], max_length=6)),
                ('question_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.question')),
                ('user_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.FloatField(default=0)),
                ('senior', models.BooleanField(default=False)),
                ('correct_answers', models.IntegerField(default=0)),
                ('latest_submission_time', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

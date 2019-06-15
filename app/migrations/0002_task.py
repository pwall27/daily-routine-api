# Generated by Django 2.2.2 on 2019-06-15 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active?')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation datetime.', verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Update datetime.', null=True, verbose_name='Updated Date')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'db_table': 'tasks',
                'ordering': ('created_at',),
            },
        ),
    ]
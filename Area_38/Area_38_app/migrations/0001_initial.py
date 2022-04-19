# Generated by Django 3.2.5 on 2022-04-18 21:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=32)),
                ('actionDescription', models.CharField(max_length=200, null=True)),
                ('actionDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('reportName', models.CharField(max_length=32, null=True)),
                ('userEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Area_38_app.userinfo', to_field='email')),
            ],
        ),
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=32)),
                ('fileDescription', models.CharField(max_length=200, null=True)),
                ('uploadDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('userEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Area_38_app.userinfo', to_field='email')),
            ],
        ),
    ]

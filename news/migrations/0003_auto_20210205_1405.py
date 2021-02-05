# Generated by Django 3.1.6 on 2021-02-05 13:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_auto_20210205_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 5, 14, 5, 11, 782192)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('posted_on', models.DateTimeField(default=datetime.datetime(2021, 2, 5, 14, 5, 11, 782192))),
                ('posted_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
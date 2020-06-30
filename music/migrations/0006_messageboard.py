# Generated by Django 2.2.10 on 2020-06-28 13:47

from django.db import migrations, models
import django.utils.timezone
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20200628_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', music.models.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', music.models.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('content', models.TextField(verbose_name='公告')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

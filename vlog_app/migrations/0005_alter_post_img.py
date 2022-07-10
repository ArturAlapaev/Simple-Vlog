# Generated by Django 4.0.4 on 2022-07-02 05:13

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('vlog_app', '0004_siteinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[400, 350], upload_to='photos/%Y/%m/%d', verbose_name='Пост'),
        ),
    ]

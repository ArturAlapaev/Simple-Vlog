# Generated by Django 4.0.4 on 2022-06-30 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog_app', '0003_contact_delete_contacts_alter_post_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название сайта')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок сайта')),
                ('description', models.CharField(max_length=500, verbose_name='Описание сайта')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания контакта')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления контакта')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
            ],
            options={
                'ordering': ('create_date',),
            },
        ),
    ]

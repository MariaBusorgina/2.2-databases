# Generated by Django 4.1.3 on 2022-12-11 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_article_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['-is_main', 'tag__name'], 'verbose_name': 'Раздел', 'verbose_name_plural': 'Тематика статьи'},
        ),
    ]

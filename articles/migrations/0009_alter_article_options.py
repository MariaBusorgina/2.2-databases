# Generated by Django 4.1.3 on 2022-12-11 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_scope_options_rename_title_tag_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
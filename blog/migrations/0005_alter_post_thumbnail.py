# Generated by Django 4.2.6 on 2023-10-13 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='posts/thumbnail/default.png', upload_to='posts/thumbnail/%Y/%m/%d/'),
        ),
    ]

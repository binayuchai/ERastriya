# Generated by Django 4.1.6 on 2023-04-27 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_post_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_hash',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, unique=True, upload_to='images/'),
        ),
    ]
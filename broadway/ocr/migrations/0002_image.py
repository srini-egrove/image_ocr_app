# Generated by Django 4.2.2 on 2023-06-20 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image_file', models.ImageField(upload_to='user_images/')),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80)),
                ('blog_title', models.CharField(max_length=100)),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='blog/media')),
                ('blog_article', models.TextField()),
                ('likes', models.CharField(max_length=100)),
                ('comments', models.TextField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='blog/media')),
                ('category', models.CharField(max_length=100)),
                ('createdat', models.DateTimeField()),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpost',
            name='post_type',
            field=models.CharField(blank=True, choices=[('post', 'Post'), ('reels', 'Reels')], max_length=5),
        ),
    ]

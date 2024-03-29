# Generated by Django 5.0.1 on 2024-01-09 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=100)),
                ('year', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='film/image')),
            ],
        ),
    ]

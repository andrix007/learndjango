# Generated by Django 4.2.5 on 2023-09-10 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=80)),
                ('zipcode', models.CharField(max_length=80)),
            ],
        ),
    ]

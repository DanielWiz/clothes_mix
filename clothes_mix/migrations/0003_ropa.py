# Generated by Django 2.2.7 on 2019-11-13 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes_mix', '0002_auto_20191102_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(null=True, upload_to='ropas')),
            ],
        ),
    ]

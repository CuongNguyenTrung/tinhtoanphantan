# Generated by Django 2.2.7 on 2019-12-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vchain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]
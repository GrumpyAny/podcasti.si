# Generated by Django 2.0.1 on 2018-01-21 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0003_auto_20180117_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(auto_now_add=True)),
                ('views', models.IntegerField(default=1)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='podcasts.Episode')),
            ],
        ),
    ]
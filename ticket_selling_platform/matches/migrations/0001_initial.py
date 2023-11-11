# Generated by Django 4.2.7 on 2023-11-10 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stadiums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_and_time', models.DateTimeField()),
                ('stadium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stadiums.stadium')),
            ],
            options={
                'unique_together': {('stadium', 'date_and_time')},
            },
        ),
    ]
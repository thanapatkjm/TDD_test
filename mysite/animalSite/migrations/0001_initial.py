# Generated by Django 2.1.1 on 2019-01-16 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('descript', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='animalSite.Animal')),
                ('food', models.TextField()),
                ('habitat', models.TextField()),
                ('legs', models.IntegerField(default=4)),
            ],
        ),
    ]

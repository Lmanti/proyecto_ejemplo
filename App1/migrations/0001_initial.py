# Generated by Django 4.1.3 on 2022-12-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]

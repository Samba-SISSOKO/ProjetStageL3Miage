# Generated by Django 4.0.4 on 2022-04-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBenevole', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connexions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse_mail', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]

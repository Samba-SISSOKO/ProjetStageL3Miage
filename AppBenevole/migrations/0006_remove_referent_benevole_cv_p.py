# Generated by Django 4.0.4 on 2022-05-13 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBenevole', '0005_remove_referent_benevole_cv_referent_benevole_cv_p'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referent_benevole',
            name='Cv_p',
        ),
    ]

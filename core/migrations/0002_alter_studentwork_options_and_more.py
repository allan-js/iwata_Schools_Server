# Generated by Django 5.1.3 on 2024-11-16 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentwork',
            options={'verbose_name': "Student's Work", 'verbose_name_plural': "Student's Works"},
        ),
        migrations.RenameField(
            model_name='studentwork',
            old_name='created',
            new_name='uploaded_on',
        ),
    ]
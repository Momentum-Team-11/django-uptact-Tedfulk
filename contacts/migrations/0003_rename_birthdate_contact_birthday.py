# Generated by Django 4.0.3 on 2022-03-03 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_birthdate_alter_contact_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='birthdate',
            new_name='birthday',
        ),
    ]

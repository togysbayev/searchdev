# Generated by Django 4.1.5 on 2023-01-30 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0005_alter_profile_user'),
        ('projects', '0002_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developers.profile'),
        ),
    ]

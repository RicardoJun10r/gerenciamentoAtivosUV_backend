# Generated by Django 4.1.7 on 2023-03-18 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eficiencia',
            name='localizacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eficiencia', to='tasks.localizacao'),
        ),
    ]

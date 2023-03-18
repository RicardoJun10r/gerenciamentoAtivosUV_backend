# Generated by Django 4.1.7 on 2023-03-18 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.BigIntegerField(db_column='longitude_col', null=True)),
                ('latitude', models.BigIntegerField(db_column='latitude_col', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eficiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(db_column='mes_col', max_length=20)),
                ('porcentagem', models.BigIntegerField(db_column='eficiencia_col')),
                ('localizacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eficiencia', to='tasks.localizacao')),
            ],
        ),
    ]

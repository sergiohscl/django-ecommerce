# Generated by Django 5.0.1 on 2024-02-17 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_alter_perfil_endereco_alter_perfil_numero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cpf',
            field=models.CharField(max_length=15),
        ),
    ]
# Generated by Django 5.0.1 on 2024-02-02 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_alter_variacao_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variacao',
            options={'verbose_name': 'Variação', 'verbose_name_plural': 'Variações'},
        ),
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('V', 'Variável'), ('S', 'Simples')], default='V', max_length=1),
        ),
    ]
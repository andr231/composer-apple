# Generated by Django 2.0.10 on 2019-02-16 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_carritocompras_identificador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carritocompras',
            name='datos_payu',
            field=models.TextField(),
        ),
    ]

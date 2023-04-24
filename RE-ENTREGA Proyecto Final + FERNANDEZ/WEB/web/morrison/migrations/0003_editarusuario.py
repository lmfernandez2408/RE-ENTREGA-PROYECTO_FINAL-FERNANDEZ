# Generated by Django 4.2 on 2023-04-24 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morrison', '0002_rename_description_mapa_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditarUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de usuario')),
                ('email', models.TextField(null=True, verbose_name='E-mail')),
            ],
        ),
    ]
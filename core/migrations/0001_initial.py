# Generated by Django 3.2 on 2021-04-19 14:40

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('imagem', stdimage.models.StdImageField(upload_to='servicos', verbose_name='Imagem')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descricao')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('biografia', models.TextField(max_length=1000, verbose_name='Bio')),
                ('foto', stdimage.models.StdImageField(upload_to='equipe', verbose_name='Foto')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Face')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Insta')),
                ('cargo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.cargo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

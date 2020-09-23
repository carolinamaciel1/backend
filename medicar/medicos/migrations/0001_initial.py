# Generated by Django 3.1.1 on 2020-09-16 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('especialidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('crm', models.CharField(max_length=13, verbose_name='CRM')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('telefone', models.CharField(blank=True, max_length=11, null=True, verbose_name='Telefone')),
                ('especialidade', models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='especialidades.especialidade')),
            ],
        ),
    ]

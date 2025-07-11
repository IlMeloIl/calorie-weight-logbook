# Generated by Django 5.2.4 on 2025-07-08 23:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome do exercício', max_length=100)),
                ('description', models.TextField(blank=True, help_text='Descrição do exercício')),
                ('user', models.ForeignKey(blank=True, help_text='Usuário criador (deixe vazio para exercícios globais)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome da rotina', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routines', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RoutineExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(help_text='Ordem do exercício na rotina')),
                ('sets', models.PositiveIntegerField(help_text='Número de séries planejadas')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logbook.exercise')),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routine_exercises', to='logbook.routine')),
            ],
            options={
                'ordering': ['order'],
                'unique_together': {('routine', 'exercise')},
            },
        ),
    ]

# Generated by Django 3.2.16 on 2023-01-03 14:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('phytomorphology', '0005_auto_20230103_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutumnLeavesColour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Белый', 'Белый'), ('Бронзоватый', 'Бронзоватый'), ('Голубой', 'Голубой'), ('Желтый', 'Желтый'), ('Зеленый', 'Зеленый'), ('Красный', 'Красный'), ('Оранжевый', 'Оранжевый'), ('Розовый', 'Розовый'), ('Серебристый', 'Серебристый'), ('Серый', 'Серый'), ('Сизый', 'Сизый'), ('Синий', 'Синий'), ('Фиолетовый', 'Фиолетовый')], default=uuid.uuid1, max_length=50, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Осенняя окраска листьев',
                'verbose_name_plural': 'Осенняя окраска листьев',
            },
        ),
        migrations.AlterField(
            model_name='leavescolour',
            name='name',
            field=models.CharField(choices=[('Белый', 'Белый'), ('Бронзоватый', 'Бронзоватый'), ('Голубой', 'Голубой'), ('Желтый', 'Желтый'), ('Зеленый', 'Зеленый'), ('Красный', 'Красный'), ('Оранжевый', 'Оранжевый'), ('Розовый', 'Розовый'), ('Серебристый', 'Серебристый'), ('Серый', 'Серый'), ('Сизый', 'Сизый'), ('Синий', 'Синий'), ('Фиолетовый', 'Фиолетовый')], default=uuid.uuid1, max_length=50, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='youngleavescolour',
            name='name',
            field=models.CharField(choices=[('Белый', 'Белый'), ('Бронзоватый', 'Бронзоватый'), ('Голубой', 'Голубой'), ('Желтый', 'Желтый'), ('Зеленый', 'Зеленый'), ('Красный', 'Красный'), ('Оранжевый', 'Оранжевый'), ('Розовый', 'Розовый'), ('Серебристый', 'Серебристый'), ('Серый', 'Серый'), ('Сизый', 'Сизый'), ('Синий', 'Синий'), ('Фиолетовый', 'Фиолетовый')], default=uuid.uuid1, max_length=50, unique=True, verbose_name='Name'),
        ),
    ]

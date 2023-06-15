# Generated by Django 3.2.16 on 2023-01-03 15:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('phytomorphology', '0008_auto_20230103_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autumnleavescolour',
            name='name',
            field=models.CharField(choices=[('Белый', 'Белый'), ('Бронзоватый', 'Бронзоватый'), ('Голубой', 'Голубой'), ('Желтый', 'Желтый'), ('Зеленый', 'Зеленый'), ('Коричневый', 'Коричневый'), ('Красный', 'Красный'), ('Оранжевый', 'Оранжевый'), ('Розовый', 'Розовый'), ('Серебристый', 'Серебристый'), ('Серый', 'Серый'), ('Сизый', 'Сизый'), ('Синий', 'Синий'), ('Фиолетовый', 'Фиолетовый'), ('Черный', 'Черный')], default=uuid.uuid1, max_length=50, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='bloomcolour',
            name='name',
            field=models.CharField(choices=[('Белый', 'Белый'), ('Бронзоватый', 'Бронзоватый'), ('Голубой', 'Голубой'), ('Желтый', 'Желтый'), ('Зеленый', 'Зеленый'), ('Коричневый', 'Коричневый'), ('Красный', 'Красный'), ('Оранжевый', 'Оранжевый'), ('Розовый', 'Розовый'), ('Серебристый', 'Серебристый'), ('Серый', 'Серый'), ('Сизый', 'Сизый'), ('Синий', 'Синий'), ('Фиолетовый', 'Фиолетовый'), ('Черный', 'Черный'), ('Не являются декоративными', 'Не являются декоративными'), ('Отсутствуют', 'Отсутствуют')], default=uuid.uuid1, max_length=50, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='bloomingperiod',
            name='name',
            field=models.CharField(choices=[('Январь', 'Январь'), ('Февраль', 'Февраль'), ('Март', 'Март'), ('Апрель', 'Апрель'), ('Май', 'Май'), ('Июнь', 'Июнь'), ('Июль', 'Июль'), ('Август', 'Август'), ('Сентябрь', 'Сентябрь'), ('Октябрь', 'Октябрь'), ('Ноябрь', 'Ноябрь'), ('Декабрь', 'Декабрь'), ('Отсутствуют', 'Отсутствуют')], default=uuid.uuid1, max_length=50, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='leavescolour',
            name='name',
            field=models.CharField(choices=[('Белый', 'Белый'), ('Бронзоватый', 'Бронзоватый'), ('Голубой', 'Голубой'), ('Желтый', 'Желтый'), ('Зеленый', 'Зеленый'), ('Коричневый', 'Коричневый'), ('Красный', 'Красный'), ('Оранжевый', 'Оранжевый'), ('Розовый', 'Розовый'), ('Серебристый', 'Серебристый'), ('Серый', 'Серый'), ('Сизый', 'Сизый'), ('Синий', 'Синий'), ('Фиолетовый', 'Фиолетовый'), ('Черный', 'Черный')], default=uuid.uuid1, max_length=50, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='youngleavescolour',
            name='name',
            field=models.CharField(choices=[('Белый', 'Белый'), ('Бронзоватый', 'Бронзоватый'), ('Голубой', 'Голубой'), ('Желтый', 'Желтый'), ('Зеленый', 'Зеленый'), ('Коричневый', 'Коричневый'), ('Красный', 'Красный'), ('Оранжевый', 'Оранжевый'), ('Розовый', 'Розовый'), ('Серебристый', 'Серебристый'), ('Серый', 'Серый'), ('Сизый', 'Сизый'), ('Синий', 'Синий'), ('Фиолетовый', 'Фиолетовый'), ('Черный', 'Черный')], default=uuid.uuid1, max_length=50, unique=True, verbose_name='Name'),
        ),
    ]
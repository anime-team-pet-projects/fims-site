# Generated by Django 4.0.4 on 2022-05-30 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название награды')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/award/%Y/%m/%d', verbose_name='Фото награды')),
                ('description', models.TextField(max_length=1024, verbose_name='Описание награды')),
                ('year', models.PositiveIntegerField(verbose_name='Год выпуска награды')),
            ],
            options={
                'verbose_name': 'Награда',
                'verbose_name_plural': 'Награды',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Название жанра')),
                ('description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Описание жанра')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/people/%Y/%m/%d', verbose_name='Фото')),
                ('date_of_birth', models.PositiveIntegerField(verbose_name='Дата рождения')),
                ('award', models.ManyToManyField(blank=True, to='film.award', verbose_name='Награды')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
            },
        ),
        migrations.CreateModel(
            name='SuggestedFilm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('cover', models.ImageField(blank=True, help_text='Большой постер фильма(рекомендуемый размер загрузки - 485x600)', null=True, upload_to='photo/cover/%Y/%m/%d', verbose_name='Основная обложка фильма')),
                ('cover_mini', models.ImageField(blank=True, help_text='Маленький постер фильма, который можно указать в лентепользователя или в категории - "ТОП - 10"(рекомендуемый размерзагрузки- 259x29)', null=True, upload_to='photo/cover_mini/%Y/%m/%d', verbose_name='Миниатюрная обложка фильма')),
                ('description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Описание фильма')),
                ('country', models.CharField(blank=True, max_length=255, null=True, verbose_name='Страна производства')),
                ('year', models.PositiveIntegerField(verbose_name='Год выпуска фильма')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возростное ограничение')),
                ('time', models.FloatField(blank=True, null=True, verbose_name='Время показа')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовать в релиз')),
                ('awards', models.ManyToManyField(blank=True, to='film.award', verbose_name='Награды фильма')),
                ('genre', models.ManyToManyField(blank=True, to='film.genre', verbose_name='Жанры фильма')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор предложения')),
                ('starring', models.ManyToManyField(blank=True, related_name='starring_userfilm', to='film.people', verbose_name='Главные актеры')),
            ],
            options={
                'verbose_name': 'Предложенный фильм',
                'verbose_name_plural': 'Преложенные фильмы',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('cover', models.ImageField(blank=True, help_text='Большой постер фильма(рекомендуемый размер загрузки - 485x600)', null=True, upload_to='photo/cover/%Y/%m/%d', verbose_name='Основная обложка фильма')),
                ('cover_mini', models.ImageField(blank=True, help_text='Маленький постер фильма, который можно указать в лентепользователя или в категории - "ТОП - 10"(рекомендуемый размерзагрузки- 259x29)', null=True, upload_to='photo/cover_mini/%Y/%m/%d', verbose_name='Миниатюрная обложка фильма')),
                ('description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Описание фильма')),
                ('country', models.CharField(blank=True, max_length=255, null=True, verbose_name='Страна производства')),
                ('year', models.PositiveIntegerField(verbose_name='Год выпуска фильма')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возростное ограничение')),
                ('time', models.FloatField(blank=True, null=True, verbose_name='Время показа')),
                ('rating', models.CharField(blank=True, help_text='Рейтинг филмьа согласно какому-либо изданию(кинопоиск и тд...)', max_length=255, null=True, verbose_name='Рэйтинг')),
                ('awards', models.ManyToManyField(blank=True, to='film.award', verbose_name='Награды фильма')),
                ('genre', models.ManyToManyField(blank=True, to='film.genre', verbose_name='Жанры фильма')),
                ('starring', models.ManyToManyField(blank=True, related_name='starring', to='film.people', verbose_name='Главные актеры')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=1024, verbose_name='Тело текста')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания комментария')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего обновления комментария')),
                ('active', models.BooleanField(default=True, verbose_name='Состояние комментария')),
                ('rating', models.CharField(blank=True, choices=[('1', 'terribly'), ('2', 'bad'), ('3', 'ok'), ('4', 'good'), ('5', 'amazing')], max_length=25, null=True, verbose_name='Рейтинг фильма')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='film.film', verbose_name='Комменитрованный фильм')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='film.comment', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
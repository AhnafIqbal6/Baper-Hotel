from django.contrib import admin

# Register your models here.
# Generated by Django 3.2.9 on 2022-07-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_cuisine_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('secondary_description', models.TextField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='food_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='food.cuisine')),
            ],
        ),
    ]
# Generated by Django 3.2.9 on 2022-07-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_cuisine_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('secondary_description', models.TextField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='food_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='food.cuisine')),
            ],
        ),
    ]
# Generated by Django 3.2.9 on 2022-07-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_cuisine_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('secondary_description', models.TextField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='food_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='food.cuisine')),
            ],
        ),
    ]
# Generated by Django 3.2.9 on 2022-07-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migrat# Generated by Django 3.2.9 on 2022-07-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
# Generated by Django 3.2.9 on 2022-07-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migrat# Generated by Django 3.2.9 on 2022-07-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_cuisine_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('secondary_description', models.TextField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='food_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='food.cuisine')),
            ],
        ),
    ]
ion(migrations.Migration):

    dependencies = [
        ('food', '0002_cuisine_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('secondary_description', models.TextField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='food_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='food.cuisine')),
            ],
        ),
    ]
# Generated by Django 3.2.9 on 2022-07-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_cuisine_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('secondary_description', models.TextField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='food_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='food.cuisine')),
            ],
        ),
    ]

    dependencies = [
        ('food', '0002_cuisine_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('secondary_description', models.TextField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='food_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='food.cuisine')),
            ],
        ),
    ]
# Generated by Django 3.2.9 on 2022-07-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_cuisine_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('secondary_description', models.TextField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='food_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='food.cuisine')),
            ],
        ),
    ]
# Generated by Django 3.2.9 on 2022-07-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_cuisine_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('secondary_description', models.TextField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='food_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='food.cuisine')),
            ],
        ),
    ]
ion(migrations.Migration):

    dependencies = [
        ('food', '0002_cuisine_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('secondary_description', models.TextField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='food_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='food.cuisine')),
            ],
        ),
    ]
# Generated by Django 3.2.9 on 2022-07-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_cuisine_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('secondary_description', models.TextField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='food_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='food.cuisine')),
            ],
        ),
    ]
# Generated by Django 3.2.9 on 2022-07-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_cuisine_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('secondary_description', models.TextField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='food_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='food.cuisine')),
            ],
        ),
    ]
# Generated by Django 3.2.9 on 2022-07-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_cuisine_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('secondary_description', models.TextField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='food_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='food.cuisine')),
            ],
        ),
    ]

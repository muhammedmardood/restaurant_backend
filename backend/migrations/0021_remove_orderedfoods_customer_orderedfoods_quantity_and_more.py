# Generated by Django 4.0 on 2022-01-21 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_alter_category_options_alter_orderedfoods_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedfoods',
            name='customer',
        ),
        migrations.AddField(
            model_name='orderedfoods',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='orderedfoods',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.RemoveField(
            model_name='orderedfoods',
            name='food',
        ),
        migrations.AddField(
            model_name='orderedfoods',
            name='food',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='food', to='backend.food'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('order_id', models.CharField(max_length=200, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.customer')),
            ],
        ),
        migrations.AddField(
            model_name='orderedfoods',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.order'),
        ),
    ]

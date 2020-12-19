# Generated by Django 2.2 on 2020-12-19 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plant', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='delivered', max_length=50)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField()),
                ('price_each', models.DecimalField(decimal_places=2, max_digits=5)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='plant.Plant')),
            ],
        ),
    ]

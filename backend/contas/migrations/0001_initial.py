from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiroNome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('matricula', models.CharField(max_length=20, unique=True)),
                ('saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiroNome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('matricula', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]

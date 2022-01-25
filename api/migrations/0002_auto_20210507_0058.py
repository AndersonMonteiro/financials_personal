# Generated by Django 3.2 on 2021-05-07 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoAcesso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30, unique=True)),
                ('data_cadastro', models.DateTimeField(null=True)),
                ('data_atualizacao', models.DateTimeField(null=True)),
                ('perfil_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='responsavel_grupo_acesso', to='api.perfil')),
            ],
            options={
                'db_table': 'grupo_acesso',
                'ordering': ('data_cadastro',),
            },
        ),
        migrations.CreateModel(
            name='TipoGrupoAcesso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'tipo_grupo_acesso',
            },
        ),
        migrations.AlterField(
            model_name='comentario',
            name='perfil_responsavel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='responsavel_comentario', to='api.perfil'),
        ),
        migrations.AlterField(
            model_name='metafinanceira',
            name='perfil_responsavel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='responsavel_meta', to='api.perfil'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='perfil_responsavel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='responsavel_orcamento', to='api.perfil'),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='conta_destino',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='conta_destino_pagamento', to='api.conta'),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='conta_origem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='conta_origem_pagamento', to='api.conta'),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='perfil_responsavel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='responsavel_pagamento', to='api.perfil'),
        ),
        migrations.CreateModel(
            name='ParticipanteGrupoAcesso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edicao_ativo', models.BooleanField(default=True)),
                ('data_cadastro', models.DateTimeField(null=True)),
                ('data_atualizacao', models.DateTimeField(null=True)),
                ('grupo_acesso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.grupoacesso')),
                ('perfil_participante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='responsavel_participante', to='api.perfil')),
            ],
            options={
                'db_table': 'participante_grupo_acesso',
                'ordering': ('data_cadastro',),
            },
        ),
        migrations.AddField(
            model_name='grupoacesso',
            name='tipo_grupo_acesso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.tipogrupoacesso'),
        ),
        migrations.AddField(
            model_name='conta',
            name='grupo_acesso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.grupoacesso'),
        ),
        migrations.AddField(
            model_name='historical_movimentacao',
            name='grupo_acesso',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api.grupoacesso'),
        ),
        migrations.AddField(
            model_name='movimentacao',
            name='grupo_acesso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.grupoacesso'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='grupo_acesso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.grupoacesso'),
        ),
    ]

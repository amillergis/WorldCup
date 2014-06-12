# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'worldcuppool_user', (
            ('userID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=254)),
        ))
        db.send_create_signal(u'worldcuppool', ['User'])

        # Adding M2M table for field team1 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team1')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding M2M table for field team2 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team2')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding M2M table for field team3 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team3')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding M2M table for field team4 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team4')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding M2M table for field team5 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team5')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding M2M table for field team6 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team6')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding M2M table for field team7 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team7')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding M2M table for field team8 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team8')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding M2M table for field team9 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team9')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding M2M table for field team10 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team10')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding M2M table for field team11 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team11')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding M2M table for field team12 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team12')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding M2M table for field team13 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team13')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding M2M table for field team14 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team14')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding M2M table for field team15 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team15')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding M2M table for field team16 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team16')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding model 'Team'
        db.create_table(u'worldcuppool_team', (
            ('teamID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('advanced', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('knockout_wins', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'worldcuppool', ['Team'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'worldcuppool_user')

        # Removing M2M table for field team1 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team1'))

        # Removing M2M table for field team2 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team2'))

        # Removing M2M table for field team3 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team3'))

        # Removing M2M table for field team4 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team4'))

        # Removing M2M table for field team5 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team5'))

        # Removing M2M table for field team6 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team6'))

        # Removing M2M table for field team7 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team7'))

        # Removing M2M table for field team8 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team8'))

        # Removing M2M table for field team9 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team9'))

        # Removing M2M table for field team10 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team10'))

        # Removing M2M table for field team11 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team11'))

        # Removing M2M table for field team12 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team12'))

        # Removing M2M table for field team13 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team13'))

        # Removing M2M table for field team14 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team14'))

        # Removing M2M table for field team15 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team15'))

        # Removing M2M table for field team16 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team16'))

        # Deleting model 'Team'
        db.delete_table(u'worldcuppool_team')


    models = {
        u'worldcuppool.team': {
            'Meta': {'object_name': 'Team'},
            'advanced': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'knockout_wins': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'teamID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'worldcuppool.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'team1': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_pick_1'", 'symmetrical': 'False', 'to': u"orm['worldcuppool.Team']"}),
            'team10': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_pick_10'", 'symmetrical': 'False', 'to': u"orm['worldcuppool.Team']"}),
            'team11': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_pick_11'", 'symmetrical': 'False', 'to': u"orm['worldcuppool.Team']"}),
            'team12': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_pick_12'", 'symmetrical': 'False', 'to': u"orm['worldcuppool.Team']"}),
            'team13': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_pick_13'", 'symmetrical': 'False', 'to': u"orm['worldcuppool.Team']"}),
            'team14': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_pick_14'", 'symmetrical': 'False', 'to': u"orm['worldcuppool.Team']"}),
            'team15': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_pick_15'", 'symmetrical': 'False', 'to': u"orm['worldcuppool.Team']"}),
            'team16': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_pick_16'", 'symmetrical': 'False', 'to': u"orm['worldcuppool.Team']"}),
            'team2': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_pick_2'", 'symmetrical': 'False', 'to': u"orm['worldcuppool.Team']"}),
            'team3': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_pick_3'", 'symmetrical': 'False', 'to': u"orm['worldcuppool.Team']"}),
            'team4': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_pick_4'", 'symmetrical': 'False', 'to': u"orm['worldcuppool.Team']"}),
            'team5': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_pick_5'", 'symmetrical': 'False', 'to': u"orm['worldcuppool.Team']"}),
            'team6': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_pick_6'", 'symmetrical': 'False', 'to': u"orm['worldcuppool.Team']"}),
            'team7': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_pick_7'", 'symmetrical': 'False', 'to': u"orm['worldcuppool.Team']"}),
            'team8': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_pick_8'", 'symmetrical': 'False', 'to': u"orm['worldcuppool.Team']"}),
            'team9': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_pick_9'", 'symmetrical': 'False', 'to': u"orm['worldcuppool.Team']"}),
            'userID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['worldcuppool']
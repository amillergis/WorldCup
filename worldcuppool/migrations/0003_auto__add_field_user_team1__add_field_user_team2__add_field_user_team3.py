# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.team1'
        db.add_column(u'worldcuppool_user', 'team1',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_1', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team2'
        db.add_column(u'worldcuppool_user', 'team2',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_2', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team3'
        db.add_column(u'worldcuppool_user', 'team3',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_3', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team4'
        db.add_column(u'worldcuppool_user', 'team4',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_4', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team5'
        db.add_column(u'worldcuppool_user', 'team5',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_5', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team6'
        db.add_column(u'worldcuppool_user', 'team6',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_6', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team7'
        db.add_column(u'worldcuppool_user', 'team7',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_7', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team8'
        db.add_column(u'worldcuppool_user', 'team8',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_8', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team9'
        db.add_column(u'worldcuppool_user', 'team9',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_9', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team10'
        db.add_column(u'worldcuppool_user', 'team10',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_10', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team11'
        db.add_column(u'worldcuppool_user', 'team11',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_11', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team12'
        db.add_column(u'worldcuppool_user', 'team12',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_12', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team13'
        db.add_column(u'worldcuppool_user', 'team13',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_13', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team14'
        db.add_column(u'worldcuppool_user', 'team14',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_14', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team15'
        db.add_column(u'worldcuppool_user', 'team15',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_15', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team16'
        db.add_column(u'worldcuppool_user', 'team16',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_16', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Removing M2M table for field team7 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team7'))

        # Removing M2M table for field team8 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team8'))

        # Removing M2M table for field team16 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team16'))

        # Removing M2M table for field team5 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team5'))

        # Removing M2M table for field team14 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team14'))

        # Removing M2M table for field team15 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team15'))

        # Removing M2M table for field team12 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team12'))

        # Removing M2M table for field team1 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team1'))

        # Removing M2M table for field team10 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team10'))

        # Removing M2M table for field team11 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team11'))

        # Removing M2M table for field team4 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team4'))

        # Removing M2M table for field team2 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team2'))

        # Removing M2M table for field team6 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team6'))

        # Removing M2M table for field team3 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team3'))

        # Removing M2M table for field team13 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team13'))

        # Removing M2M table for field team9 on 'User'
        db.delete_table(db.shorten_name(u'worldcuppool_user_team9'))


    def backwards(self, orm):
        # Deleting field 'User.team1'
        db.delete_column(u'worldcuppool_user', 'team1_id')

        # Deleting field 'User.team2'
        db.delete_column(u'worldcuppool_user', 'team2_id')

        # Deleting field 'User.team3'
        db.delete_column(u'worldcuppool_user', 'team3_id')

        # Deleting field 'User.team4'
        db.delete_column(u'worldcuppool_user', 'team4_id')

        # Deleting field 'User.team5'
        db.delete_column(u'worldcuppool_user', 'team5_id')

        # Deleting field 'User.team6'
        db.delete_column(u'worldcuppool_user', 'team6_id')

        # Deleting field 'User.team7'
        db.delete_column(u'worldcuppool_user', 'team7_id')

        # Deleting field 'User.team8'
        db.delete_column(u'worldcuppool_user', 'team8_id')

        # Deleting field 'User.team9'
        db.delete_column(u'worldcuppool_user', 'team9_id')

        # Deleting field 'User.team10'
        db.delete_column(u'worldcuppool_user', 'team10_id')

        # Deleting field 'User.team11'
        db.delete_column(u'worldcuppool_user', 'team11_id')

        # Deleting field 'User.team12'
        db.delete_column(u'worldcuppool_user', 'team12_id')

        # Deleting field 'User.team13'
        db.delete_column(u'worldcuppool_user', 'team13_id')

        # Deleting field 'User.team14'
        db.delete_column(u'worldcuppool_user', 'team14_id')

        # Deleting field 'User.team15'
        db.delete_column(u'worldcuppool_user', 'team15_id')

        # Deleting field 'User.team16'
        db.delete_column(u'worldcuppool_user', 'team16_id')

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

        # Adding M2M table for field team16 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team16')
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

        # Adding M2M table for field team12 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team12')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'worldcuppool.user'], null=False)),
            ('team', models.ForeignKey(orm[u'worldcuppool.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'team_id'])

        # Adding M2M table for field team1 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team1')
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

        # Adding M2M table for field team4 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team4')
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

        # Adding M2M table for field team6 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team6')
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

        # Adding M2M table for field team13 on 'User'
        m2m_table_name = db.shorten_name(u'worldcuppool_user_team13')
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
            'team1': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_1'", 'to': u"orm['worldcuppool.Team']"}),
            'team10': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_10'", 'to': u"orm['worldcuppool.Team']"}),
            'team11': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_11'", 'to': u"orm['worldcuppool.Team']"}),
            'team12': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_12'", 'to': u"orm['worldcuppool.Team']"}),
            'team13': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_13'", 'to': u"orm['worldcuppool.Team']"}),
            'team14': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_14'", 'to': u"orm['worldcuppool.Team']"}),
            'team15': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_15'", 'to': u"orm['worldcuppool.Team']"}),
            'team16': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_16'", 'to': u"orm['worldcuppool.Team']"}),
            'team2': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_2'", 'to': u"orm['worldcuppool.Team']"}),
            'team3': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_3'", 'to': u"orm['worldcuppool.Team']"}),
            'team4': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_4'", 'to': u"orm['worldcuppool.Team']"}),
            'team5': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_5'", 'to': u"orm['worldcuppool.Team']"}),
            'team6': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_6'", 'to': u"orm['worldcuppool.Team']"}),
            'team7': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_7'", 'to': u"orm['worldcuppool.Team']"}),
            'team8': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_8'", 'to': u"orm['worldcuppool.Team']"}),
            'team9': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_9'", 'to': u"orm['worldcuppool.Team']"}),
            'userID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['worldcuppool']
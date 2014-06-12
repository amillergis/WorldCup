# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.team7'
        db.delete_column(u'worldcuppool_user', 'team7_id')

        # Deleting field 'User.team8'
        db.delete_column(u'worldcuppool_user', 'team8_id')

        # Deleting field 'User.team16'
        db.delete_column(u'worldcuppool_user', 'team16_id')

        # Deleting field 'User.team5'
        db.delete_column(u'worldcuppool_user', 'team5_id')

        # Deleting field 'User.team14'
        db.delete_column(u'worldcuppool_user', 'team14_id')

        # Deleting field 'User.team15'
        db.delete_column(u'worldcuppool_user', 'team15_id')

        # Deleting field 'User.team12'
        db.delete_column(u'worldcuppool_user', 'team12_id')

        # Deleting field 'User.team1'
        db.delete_column(u'worldcuppool_user', 'team1_id')

        # Deleting field 'User.team10'
        db.delete_column(u'worldcuppool_user', 'team10_id')

        # Deleting field 'User.team11'
        db.delete_column(u'worldcuppool_user', 'team11_id')

        # Deleting field 'User.team4'
        db.delete_column(u'worldcuppool_user', 'team4_id')

        # Deleting field 'User.team2'
        db.delete_column(u'worldcuppool_user', 'team2_id')

        # Deleting field 'User.team6'
        db.delete_column(u'worldcuppool_user', 'team6_id')

        # Deleting field 'User.team3'
        db.delete_column(u'worldcuppool_user', 'team3_id')

        # Deleting field 'User.team13'
        db.delete_column(u'worldcuppool_user', 'team13_id')

        # Deleting field 'User.team9'
        db.delete_column(u'worldcuppool_user', 'team9_id')

        # Adding field 'User.pick1'
        db.add_column(u'worldcuppool_user', 'pick1',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_1', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.pick2'
        db.add_column(u'worldcuppool_user', 'pick2',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_2', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.pick3'
        db.add_column(u'worldcuppool_user', 'pick3',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_3', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.pick4'
        db.add_column(u'worldcuppool_user', 'pick4',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_4', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.pick5'
        db.add_column(u'worldcuppool_user', 'pick5',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_5', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.pick6'
        db.add_column(u'worldcuppool_user', 'pick6',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_6', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.pick7'
        db.add_column(u'worldcuppool_user', 'pick7',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_7', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.pick8'
        db.add_column(u'worldcuppool_user', 'pick8',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_8', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.pick9'
        db.add_column(u'worldcuppool_user', 'pick9',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_9', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.pick10'
        db.add_column(u'worldcuppool_user', 'pick10',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_10', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.pick11'
        db.add_column(u'worldcuppool_user', 'pick11',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_11', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.pick12'
        db.add_column(u'worldcuppool_user', 'pick12',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_12', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.pick13'
        db.add_column(u'worldcuppool_user', 'pick13',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_13', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.pick14'
        db.add_column(u'worldcuppool_user', 'pick14',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_14', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.pick15'
        db.add_column(u'worldcuppool_user', 'pick15',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_15', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.pick16'
        db.add_column(u'worldcuppool_user', 'pick16',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_16', to=orm['worldcuppool.Team']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'User.team7'
        db.add_column(u'worldcuppool_user', 'team7',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_7', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team8'
        db.add_column(u'worldcuppool_user', 'team8',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_8', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team16'
        db.add_column(u'worldcuppool_user', 'team16',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_16', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team5'
        db.add_column(u'worldcuppool_user', 'team5',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_5', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team14'
        db.add_column(u'worldcuppool_user', 'team14',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_14', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team15'
        db.add_column(u'worldcuppool_user', 'team15',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_15', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team12'
        db.add_column(u'worldcuppool_user', 'team12',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_12', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team1'
        db.add_column(u'worldcuppool_user', 'team1',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_1', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team10'
        db.add_column(u'worldcuppool_user', 'team10',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_10', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team11'
        db.add_column(u'worldcuppool_user', 'team11',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_11', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team4'
        db.add_column(u'worldcuppool_user', 'team4',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_4', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team2'
        db.add_column(u'worldcuppool_user', 'team2',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_2', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team6'
        db.add_column(u'worldcuppool_user', 'team6',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_6', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team3'
        db.add_column(u'worldcuppool_user', 'team3',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_3', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team13'
        db.add_column(u'worldcuppool_user', 'team13',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_13', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Adding field 'User.team9'
        db.add_column(u'worldcuppool_user', 'team9',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='user_pick_9', to=orm['worldcuppool.Team']),
                      keep_default=False)

        # Deleting field 'User.pick1'
        db.delete_column(u'worldcuppool_user', 'pick1_id')

        # Deleting field 'User.pick2'
        db.delete_column(u'worldcuppool_user', 'pick2_id')

        # Deleting field 'User.pick3'
        db.delete_column(u'worldcuppool_user', 'pick3_id')

        # Deleting field 'User.pick4'
        db.delete_column(u'worldcuppool_user', 'pick4_id')

        # Deleting field 'User.pick5'
        db.delete_column(u'worldcuppool_user', 'pick5_id')

        # Deleting field 'User.pick6'
        db.delete_column(u'worldcuppool_user', 'pick6_id')

        # Deleting field 'User.pick7'
        db.delete_column(u'worldcuppool_user', 'pick7_id')

        # Deleting field 'User.pick8'
        db.delete_column(u'worldcuppool_user', 'pick8_id')

        # Deleting field 'User.pick9'
        db.delete_column(u'worldcuppool_user', 'pick9_id')

        # Deleting field 'User.pick10'
        db.delete_column(u'worldcuppool_user', 'pick10_id')

        # Deleting field 'User.pick11'
        db.delete_column(u'worldcuppool_user', 'pick11_id')

        # Deleting field 'User.pick12'
        db.delete_column(u'worldcuppool_user', 'pick12_id')

        # Deleting field 'User.pick13'
        db.delete_column(u'worldcuppool_user', 'pick13_id')

        # Deleting field 'User.pick14'
        db.delete_column(u'worldcuppool_user', 'pick14_id')

        # Deleting field 'User.pick15'
        db.delete_column(u'worldcuppool_user', 'pick15_id')

        # Deleting field 'User.pick16'
        db.delete_column(u'worldcuppool_user', 'pick16_id')


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
            'pick1': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_1'", 'to': u"orm['worldcuppool.Team']"}),
            'pick10': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_10'", 'to': u"orm['worldcuppool.Team']"}),
            'pick11': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_11'", 'to': u"orm['worldcuppool.Team']"}),
            'pick12': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_12'", 'to': u"orm['worldcuppool.Team']"}),
            'pick13': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_13'", 'to': u"orm['worldcuppool.Team']"}),
            'pick14': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_14'", 'to': u"orm['worldcuppool.Team']"}),
            'pick15': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_15'", 'to': u"orm['worldcuppool.Team']"}),
            'pick16': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_16'", 'to': u"orm['worldcuppool.Team']"}),
            'pick2': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_2'", 'to': u"orm['worldcuppool.Team']"}),
            'pick3': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_3'", 'to': u"orm['worldcuppool.Team']"}),
            'pick4': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_4'", 'to': u"orm['worldcuppool.Team']"}),
            'pick5': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_5'", 'to': u"orm['worldcuppool.Team']"}),
            'pick6': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_6'", 'to': u"orm['worldcuppool.Team']"}),
            'pick7': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_7'", 'to': u"orm['worldcuppool.Team']"}),
            'pick8': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_8'", 'to': u"orm['worldcuppool.Team']"}),
            'pick9': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'user_pick_9'", 'to': u"orm['worldcuppool.Team']"}),
            'userID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['worldcuppool']
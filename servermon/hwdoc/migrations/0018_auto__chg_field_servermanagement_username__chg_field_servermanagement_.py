# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ServerManagement.username'
        db.alter_column('hwdoc_servermanagement', 'username', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True))

        # Changing field 'ServerManagement.license'
        db.alter_column('hwdoc_servermanagement', 'license', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True))

        # Changing field 'ServerManagement.raid_license'
        db.alter_column('hwdoc_servermanagement', 'raid_license', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True))

        # Changing field 'ServerManagement.mac'
        db.alter_column('hwdoc_servermanagement', 'mac', self.gf('django.db.models.fields.CharField')(max_length=17, blank=True))

        # Changing field 'ServerManagement.password'
        db.alter_column('hwdoc_servermanagement', 'password', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True))

        # Changing field 'Equipment.comments'
        db.alter_column('hwdoc_equipment', 'comments', self.gf('django.db.models.fields.TextField')(blank=True))

        # Changing field 'Equipment.purpose'
        db.alter_column('hwdoc_equipment', 'purpose', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True))


    def backwards(self, orm):

        # Changing field 'ServerManagement.username'
        db.alter_column('hwdoc_servermanagement', 'username', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True))

        # Changing field 'ServerManagement.license'
        db.alter_column('hwdoc_servermanagement', 'license', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True))

        # Changing field 'ServerManagement.raid_license'
        db.alter_column('hwdoc_servermanagement', 'raid_license', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True))

        # Changing field 'ServerManagement.mac'
        db.alter_column('hwdoc_servermanagement', 'mac', self.gf('django.db.models.fields.CharField')(max_length=17, null=True, blank=True))

        # Changing field 'ServerManagement.password'
        db.alter_column('hwdoc_servermanagement', 'password', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True))

        # Changing field 'Equipment.comments'
        db.alter_column('hwdoc_equipment', 'comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True))

        # Changing field 'Equipment.purpose'
        db.alter_column('hwdoc_equipment', 'purpose', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True))


    models = {
        'hwdoc.datacenter': {
            'Meta': {'object_name': 'Datacenter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'hwdoc.email': {
            'Meta': {'object_name': 'Email'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'hwdoc.equipment': {
            'Meta': {'object_name': 'Equipment'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'allocation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hwdoc.Project']", 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hwdoc.EquipmentModel']"}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'rack': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hwdoc.Rack']", 'null': 'True', 'blank': 'True'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'unit': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'hwdoc.equipmentmodel': {
            'Meta': {'object_name': 'EquipmentModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'u': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hwdoc.Vendor']"})
        },
        'hwdoc.person': {
            'Meta': {'object_name': 'Person'},
            'emails': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['hwdoc.Email']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'phones': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['hwdoc.Phone']", 'symmetrical': 'False'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'hwdoc.phone': {
            'Meta': {'object_name': 'Phone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'hwdoc.project': {
            'Meta': {'object_name': 'Project'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['hwdoc.Person']", 'through': "orm['hwdoc.Role']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'hwdoc.rack': {
            'Meta': {'object_name': 'Rack'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hwdoc.RackModel']"}),
            'mounted_depth': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60', 'max_length': '10'})
        },
        'hwdoc.rackmodel': {
            'Meta': {'object_name': 'RackModel'},
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_mounting_depth': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '10'}),
            'min_mounting_depth': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hwdoc.Vendor']"}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '10'})
        },
        'hwdoc.rackposition': {
            'Meta': {'object_name': 'RackPosition'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '20'}),
            'rack': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['hwdoc.Rack']", 'unique': 'True'}),
            'rr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hwdoc.RackRow']"})
        },
        'hwdoc.rackrow': {
            'Meta': {'object_name': 'RackRow'},
            'dc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hwdoc.Datacenter']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'hwdoc.role': {
            'Meta': {'object_name': 'Role'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hwdoc.Person']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hwdoc.Project']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'hwdoc.servermanagement': {
            'Meta': {'object_name': 'ServerManagement'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'equipment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['hwdoc.Equipment']", 'unique': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '17', 'blank': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'raid_license': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        },
        'hwdoc.vendor': {
            'Meta': {'object_name': 'Vendor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['hwdoc']

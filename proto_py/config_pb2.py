# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import config_sensors_pb2 as config__sensors__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63onfig.proto\x12\x06\x63onfig\x1a\x14\x63onfig_sensors.proto\"V\n\nConfigUnit\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x04yaml\x18\x03 \x01(\tH\x00\x12\x1f\n\x05proto\x18\x04 \x01(\x0b\x32\x0e.config.ConfigH\x00\x42\t\n\x07\x63ontent\"\\\n\rConfigCommand\x12\'\n\x04type\x18\x01 \x01(\x0e\x32\x19.config.ConfigCommandType\x12\"\n\x06\x63onfig\x18\x02 \x03(\x0b\x32\x12.config.ConfigUnit\"G\n\x15\x43onfigCommandResponse\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\"\n\x06\x63onfig\x18\x02 \x03(\x0b\x32\x12.config.ConfigUnit\"y\n\x0e\x43onfigUnitInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12$\n\x04type\x18\x03 \x01(\x0e\x32\x16.config.ConfigUnitType\x12\x0c\n\x04\x64\x65sc\x18\x04 \x01(\t\x12\x14\n\x0c\x66ile_monitor\x18\x05 \x01(\x08\"j\n\x06\x43onfig\x12)\n\tunit_info\x18\x01 \x01(\x0b\x32\x16.config.ConfigUnitInfo\x12+\n\x07sensors\x18\n \x01(\x0b\x32\x18.config.CfgSensorsConfigH\x00\x42\x08\n\x06\x63onfig*\xa8\x01\n\x11\x43onfigCommandType\x12\x15\n\x11\x43onfigCommandNone\x10\x00\x12\x14\n\x10\x43onfigCommandGet\x10\x01\x12\x17\n\x13\x43onfigCommandUpdate\x10\x02\x12\x16\n\x12\x43onfigCommandMerge\x10\x03\x12\x18\n\x14\x43onfigCommandRestore\x10\x04\x12\x1b\n\x17\x43onfigCommandRestoreAll\x10\x05*^\n\x0e\x43onfigUnitType\x12\x19\n\x15\x43onfigUnitTypeRestore\x10\x01\x12\x16\n\x12\x43onfigUnitTypeKeep\x10\x02\x12\x19\n\x15\x43onfigUnitTypeFactory\x10\x03')

_CONFIGCOMMANDTYPE = DESCRIPTOR.enum_types_by_name['ConfigCommandType']
ConfigCommandType = enum_type_wrapper.EnumTypeWrapper(_CONFIGCOMMANDTYPE)
_CONFIGUNITTYPE = DESCRIPTOR.enum_types_by_name['ConfigUnitType']
ConfigUnitType = enum_type_wrapper.EnumTypeWrapper(_CONFIGUNITTYPE)
ConfigCommandNone = 0
ConfigCommandGet = 1
ConfigCommandUpdate = 2
ConfigCommandMerge = 3
ConfigCommandRestore = 4
ConfigCommandRestoreAll = 5
ConfigUnitTypeRestore = 1
ConfigUnitTypeKeep = 2
ConfigUnitTypeFactory = 3


_CONFIGUNIT = DESCRIPTOR.message_types_by_name['ConfigUnit']
_CONFIGCOMMAND = DESCRIPTOR.message_types_by_name['ConfigCommand']
_CONFIGCOMMANDRESPONSE = DESCRIPTOR.message_types_by_name['ConfigCommandResponse']
_CONFIGUNITINFO = DESCRIPTOR.message_types_by_name['ConfigUnitInfo']
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
ConfigUnit = _reflection.GeneratedProtocolMessageType('ConfigUnit', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGUNIT,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:config.ConfigUnit)
  })
_sym_db.RegisterMessage(ConfigUnit)

ConfigCommand = _reflection.GeneratedProtocolMessageType('ConfigCommand', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGCOMMAND,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:config.ConfigCommand)
  })
_sym_db.RegisterMessage(ConfigCommand)

ConfigCommandResponse = _reflection.GeneratedProtocolMessageType('ConfigCommandResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGCOMMANDRESPONSE,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:config.ConfigCommandResponse)
  })
_sym_db.RegisterMessage(ConfigCommandResponse)

ConfigUnitInfo = _reflection.GeneratedProtocolMessageType('ConfigUnitInfo', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGUNITINFO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:config.ConfigUnitInfo)
  })
_sym_db.RegisterMessage(ConfigUnitInfo)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:config.Config)
  })
_sym_db.RegisterMessage(Config)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIGCOMMANDTYPE._serialized_start=533
  _CONFIGCOMMANDTYPE._serialized_end=701
  _CONFIGUNITTYPE._serialized_start=703
  _CONFIGUNITTYPE._serialized_end=797
  _CONFIGUNIT._serialized_start=46
  _CONFIGUNIT._serialized_end=132
  _CONFIGCOMMAND._serialized_start=134
  _CONFIGCOMMAND._serialized_end=226
  _CONFIGCOMMANDRESPONSE._serialized_start=228
  _CONFIGCOMMANDRESPONSE._serialized_end=299
  _CONFIGUNITINFO._serialized_start=301
  _CONFIGUNITINFO._serialized_end=422
  _CONFIG._serialized_start=424
  _CONFIG._serialized_end=530
# @@protoc_insertion_point(module_scope)

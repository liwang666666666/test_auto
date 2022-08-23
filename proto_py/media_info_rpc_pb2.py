# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: media_info_rpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_types_pb2 as common__types__pb2
import media_pb2 as media__pb2
import media_file_metadata_types_pb2 as media__file__metadata__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14media_info_rpc.proto\x12\x04h130\x1a\x12\x63ommon_types.proto\x1a\x0bmedia.proto\x1a\x1fmedia_file_metadata_types.proto\"\x18\n\nCommandAck\x12\n\n\x02rc\x18\x01 \x02(\x05\"\xb6\x02\n\x0eInsertDataToDb\x12\x1d\n\x04type\x18\x02 \x01(\x0e\x32\x0f.h130.MediaType\x12\x17\n\x0fthumbnails_size\x18\x03 \x01(\x05\x12\x17\n\x0fthumbnails_path\x18\x04 \x01(\t\x12\x15\n\ranimated_size\x18\x05 \x01(\x05\x12\x15\n\ranimated_path\x18\x06 \x01(\t\x12\x19\n\x11\x61\x63tual_media_path\x18\x07 \x01(\t\x12#\n\nvideo_data\x18\x08 \x01(\x0b\x32\x0f.h130.VideoData\x12#\n\nphoto_data\x18\t \x01(\x0b\x32\x0f.h130.ImageData\x12+\n\x0bsensor_data\x18\n \x01(\x0b\x32\x16.h130.CameraSensorData\x12\x13\n\x0b\x63reate_time\x18\x0b \x01(\x04\x32\x85\x01\n\x08MediaRpc\x12=\n\x0fStartInfoNotify\x12\x18.h130.MediaCountsMessage\x1a\x10.h130.CommandAck\x12:\n\x10\x43\x61ptureMediaData\x12\x14.h130.InsertDataToDb\x1a\x10.h130.CommandAck')



_COMMANDACK = DESCRIPTOR.message_types_by_name['CommandAck']
_INSERTDATATODB = DESCRIPTOR.message_types_by_name['InsertDataToDb']
CommandAck = _reflection.GeneratedProtocolMessageType('CommandAck', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDACK,
  '__module__' : 'media_info_rpc_pb2'
  # @@protoc_insertion_point(class_scope:h130.CommandAck)
  })
_sym_db.RegisterMessage(CommandAck)

InsertDataToDb = _reflection.GeneratedProtocolMessageType('InsertDataToDb', (_message.Message,), {
  'DESCRIPTOR' : _INSERTDATATODB,
  '__module__' : 'media_info_rpc_pb2'
  # @@protoc_insertion_point(class_scope:h130.InsertDataToDb)
  })
_sym_db.RegisterMessage(InsertDataToDb)

_MEDIARPC = DESCRIPTOR.services_by_name['MediaRpc']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMMANDACK._serialized_start=96
  _COMMANDACK._serialized_end=120
  _INSERTDATATODB._serialized_start=123
  _INSERTDATATODB._serialized_end=433
  _MEDIARPC._serialized_start=436
  _MEDIARPC._serialized_end=569
# @@protoc_insertion_point(module_scope)

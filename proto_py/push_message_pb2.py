# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: push_message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import events_pb2 as events__pb2
import common_types_pb2 as common__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12push_message.proto\x12\x04h130\x1a\x0c\x65vents.proto\x1a\x12\x63ommon_types.proto\"\xf4\x03\n\x0bPushMessage\x12\x13\n\x0blog_message\x18\x01 \x01(\t\x12-\n\tlog_level\x18\x02 \x01(\x0e\x32\x1a.h130.PushMessage.LogLevel\x12\x15\n\rms_since_boot\x18\x03 \x01(\r\x12\x43\n\x13invalidated_request\x18\x04 \x01(\x0b\x32$.h130.PushMessage.InvalidatedRequestH\x00\x12\x30\n\x0cmedia_counts\x18\x05 \x01(\x0b\x32\x18.h130.MediaCountsMessageH\x00\x12)\n\x0c\x63rash_report\x18\x06 \x01(\x0b\x32\x11.h130.CrashReportH\x00\x12\x1e\n\x05\x65vent\x18\x07 \x01(\x0b\x32\r.h130.EventPbH\x00\x12\x32\n\x1brequest_location_for_camera\x18\x08 \x01(\x0b\x32\x0b.h130.EmptyH\x00\x1a=\n\x12InvalidatedRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\r\x12\x13\n\x0bmethod_uuid\x18\x02 \x01(\x04\"J\n\x08LogLevel\x12\x0f\n\x0b\x44\x45\x42UG_UNSET\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0b\n\x07VERBOSE\x10\x04\x42\t\n\x07payloadB#\n\x16\x63n.zerozero.proto.h130P\x01\xa2\x02\x06H130PB')



_PUSHMESSAGE = DESCRIPTOR.message_types_by_name['PushMessage']
_PUSHMESSAGE_INVALIDATEDREQUEST = _PUSHMESSAGE.nested_types_by_name['InvalidatedRequest']
_PUSHMESSAGE_LOGLEVEL = _PUSHMESSAGE.enum_types_by_name['LogLevel']
PushMessage = _reflection.GeneratedProtocolMessageType('PushMessage', (_message.Message,), {

  'InvalidatedRequest' : _reflection.GeneratedProtocolMessageType('InvalidatedRequest', (_message.Message,), {
    'DESCRIPTOR' : _PUSHMESSAGE_INVALIDATEDREQUEST,
    '__module__' : 'push_message_pb2'
    # @@protoc_insertion_point(class_scope:h130.PushMessage.InvalidatedRequest)
    })
  ,
  'DESCRIPTOR' : _PUSHMESSAGE,
  '__module__' : 'push_message_pb2'
  # @@protoc_insertion_point(class_scope:h130.PushMessage)
  })
_sym_db.RegisterMessage(PushMessage)
_sym_db.RegisterMessage(PushMessage.InvalidatedRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026cn.zerozero.proto.h130P\001\242\002\006H130PB'
  _PUSHMESSAGE._serialized_start=63
  _PUSHMESSAGE._serialized_end=563
  _PUSHMESSAGE_INVALIDATEDREQUEST._serialized_start=415
  _PUSHMESSAGE_INVALIDATEDREQUEST._serialized_end=476
  _PUSHMESSAGE_LOGLEVEL._serialized_start=478
  _PUSHMESSAGE_LOGLEVEL._serialized_end=552
# @@protoc_insertion_point(module_scope)

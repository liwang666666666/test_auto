# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exception_message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x65xception_message.proto\x12\x11\x65xception_message\"\x81\x01\n\x07Message\x12/\n\x05level\x18\x01 \x02(\x0e\x32 .exception_message.Message.Level\x12\x0f\n\x07message\x18\x02 \x02(\t\"4\n\x05Level\x12\x08\n\x04INFO\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\t\n\x05\x46\x41TAL\x10\x04\":\n\nMessageSet\x12,\n\x08messages\x18\x01 \x03(\x0b\x32\x1a.exception_message.Message')



_MESSAGE = DESCRIPTOR.message_types_by_name['Message']
_MESSAGESET = DESCRIPTOR.message_types_by_name['MessageSet']
_MESSAGE_LEVEL = _MESSAGE.enum_types_by_name['Level']
Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'exception_message_pb2'
  # @@protoc_insertion_point(class_scope:exception_message.Message)
  })
_sym_db.RegisterMessage(Message)

MessageSet = _reflection.GeneratedProtocolMessageType('MessageSet', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGESET,
  '__module__' : 'exception_message_pb2'
  # @@protoc_insertion_point(class_scope:exception_message.MessageSet)
  })
_sym_db.RegisterMessage(MessageSet)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGE._serialized_start=47
  _MESSAGE._serialized_end=176
  _MESSAGE_LEVEL._serialized_start=124
  _MESSAGE_LEVEL._serialized_end=176
  _MESSAGESET._serialized_start=178
  _MESSAGESET._serialized_end=236
# @@protoc_insertion_point(module_scope)

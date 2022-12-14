# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: events.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import rpc_message_types_pb2 as rpc__message__types__pb2
import camera_pb2 as camera__pb2
import common_types_pb2 as common__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x65vents.proto\x12\x04h130\x1a\x17rpc_message_types.proto\x1a\x0c\x63\x61mera.proto\x1a\x12\x63ommon_types.proto\"\xea\x05\n\x07\x45ventPb\x12\x33\n\rcharger_event\x18\x01 \x01(\x0b\x32\x1a.h130.ChargerStateResponseH\x00\x12\x34\n\x10ota_update_event\x18\x02 \x01(\x0b\x32\x18.h130.OTAUpdateEventDataH\x00\x12:\n\x18\x66light_mode_change_event\x18\x03 \x01(\x0b\x32\x16.h130.FlightModeConfigH\x00\x12\x37\n\x1a\x66light_status_change_event\x18\x04 \x01(\x0b\x32\x11.h130.CaptainInfoH\x00\x12<\n\x19\x66light_status_error_event\x18\x05 \x01(\x0b\x32\x17.h130.FlightStatusErrorH\x00\x12H\n#remaining_flight_info_changed_event\x18\x06 \x01(\x0b\x32\x19.h130.RemainingFlightInfoH\x00\x12\x39\n\x14usb_connection_event\x18\x07 \x01(\x0b\x32\x19.h130.USBConnectionStatusH\x00\x12;\n\x14\x62\x61ttery_status_event\x18\x08 \x01(\x0b\x32\x1b.h130.BatteryStatusResponseH\x00\x12;\n\x18\x63\x61libration_status_event\x18\t \x01(\x0b\x32\x17.h130.CalibrationStatusH\x00\x12.\n\x0flost_mode_event\x18\n \x01(\x0b\x32\x13.h130.LostModeEventH\x00\x12%\n\x0c\x63\x61mera_event\x18\x0b \x01(\x0b\x32\r.camera.EventH\x00\x12=\n\x17\x63\x61mera_count_down_event\x18\x0c \x01(\x0b\x32\x1a.h130.CameraCountDownEventH\x00\x12#\n\tsys_event\x18\r \x01(\x0b\x32\x0e.h130.SysEventH\x00\x42\x07\n\x05\x65ventB#\n\x16\x63n.zerozero.proto.h130P\x01\xa2\x02\x06H130PB')



_EVENTPB = DESCRIPTOR.message_types_by_name['EventPb']
EventPb = _reflection.GeneratedProtocolMessageType('EventPb', (_message.Message,), {
  'DESCRIPTOR' : _EVENTPB,
  '__module__' : 'events_pb2'
  # @@protoc_insertion_point(class_scope:h130.EventPb)
  })
_sym_db.RegisterMessage(EventPb)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026cn.zerozero.proto.h130P\001\242\002\006H130PB'
  _EVENTPB._serialized_start=82
  _EVENTPB._serialized_end=828
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: geofence/geofence.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='geofence/geofence.proto',
  package='mavsdk.rpc.geofence',
  syntax='proto3',
  serialized_options=b'\n\022io.mavsdk.geofenceB\rGeofenceProto',
  serialized_pb=b'\n\x17geofence/geofence.proto\x12\x13mavsdk.rpc.geofence\"4\n\x05Point\x12\x14\n\x0clatitude_deg\x18\x01 \x01(\x01\x12\x15\n\rlongitude_deg\x18\x02 \x01(\x01\"\x96\x01\n\x07Polygon\x12*\n\x06points\x18\x01 \x03(\x0b\x32\x1a.mavsdk.rpc.geofence.Point\x12/\n\x04type\x18\x02 \x01(\x0e\x32!.mavsdk.rpc.geofence.Polygon.Type\".\n\x04Type\x12\x12\n\x0eTYPE_INCLUSION\x10\x00\x12\x12\n\x0eTYPE_EXCLUSION\x10\x01\"G\n\x15UploadGeofenceRequest\x12.\n\x08polygons\x18\x01 \x03(\x0b\x32\x1c.mavsdk.rpc.geofence.Polygon\"V\n\x16UploadGeofenceResponse\x12<\n\x0fgeofence_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.geofence.GeofenceResult\"\x8b\x02\n\x0eGeofenceResult\x12:\n\x06result\x18\x01 \x01(\x0e\x32*.mavsdk.rpc.geofence.GeofenceResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xa8\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x10\n\x0cRESULT_ERROR\x10\x02\x12\"\n\x1eRESULT_TOO_MANY_GEOFENCE_ITEMS\x10\x03\x12\x0f\n\x0bRESULT_BUSY\x10\x04\x12\x12\n\x0eRESULT_TIMEOUT\x10\x05\x12\x1b\n\x17RESULT_INVALID_ARGUMENT\x10\x06\x32~\n\x0fGeofenceService\x12k\n\x0eUploadGeofence\x12*.mavsdk.rpc.geofence.UploadGeofenceRequest\x1a+.mavsdk.rpc.geofence.UploadGeofenceResponse\"\x00\x42#\n\x12io.mavsdk.geofenceB\rGeofenceProtob\x06proto3'
)



_POLYGON_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='mavsdk.rpc.geofence.Polygon.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_INCLUSION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_EXCLUSION', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=207,
  serialized_end=253,
)
_sym_db.RegisterEnumDescriptor(_POLYGON_TYPE)

_GEOFENCERESULT_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mavsdk.rpc.geofence.GeofenceResult.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_TOO_MANY_GEOFENCE_ITEMS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_BUSY', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_TIMEOUT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_INVALID_ARGUMENT', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=516,
  serialized_end=684,
)
_sym_db.RegisterEnumDescriptor(_GEOFENCERESULT_RESULT)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='mavsdk.rpc.geofence.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude_deg', full_name='mavsdk.rpc.geofence.Point.latitude_deg', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude_deg', full_name='mavsdk.rpc.geofence.Point.longitude_deg', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=100,
)


_POLYGON = _descriptor.Descriptor(
  name='Polygon',
  full_name='mavsdk.rpc.geofence.Polygon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='points', full_name='mavsdk.rpc.geofence.Polygon.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='mavsdk.rpc.geofence.Polygon.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _POLYGON_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=253,
)


_UPLOADGEOFENCEREQUEST = _descriptor.Descriptor(
  name='UploadGeofenceRequest',
  full_name='mavsdk.rpc.geofence.UploadGeofenceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='polygons', full_name='mavsdk.rpc.geofence.UploadGeofenceRequest.polygons', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=255,
  serialized_end=326,
)


_UPLOADGEOFENCERESPONSE = _descriptor.Descriptor(
  name='UploadGeofenceResponse',
  full_name='mavsdk.rpc.geofence.UploadGeofenceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='geofence_result', full_name='mavsdk.rpc.geofence.UploadGeofenceResponse.geofence_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=328,
  serialized_end=414,
)


_GEOFENCERESULT = _descriptor.Descriptor(
  name='GeofenceResult',
  full_name='mavsdk.rpc.geofence.GeofenceResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mavsdk.rpc.geofence.GeofenceResult.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result_str', full_name='mavsdk.rpc.geofence.GeofenceResult.result_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GEOFENCERESULT_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=417,
  serialized_end=684,
)

_POLYGON.fields_by_name['points'].message_type = _POINT
_POLYGON.fields_by_name['type'].enum_type = _POLYGON_TYPE
_POLYGON_TYPE.containing_type = _POLYGON
_UPLOADGEOFENCEREQUEST.fields_by_name['polygons'].message_type = _POLYGON
_UPLOADGEOFENCERESPONSE.fields_by_name['geofence_result'].message_type = _GEOFENCERESULT
_GEOFENCERESULT.fields_by_name['result'].enum_type = _GEOFENCERESULT_RESULT
_GEOFENCERESULT_RESULT.containing_type = _GEOFENCERESULT
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['Polygon'] = _POLYGON
DESCRIPTOR.message_types_by_name['UploadGeofenceRequest'] = _UPLOADGEOFENCEREQUEST
DESCRIPTOR.message_types_by_name['UploadGeofenceResponse'] = _UPLOADGEOFENCERESPONSE
DESCRIPTOR.message_types_by_name['GeofenceResult'] = _GEOFENCERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'geofence.geofence_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.geofence.Point)
  })
_sym_db.RegisterMessage(Point)

Polygon = _reflection.GeneratedProtocolMessageType('Polygon', (_message.Message,), {
  'DESCRIPTOR' : _POLYGON,
  '__module__' : 'geofence.geofence_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.geofence.Polygon)
  })
_sym_db.RegisterMessage(Polygon)

UploadGeofenceRequest = _reflection.GeneratedProtocolMessageType('UploadGeofenceRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADGEOFENCEREQUEST,
  '__module__' : 'geofence.geofence_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.geofence.UploadGeofenceRequest)
  })
_sym_db.RegisterMessage(UploadGeofenceRequest)

UploadGeofenceResponse = _reflection.GeneratedProtocolMessageType('UploadGeofenceResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADGEOFENCERESPONSE,
  '__module__' : 'geofence.geofence_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.geofence.UploadGeofenceResponse)
  })
_sym_db.RegisterMessage(UploadGeofenceResponse)

GeofenceResult = _reflection.GeneratedProtocolMessageType('GeofenceResult', (_message.Message,), {
  'DESCRIPTOR' : _GEOFENCERESULT,
  '__module__' : 'geofence.geofence_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.geofence.GeofenceResult)
  })
_sym_db.RegisterMessage(GeofenceResult)


DESCRIPTOR._options = None

_GEOFENCESERVICE = _descriptor.ServiceDescriptor(
  name='GeofenceService',
  full_name='mavsdk.rpc.geofence.GeofenceService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=686,
  serialized_end=812,
  methods=[
  _descriptor.MethodDescriptor(
    name='UploadGeofence',
    full_name='mavsdk.rpc.geofence.GeofenceService.UploadGeofence',
    index=0,
    containing_service=None,
    input_type=_UPLOADGEOFENCEREQUEST,
    output_type=_UPLOADGEOFENCERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GEOFENCESERVICE)

DESCRIPTOR.services_by_name['GeofenceService'] = _GEOFENCESERVICE

# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: primitive.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='primitive.proto',
  package='iroha.protocol',
  syntax='proto3',
  serialized_pb=_b('\n\x0fprimitive.proto\x12\x0eiroha.protocol\"\xfa\x01\n\x0bPermissions\x12\x14\n\x0cissue_assets\x18\x01 \x01(\x08\x12\x15\n\rcreate_assets\x18\x02 \x01(\x08\x12\x17\n\x0f\x63reate_accounts\x18\x03 \x01(\x08\x12\x16\n\x0e\x63reate_domains\x18\x04 \x01(\x08\x12\x19\n\x11read_all_accounts\x18\x05 \x01(\x08\x12\x15\n\radd_signatory\x18\x06 \x01(\x08\x12\x18\n\x10remove_signatory\x18\x07 \x01(\x08\x12\x17\n\x0fset_permissions\x18\x08 \x01(\x08\x12\x12\n\nset_quorum\x18\t \x01(\x08\x12\x14\n\x0c\x63\x61n_transfer\x18\n \x01(\x08\".\n\tSignature\x12\x0e\n\x06pubkey\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"G\n\x07uint256\x12\r\n\x05\x66irst\x18\x01 \x01(\x04\x12\x0e\n\x06second\x18\x02 \x01(\x04\x12\r\n\x05third\x18\x03 \x01(\x04\x12\x0e\n\x06\x66ourth\x18\x04 \x01(\x04\"C\n\x06\x41mount\x12&\n\x05value\x18\x01 \x01(\x0b\x32\x17.iroha.protocol.uint256\x12\x11\n\tprecision\x18\x02 \x01(\rb\x06proto3')
)




_PERMISSIONS = _descriptor.Descriptor(
  name='Permissions',
  full_name='iroha.protocol.Permissions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='issue_assets', full_name='iroha.protocol.Permissions.issue_assets', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_assets', full_name='iroha.protocol.Permissions.create_assets', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_accounts', full_name='iroha.protocol.Permissions.create_accounts', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_domains', full_name='iroha.protocol.Permissions.create_domains', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_all_accounts', full_name='iroha.protocol.Permissions.read_all_accounts', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_signatory', full_name='iroha.protocol.Permissions.add_signatory', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remove_signatory', full_name='iroha.protocol.Permissions.remove_signatory', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='set_permissions', full_name='iroha.protocol.Permissions.set_permissions', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='set_quorum', full_name='iroha.protocol.Permissions.set_quorum', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='can_transfer', full_name='iroha.protocol.Permissions.can_transfer', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=286,
)


_SIGNATURE = _descriptor.Descriptor(
  name='Signature',
  full_name='iroha.protocol.Signature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pubkey', full_name='iroha.protocol.Signature.pubkey', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='iroha.protocol.Signature.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=288,
  serialized_end=334,
)


_UINT256 = _descriptor.Descriptor(
  name='uint256',
  full_name='iroha.protocol.uint256',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='iroha.protocol.uint256.first', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='second', full_name='iroha.protocol.uint256.second', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='third', full_name='iroha.protocol.uint256.third', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fourth', full_name='iroha.protocol.uint256.fourth', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=336,
  serialized_end=407,
)


_AMOUNT = _descriptor.Descriptor(
  name='Amount',
  full_name='iroha.protocol.Amount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='iroha.protocol.Amount.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precision', full_name='iroha.protocol.Amount.precision', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=409,
  serialized_end=476,
)

_AMOUNT.fields_by_name['value'].message_type = _UINT256
DESCRIPTOR.message_types_by_name['Permissions'] = _PERMISSIONS
DESCRIPTOR.message_types_by_name['Signature'] = _SIGNATURE
DESCRIPTOR.message_types_by_name['uint256'] = _UINT256
DESCRIPTOR.message_types_by_name['Amount'] = _AMOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Permissions = _reflection.GeneratedProtocolMessageType('Permissions', (_message.Message,), dict(
  DESCRIPTOR = _PERMISSIONS,
  __module__ = 'primitive_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.Permissions)
  ))
_sym_db.RegisterMessage(Permissions)

Signature = _reflection.GeneratedProtocolMessageType('Signature', (_message.Message,), dict(
  DESCRIPTOR = _SIGNATURE,
  __module__ = 'primitive_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.Signature)
  ))
_sym_db.RegisterMessage(Signature)

uint256 = _reflection.GeneratedProtocolMessageType('uint256', (_message.Message,), dict(
  DESCRIPTOR = _UINT256,
  __module__ = 'primitive_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.uint256)
  ))
_sym_db.RegisterMessage(uint256)

Amount = _reflection.GeneratedProtocolMessageType('Amount', (_message.Message,), dict(
  DESCRIPTOR = _AMOUNT,
  __module__ = 'primitive_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.Amount)
  ))
_sym_db.RegisterMessage(Amount)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)

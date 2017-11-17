# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: endpoint.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import block_pb2 as block__pb2
import queries_pb2 as queries__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import responses_pb2 as responses__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='endpoint.proto',
  package='iroha.protocol',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x65ndpoint.proto\x12\x0eiroha.protocol\x1a\x0b\x62lock.proto\x1a\rqueries.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0fresponses.proto\"<\n\rToriiResponse\x12+\n\ttx_status\x18\x01 \x01(\x0e\x32\x18.iroha.protocol.TxStatus\"\"\n\x0fTxStatusRequest\x12\x0f\n\x07tx_hash\x18\x01 \x01(\x0c\"Q\n\x19\x41pplyGenesisBlockResponse\x12\x34\n\x07\x61pplied\x18\x01 \x01(\x0e\x32#.iroha.protocol.GenesisBlockApplied*\xbf\x01\n\x08TxStatus\x12\x1f\n\x1bSTATELESS_VALIDATION_FAILED\x10\x00\x12 \n\x1cSTATELESS_VALIDATION_SUCCESS\x10\x01\x12\x1e\n\x1aSTATEFUL_VALIDATION_FAILED\x10\x02\x12\x1f\n\x1bSTATEFUL_VALIDATION_SUCCESS\x10\x03\x12\r\n\tCOMMITTED\x10\x04\x12\x0e\n\nON_PROCESS\x10\x05\x12\x10\n\x0cNOT_RECEIVED\x10\x06*;\n\x13GenesisBlockApplied\x12\x11\n\rAPPLY_FAILURE\x10\x00\x12\x11\n\rAPPLY_SUCCESS\x10\x01\x32\x98\x01\n\x0e\x43ommandService\x12<\n\x05Torii\x12\x1b.iroha.protocol.Transaction\x1a\x16.google.protobuf.Empty\x12H\n\x06Status\x12\x1f.iroha.protocol.TxStatusRequest\x1a\x1d.iroha.protocol.ToriiResponse2L\n\x0cQueryService\x12<\n\x04\x46ind\x12\x15.iroha.protocol.Query\x1a\x1d.iroha.protocol.QueryResponse2\xb3\x01\n\x13GenesisBlockService\x12T\n\x10SendGenesisBlock\x12\x15.iroha.protocol.Block\x1a).iroha.protocol.ApplyGenesisBlockResponse\x12\x46\n\x15SendAbortGenesisBlock\x12\x15.iroha.protocol.Block\x1a\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[block__pb2.DESCRIPTOR,queries__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,responses__pb2.DESCRIPTOR,])

_TXSTATUS = _descriptor.EnumDescriptor(
  name='TxStatus',
  full_name='iroha.protocol.TxStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATELESS_VALIDATION_FAILED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATELESS_VALIDATION_SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATEFUL_VALIDATION_FAILED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATEFUL_VALIDATION_SUCCESS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMITTED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ON_PROCESS', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_RECEIVED', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=290,
  serialized_end=481,
)
_sym_db.RegisterEnumDescriptor(_TXSTATUS)

TxStatus = enum_type_wrapper.EnumTypeWrapper(_TXSTATUS)
_GENESISBLOCKAPPLIED = _descriptor.EnumDescriptor(
  name='GenesisBlockApplied',
  full_name='iroha.protocol.GenesisBlockApplied',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='APPLY_FAILURE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPLY_SUCCESS', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=483,
  serialized_end=542,
)
_sym_db.RegisterEnumDescriptor(_GENESISBLOCKAPPLIED)

GenesisBlockApplied = enum_type_wrapper.EnumTypeWrapper(_GENESISBLOCKAPPLIED)
STATELESS_VALIDATION_FAILED = 0
STATELESS_VALIDATION_SUCCESS = 1
STATEFUL_VALIDATION_FAILED = 2
STATEFUL_VALIDATION_SUCCESS = 3
COMMITTED = 4
ON_PROCESS = 5
NOT_RECEIVED = 6
APPLY_FAILURE = 0
APPLY_SUCCESS = 1



_TORIIRESPONSE = _descriptor.Descriptor(
  name='ToriiResponse',
  full_name='iroha.protocol.ToriiResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_status', full_name='iroha.protocol.ToriiResponse.tx_status', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=108,
  serialized_end=168,
)


_TXSTATUSREQUEST = _descriptor.Descriptor(
  name='TxStatusRequest',
  full_name='iroha.protocol.TxStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_hash', full_name='iroha.protocol.TxStatusRequest.tx_hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  serialized_start=170,
  serialized_end=204,
)


_APPLYGENESISBLOCKRESPONSE = _descriptor.Descriptor(
  name='ApplyGenesisBlockResponse',
  full_name='iroha.protocol.ApplyGenesisBlockResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='applied', full_name='iroha.protocol.ApplyGenesisBlockResponse.applied', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=206,
  serialized_end=287,
)

_TORIIRESPONSE.fields_by_name['tx_status'].enum_type = _TXSTATUS
_APPLYGENESISBLOCKRESPONSE.fields_by_name['applied'].enum_type = _GENESISBLOCKAPPLIED
DESCRIPTOR.message_types_by_name['ToriiResponse'] = _TORIIRESPONSE
DESCRIPTOR.message_types_by_name['TxStatusRequest'] = _TXSTATUSREQUEST
DESCRIPTOR.message_types_by_name['ApplyGenesisBlockResponse'] = _APPLYGENESISBLOCKRESPONSE
DESCRIPTOR.enum_types_by_name['TxStatus'] = _TXSTATUS
DESCRIPTOR.enum_types_by_name['GenesisBlockApplied'] = _GENESISBLOCKAPPLIED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ToriiResponse = _reflection.GeneratedProtocolMessageType('ToriiResponse', (_message.Message,), dict(
  DESCRIPTOR = _TORIIRESPONSE,
  __module__ = 'endpoint_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.ToriiResponse)
  ))
_sym_db.RegisterMessage(ToriiResponse)

TxStatusRequest = _reflection.GeneratedProtocolMessageType('TxStatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _TXSTATUSREQUEST,
  __module__ = 'endpoint_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.TxStatusRequest)
  ))
_sym_db.RegisterMessage(TxStatusRequest)

ApplyGenesisBlockResponse = _reflection.GeneratedProtocolMessageType('ApplyGenesisBlockResponse', (_message.Message,), dict(
  DESCRIPTOR = _APPLYGENESISBLOCKRESPONSE,
  __module__ = 'endpoint_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.ApplyGenesisBlockResponse)
  ))
_sym_db.RegisterMessage(ApplyGenesisBlockResponse)



_COMMANDSERVICE = _descriptor.ServiceDescriptor(
  name='CommandService',
  full_name='iroha.protocol.CommandService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=545,
  serialized_end=697,
  methods=[
  _descriptor.MethodDescriptor(
    name='Torii',
    full_name='iroha.protocol.CommandService.Torii',
    index=0,
    containing_service=None,
    input_type=block__pb2._TRANSACTION,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Status',
    full_name='iroha.protocol.CommandService.Status',
    index=1,
    containing_service=None,
    input_type=_TXSTATUSREQUEST,
    output_type=_TORIIRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMANDSERVICE)

DESCRIPTOR.services_by_name['CommandService'] = _COMMANDSERVICE


_QUERYSERVICE = _descriptor.ServiceDescriptor(
  name='QueryService',
  full_name='iroha.protocol.QueryService',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=699,
  serialized_end=775,
  methods=[
  _descriptor.MethodDescriptor(
    name='Find',
    full_name='iroha.protocol.QueryService.Find',
    index=0,
    containing_service=None,
    input_type=queries__pb2._QUERY,
    output_type=responses__pb2._QUERYRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERYSERVICE)

DESCRIPTOR.services_by_name['QueryService'] = _QUERYSERVICE


_GENESISBLOCKSERVICE = _descriptor.ServiceDescriptor(
  name='GenesisBlockService',
  full_name='iroha.protocol.GenesisBlockService',
  file=DESCRIPTOR,
  index=2,
  options=None,
  serialized_start=778,
  serialized_end=957,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendGenesisBlock',
    full_name='iroha.protocol.GenesisBlockService.SendGenesisBlock',
    index=0,
    containing_service=None,
    input_type=block__pb2._BLOCK,
    output_type=_APPLYGENESISBLOCKRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendAbortGenesisBlock',
    full_name='iroha.protocol.GenesisBlockService.SendAbortGenesisBlock',
    index=1,
    containing_service=None,
    input_type=block__pb2._BLOCK,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GENESISBLOCKSERVICE)

DESCRIPTOR.services_by_name['GenesisBlockService'] = _GENESISBLOCKSERVICE

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class CommandServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Torii = channel.unary_unary(
          '/iroha.protocol.CommandService/Torii',
          request_serializer=block__pb2.Transaction.SerializeToString,
          response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          )
      self.Status = channel.unary_unary(
          '/iroha.protocol.CommandService/Status',
          request_serializer=TxStatusRequest.SerializeToString,
          response_deserializer=ToriiResponse.FromString,
          )


  class CommandServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def Torii(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def Status(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_CommandServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Torii': grpc.unary_unary_rpc_method_handler(
            servicer.Torii,
            request_deserializer=block__pb2.Transaction.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        'Status': grpc.unary_unary_rpc_method_handler(
            servicer.Status,
            request_deserializer=TxStatusRequest.FromString,
            response_serializer=ToriiResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'iroha.protocol.CommandService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class QueryServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Find = channel.unary_unary(
          '/iroha.protocol.QueryService/Find',
          request_serializer=queries__pb2.Query.SerializeToString,
          response_deserializer=responses__pb2.QueryResponse.FromString,
          )


  class QueryServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def Find(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_QueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Find': grpc.unary_unary_rpc_method_handler(
            servicer.Find,
            request_deserializer=queries__pb2.Query.FromString,
            response_serializer=responses__pb2.QueryResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'iroha.protocol.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class GenesisBlockServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.SendGenesisBlock = channel.unary_unary(
          '/iroha.protocol.GenesisBlockService/SendGenesisBlock',
          request_serializer=block__pb2.Block.SerializeToString,
          response_deserializer=ApplyGenesisBlockResponse.FromString,
          )
      self.SendAbortGenesisBlock = channel.unary_unary(
          '/iroha.protocol.GenesisBlockService/SendAbortGenesisBlock',
          request_serializer=block__pb2.Block.SerializeToString,
          response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          )


  class GenesisBlockServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def SendGenesisBlock(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def SendAbortGenesisBlock(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_GenesisBlockServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SendGenesisBlock': grpc.unary_unary_rpc_method_handler(
            servicer.SendGenesisBlock,
            request_deserializer=block__pb2.Block.FromString,
            response_serializer=ApplyGenesisBlockResponse.SerializeToString,
        ),
        'SendAbortGenesisBlock': grpc.unary_unary_rpc_method_handler(
            servicer.SendAbortGenesisBlock,
            request_deserializer=block__pb2.Block.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'iroha.protocol.GenesisBlockService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaCommandServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def Torii(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Status(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaCommandServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def Torii(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    Torii.future = None
    def Status(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    Status.future = None


  def beta_create_CommandService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('iroha.protocol.CommandService', 'Status'): TxStatusRequest.FromString,
      ('iroha.protocol.CommandService', 'Torii'): block__pb2.Transaction.FromString,
    }
    response_serializers = {
      ('iroha.protocol.CommandService', 'Status'): ToriiResponse.SerializeToString,
      ('iroha.protocol.CommandService', 'Torii'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
    }
    method_implementations = {
      ('iroha.protocol.CommandService', 'Status'): face_utilities.unary_unary_inline(servicer.Status),
      ('iroha.protocol.CommandService', 'Torii'): face_utilities.unary_unary_inline(servicer.Torii),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_CommandService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('iroha.protocol.CommandService', 'Status'): TxStatusRequest.SerializeToString,
      ('iroha.protocol.CommandService', 'Torii'): block__pb2.Transaction.SerializeToString,
    }
    response_deserializers = {
      ('iroha.protocol.CommandService', 'Status'): ToriiResponse.FromString,
      ('iroha.protocol.CommandService', 'Torii'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
    }
    cardinalities = {
      'Status': cardinality.Cardinality.UNARY_UNARY,
      'Torii': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'iroha.protocol.CommandService', cardinalities, options=stub_options)


  class BetaQueryServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def Find(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaQueryServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def Find(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    Find.future = None


  def beta_create_QueryService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('iroha.protocol.QueryService', 'Find'): queries__pb2.Query.FromString,
    }
    response_serializers = {
      ('iroha.protocol.QueryService', 'Find'): responses__pb2.QueryResponse.SerializeToString,
    }
    method_implementations = {
      ('iroha.protocol.QueryService', 'Find'): face_utilities.unary_unary_inline(servicer.Find),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_QueryService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('iroha.protocol.QueryService', 'Find'): queries__pb2.Query.SerializeToString,
    }
    response_deserializers = {
      ('iroha.protocol.QueryService', 'Find'): responses__pb2.QueryResponse.FromString,
    }
    cardinalities = {
      'Find': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'iroha.protocol.QueryService', cardinalities, options=stub_options)


  class BetaGenesisBlockServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def SendGenesisBlock(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def SendAbortGenesisBlock(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaGenesisBlockServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def SendGenesisBlock(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    SendGenesisBlock.future = None
    def SendAbortGenesisBlock(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    SendAbortGenesisBlock.future = None


  def beta_create_GenesisBlockService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('iroha.protocol.GenesisBlockService', 'SendAbortGenesisBlock'): block__pb2.Block.FromString,
      ('iroha.protocol.GenesisBlockService', 'SendGenesisBlock'): block__pb2.Block.FromString,
    }
    response_serializers = {
      ('iroha.protocol.GenesisBlockService', 'SendAbortGenesisBlock'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ('iroha.protocol.GenesisBlockService', 'SendGenesisBlock'): ApplyGenesisBlockResponse.SerializeToString,
    }
    method_implementations = {
      ('iroha.protocol.GenesisBlockService', 'SendAbortGenesisBlock'): face_utilities.unary_unary_inline(servicer.SendAbortGenesisBlock),
      ('iroha.protocol.GenesisBlockService', 'SendGenesisBlock'): face_utilities.unary_unary_inline(servicer.SendGenesisBlock),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_GenesisBlockService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('iroha.protocol.GenesisBlockService', 'SendAbortGenesisBlock'): block__pb2.Block.SerializeToString,
      ('iroha.protocol.GenesisBlockService', 'SendGenesisBlock'): block__pb2.Block.SerializeToString,
    }
    response_deserializers = {
      ('iroha.protocol.GenesisBlockService', 'SendAbortGenesisBlock'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
      ('iroha.protocol.GenesisBlockService', 'SendGenesisBlock'): ApplyGenesisBlockResponse.FromString,
    }
    cardinalities = {
      'SendAbortGenesisBlock': cardinality.Cardinality.UNARY_UNARY,
      'SendGenesisBlock': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'iroha.protocol.GenesisBlockService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/tensor/fixed_precision_tensor.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# relative
from . import share_tensor_pb2 as proto_dot_core_dot_tensor_dot_share__tensor__pb2
from . import tensor_pb2 as proto_dot_core_dot_tensor_dot_tensor__pb2
from ...lib.numpy import array_pb2 as proto_dot_lib_dot_numpy_dot_array__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/tensor/fixed_precision_tensor.proto",
    package="syft.core.tensor",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n.proto/core/tensor/fixed_precision_tensor.proto\x12\x10syft.core.tensor\x1a\x1eproto/core/tensor/tensor.proto\x1a$proto/core/tensor/share_tensor.proto\x1a\x1bproto/lib/numpy/array.proto"\xc8\x01\n\x14\x46ixedPrecisionTensor\x12*\n\x06tensor\x18\x01 \x01(\x0b\x32\x18.syft.core.tensor.TensorH\x00\x12.\n\x05share\x18\x02 \x01(\x0b\x32\x1d.syft.core.tensor.ShareTensorH\x00\x12+\n\x05\x61rray\x18\x03 \x01(\x0b\x32\x1a.syft.lib.numpy.NumpyProtoH\x00\x12\x0c\n\x04\x62\x61se\x18\x04 \x01(\r\x12\x11\n\tprecision\x18\x05 \x01(\rB\x06\n\x04\x64\x61tab\x06proto3',
    dependencies=[
        proto_dot_core_dot_tensor_dot_tensor__pb2.DESCRIPTOR,
        proto_dot_core_dot_tensor_dot_share__tensor__pb2.DESCRIPTOR,
        proto_dot_lib_dot_numpy_dot_array__pb2.DESCRIPTOR,
    ],
)


_FIXEDPRECISIONTENSOR = _descriptor.Descriptor(
    name="FixedPrecisionTensor",
    full_name="syft.core.tensor.FixedPrecisionTensor",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="tensor",
            full_name="syft.core.tensor.FixedPrecisionTensor.tensor",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="share",
            full_name="syft.core.tensor.FixedPrecisionTensor.share",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="array",
            full_name="syft.core.tensor.FixedPrecisionTensor.array",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="base",
            full_name="syft.core.tensor.FixedPrecisionTensor.base",
            index=3,
            number=4,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="precision",
            full_name="syft.core.tensor.FixedPrecisionTensor.precision",
            index=4,
            number=5,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="data",
            full_name="syft.core.tensor.FixedPrecisionTensor.data",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=168,
    serialized_end=368,
)

_FIXEDPRECISIONTENSOR.fields_by_name[
    "tensor"
].message_type = proto_dot_core_dot_tensor_dot_tensor__pb2._TENSOR
_FIXEDPRECISIONTENSOR.fields_by_name[
    "share"
].message_type = proto_dot_core_dot_tensor_dot_share__tensor__pb2._SHARETENSOR
_FIXEDPRECISIONTENSOR.fields_by_name[
    "array"
].message_type = proto_dot_lib_dot_numpy_dot_array__pb2._NUMPYPROTO
_FIXEDPRECISIONTENSOR.oneofs_by_name["data"].fields.append(
    _FIXEDPRECISIONTENSOR.fields_by_name["tensor"]
)
_FIXEDPRECISIONTENSOR.fields_by_name[
    "tensor"
].containing_oneof = _FIXEDPRECISIONTENSOR.oneofs_by_name["data"]
_FIXEDPRECISIONTENSOR.oneofs_by_name["data"].fields.append(
    _FIXEDPRECISIONTENSOR.fields_by_name["share"]
)
_FIXEDPRECISIONTENSOR.fields_by_name[
    "share"
].containing_oneof = _FIXEDPRECISIONTENSOR.oneofs_by_name["data"]
_FIXEDPRECISIONTENSOR.oneofs_by_name["data"].fields.append(
    _FIXEDPRECISIONTENSOR.fields_by_name["array"]
)
_FIXEDPRECISIONTENSOR.fields_by_name[
    "array"
].containing_oneof = _FIXEDPRECISIONTENSOR.oneofs_by_name["data"]
DESCRIPTOR.message_types_by_name["FixedPrecisionTensor"] = _FIXEDPRECISIONTENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FixedPrecisionTensor = _reflection.GeneratedProtocolMessageType(
    "FixedPrecisionTensor",
    (_message.Message,),
    {
        "DESCRIPTOR": _FIXEDPRECISIONTENSOR,
        "__module__": "proto.core.tensor.fixed_precision_tensor_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.tensor.FixedPrecisionTensor)
    },
)
_sym_db.RegisterMessage(FixedPrecisionTensor)


# @@protoc_insertion_point(module_scope)

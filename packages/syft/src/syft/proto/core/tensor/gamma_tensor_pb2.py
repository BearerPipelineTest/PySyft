# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/tensor/gamma_tensor.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/tensor/gamma_tensor.proto",
    package="syft.core.tensor",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n$proto/core/tensor/gamma_tensor.proto\x12\x10syft.core.tensor"w\n\x0bGammaTensor\x12\r\n\x05value\x18\x01 \x01(\x0c\x12\x0f\n\x07min_val\x18\x02 \x01(\x02\x12\x0f\n\x07max_val\x18\x03 \x01(\x02\x12\x11\n\tis_linear\x18\x04 \x01(\x08\x12\x15\n\rdata_subjects\x18\x05 \x01(\x0c\x12\r\n\x05state\x18\x06 \x01(\x0c\x62\x06proto3',
)


_GAMMATENSOR = _descriptor.Descriptor(
    name="GammaTensor",
    full_name="syft.core.tensor.GammaTensor",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="value",
            full_name="syft.core.tensor.GammaTensor.value",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
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
            name="min_val",
            full_name="syft.core.tensor.GammaTensor.min_val",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
            name="max_val",
            full_name="syft.core.tensor.GammaTensor.max_val",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
            name="is_linear",
            full_name="syft.core.tensor.GammaTensor.is_linear",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
            name="data_subjects",
            full_name="syft.core.tensor.GammaTensor.data_subjects",
            index=4,
            number=5,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
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
            name="state",
            full_name="syft.core.tensor.GammaTensor.state",
            index=5,
            number=6,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
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
    oneofs=[],
    serialized_start=58,
    serialized_end=177,
)

DESCRIPTOR.message_types_by_name["GammaTensor"] = _GAMMATENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GammaTensor = _reflection.GeneratedProtocolMessageType(
    "GammaTensor",
    (_message.Message,),
    {
        "DESCRIPTOR": _GAMMATENSOR,
        "__module__": "proto.core.tensor.gamma_tensor_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.tensor.GammaTensor)
    },
)
_sym_db.RegisterMessage(GammaTensor)


# @@protoc_insertion_point(module_scope)

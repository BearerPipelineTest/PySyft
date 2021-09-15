# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/PIL/image.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# relative
from ..torch import tensor_pb2 as proto_dot_lib_dot_torch_dot_tensor__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/PIL/image.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x19proto/lib/PIL/image.proto\x1a\x1cproto/lib/torch/tensor.proto"2\n\x05Image\x12)\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1b.syft.lib.torch.TensorProtob\x06proto3',
    dependencies=[
        proto_dot_lib_dot_torch_dot_tensor__pb2.DESCRIPTOR,
    ],
)


_IMAGE = _descriptor.Descriptor(
    name="Image",
    full_name="Image",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="data",
            full_name="Image.data",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=59,
    serialized_end=109,
)

_IMAGE.fields_by_name[
    "data"
].message_type = proto_dot_lib_dot_torch_dot_tensor__pb2._TENSORPROTO
DESCRIPTOR.message_types_by_name["Image"] = _IMAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Image = _reflection.GeneratedProtocolMessageType(
    "Image",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMAGE,
        "__module__": "proto.lib.PIL.image_pb2"
        # @@protoc_insertion_point(class_scope:Image)
    },
)
_sym_db.RegisterMessage(Image)


# @@protoc_insertion_point(module_scope)

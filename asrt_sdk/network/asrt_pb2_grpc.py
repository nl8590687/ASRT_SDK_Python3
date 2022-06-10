# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import asrt_sdk.network.asrt_pb2 as asrt__pb2


class AsrtGrpcServiceStub(object):
    """定义服务接口
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Speech = channel.unary_unary(
                '/asrt.AsrtGrpcService/Speech',
                request_serializer=asrt__pb2.SpeechRequest.SerializeToString,
                response_deserializer=asrt__pb2.SpeechResponse.FromString,
                )
        self.Language = channel.unary_unary(
                '/asrt.AsrtGrpcService/Language',
                request_serializer=asrt__pb2.LanguageRequest.SerializeToString,
                response_deserializer=asrt__pb2.TextResponse.FromString,
                )
        self.All = channel.unary_unary(
                '/asrt.AsrtGrpcService/All',
                request_serializer=asrt__pb2.SpeechRequest.SerializeToString,
                response_deserializer=asrt__pb2.TextResponse.FromString,
                )
        self.Stream = channel.stream_stream(
                '/asrt.AsrtGrpcService/Stream',
                request_serializer=asrt__pb2.SpeechRequest.SerializeToString,
                response_deserializer=asrt__pb2.TextResponse.FromString,
                )


class AsrtGrpcServiceServicer(object):
    """定义服务接口
    """

    def Speech(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Language(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def All(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AsrtGrpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Speech': grpc.unary_unary_rpc_method_handler(
                    servicer.Speech,
                    request_deserializer=asrt__pb2.SpeechRequest.FromString,
                    response_serializer=asrt__pb2.SpeechResponse.SerializeToString,
            ),
            'Language': grpc.unary_unary_rpc_method_handler(
                    servicer.Language,
                    request_deserializer=asrt__pb2.LanguageRequest.FromString,
                    response_serializer=asrt__pb2.TextResponse.SerializeToString,
            ),
            'All': grpc.unary_unary_rpc_method_handler(
                    servicer.All,
                    request_deserializer=asrt__pb2.SpeechRequest.FromString,
                    response_serializer=asrt__pb2.TextResponse.SerializeToString,
            ),
            'Stream': grpc.stream_stream_rpc_method_handler(
                    servicer.Stream,
                    request_deserializer=asrt__pb2.SpeechRequest.FromString,
                    response_serializer=asrt__pb2.TextResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'asrt.AsrtGrpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AsrtGrpcService(object):
    """定义服务接口
    """

    @staticmethod
    def Speech(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/asrt.AsrtGrpcService/Speech',
            asrt__pb2.SpeechRequest.SerializeToString,
            asrt__pb2.SpeechResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Language(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/asrt.AsrtGrpcService/Language',
            asrt__pb2.LanguageRequest.SerializeToString,
            asrt__pb2.TextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def All(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/asrt.AsrtGrpcService/All',
            asrt__pb2.SpeechRequest.SerializeToString,
            asrt__pb2.TextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/asrt.AsrtGrpcService/Stream',
            asrt__pb2.SpeechRequest.SerializeToString,
            asrt__pb2.TextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
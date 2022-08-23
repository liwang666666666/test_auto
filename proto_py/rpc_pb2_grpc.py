# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import camera_pb2 as camera__pb2
import common_types_pb2 as common__types__pb2
import rpc_pb2 as rpc__pb2


class HoverStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartSession = channel.unary_unary(
                '/pb.Hover/StartSession',
                request_serializer=camera__pb2.SessionId.SerializeToString,
                response_deserializer=camera__pb2.SessionId.FromString,
                )
        self.StopSession = channel.unary_unary(
                '/pb.Hover/StopSession',
                request_serializer=rpc__pb2.ParamNone.SerializeToString,
                response_deserializer=rpc__pb2.CommandAck.FromString,
                )
        self.SetCameraParam = channel.unary_unary(
                '/pb.Hover/SetCameraParam',
                request_serializer=camera__pb2.SetMetadata.SerializeToString,
                response_deserializer=rpc__pb2.CommandAck.FromString,
                )
        self.GetCameraParam = channel.unary_unary(
                '/pb.Hover/GetCameraParam',
                request_serializer=rpc__pb2.ParamNone.SerializeToString,
                response_deserializer=camera__pb2.Metadata.FromString,
                )
        self.RegisterCameraEvent = channel.unary_stream(
                '/pb.Hover/RegisterCameraEvent',
                request_serializer=rpc__pb2.ParamNone.SerializeToString,
                response_deserializer=camera__pb2.Event.FromString,
                )
        self.ReadCameraEvent = channel.unary_unary(
                '/pb.Hover/ReadCameraEvent',
                request_serializer=rpc__pb2.ParamNone.SerializeToString,
                response_deserializer=camera__pb2.Event.FromString,
                )
        self.StartPreview = channel.unary_unary(
                '/pb.Hover/StartPreview',
                request_serializer=rpc__pb2.ParamNone.SerializeToString,
                response_deserializer=rpc__pb2.CommandAck.FromString,
                )
        self.StopPreview = channel.unary_unary(
                '/pb.Hover/StopPreview',
                request_serializer=rpc__pb2.ParamNone.SerializeToString,
                response_deserializer=rpc__pb2.CommandAck.FromString,
                )
        self.StartVideo = channel.unary_unary(
                '/pb.Hover/StartVideo',
                request_serializer=rpc__pb2.ParamNone.SerializeToString,
                response_deserializer=rpc__pb2.CommandAck.FromString,
                )
        self.StopVideo = channel.unary_unary(
                '/pb.Hover/StopVideo',
                request_serializer=rpc__pb2.ParamNone.SerializeToString,
                response_deserializer=rpc__pb2.CommandAck.FromString,
                )
        self.TakeSnapshot = channel.unary_unary(
                '/pb.Hover/TakeSnapshot',
                request_serializer=rpc__pb2.ParamNone.SerializeToString,
                response_deserializer=rpc__pb2.CommandAck.FromString,
                )
        self.StopSnapshot = channel.unary_unary(
                '/pb.Hover/StopSnapshot',
                request_serializer=rpc__pb2.ParamNone.SerializeToString,
                response_deserializer=rpc__pb2.CommandAck.FromString,
                )
        self.RockerControl = channel.unary_unary(
                '/pb.Hover/RockerControl',
                request_serializer=common__types__pb2.RockerControlCommand.SerializeToString,
                response_deserializer=rpc__pb2.ParamNone.FromString,
                )


class HoverServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartSession(self, request, context):
        """StartSession:(should be called before other camera cmds)
        1. fist time must set input sessionid = 0 to get an output sessionid from mediadb
        2. In one session, if app/sRC/bRC reconnect, you should set input sessionid got from 1st step  
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCameraParam(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCameraParam(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterCameraEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadCameraEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartPreview(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopPreview(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartVideo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopVideo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TakeSnapshot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopSnapshot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RockerControl(self, request, context):
        """ManualControl
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HoverServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartSession': grpc.unary_unary_rpc_method_handler(
                    servicer.StartSession,
                    request_deserializer=camera__pb2.SessionId.FromString,
                    response_serializer=camera__pb2.SessionId.SerializeToString,
            ),
            'StopSession': grpc.unary_unary_rpc_method_handler(
                    servicer.StopSession,
                    request_deserializer=rpc__pb2.ParamNone.FromString,
                    response_serializer=rpc__pb2.CommandAck.SerializeToString,
            ),
            'SetCameraParam': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCameraParam,
                    request_deserializer=camera__pb2.SetMetadata.FromString,
                    response_serializer=rpc__pb2.CommandAck.SerializeToString,
            ),
            'GetCameraParam': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCameraParam,
                    request_deserializer=rpc__pb2.ParamNone.FromString,
                    response_serializer=camera__pb2.Metadata.SerializeToString,
            ),
            'RegisterCameraEvent': grpc.unary_stream_rpc_method_handler(
                    servicer.RegisterCameraEvent,
                    request_deserializer=rpc__pb2.ParamNone.FromString,
                    response_serializer=camera__pb2.Event.SerializeToString,
            ),
            'ReadCameraEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadCameraEvent,
                    request_deserializer=rpc__pb2.ParamNone.FromString,
                    response_serializer=camera__pb2.Event.SerializeToString,
            ),
            'StartPreview': grpc.unary_unary_rpc_method_handler(
                    servicer.StartPreview,
                    request_deserializer=rpc__pb2.ParamNone.FromString,
                    response_serializer=rpc__pb2.CommandAck.SerializeToString,
            ),
            'StopPreview': grpc.unary_unary_rpc_method_handler(
                    servicer.StopPreview,
                    request_deserializer=rpc__pb2.ParamNone.FromString,
                    response_serializer=rpc__pb2.CommandAck.SerializeToString,
            ),
            'StartVideo': grpc.unary_unary_rpc_method_handler(
                    servicer.StartVideo,
                    request_deserializer=rpc__pb2.ParamNone.FromString,
                    response_serializer=rpc__pb2.CommandAck.SerializeToString,
            ),
            'StopVideo': grpc.unary_unary_rpc_method_handler(
                    servicer.StopVideo,
                    request_deserializer=rpc__pb2.ParamNone.FromString,
                    response_serializer=rpc__pb2.CommandAck.SerializeToString,
            ),
            'TakeSnapshot': grpc.unary_unary_rpc_method_handler(
                    servicer.TakeSnapshot,
                    request_deserializer=rpc__pb2.ParamNone.FromString,
                    response_serializer=rpc__pb2.CommandAck.SerializeToString,
            ),
            'StopSnapshot': grpc.unary_unary_rpc_method_handler(
                    servicer.StopSnapshot,
                    request_deserializer=rpc__pb2.ParamNone.FromString,
                    response_serializer=rpc__pb2.CommandAck.SerializeToString,
            ),
            'RockerControl': grpc.unary_unary_rpc_method_handler(
                    servicer.RockerControl,
                    request_deserializer=common__types__pb2.RockerControlCommand.FromString,
                    response_serializer=rpc__pb2.ParamNone.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.Hover', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Hover(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Hover/StartSession',
            camera__pb2.SessionId.SerializeToString,
            camera__pb2.SessionId.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Hover/StopSession',
            rpc__pb2.ParamNone.SerializeToString,
            rpc__pb2.CommandAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetCameraParam(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Hover/SetCameraParam',
            camera__pb2.SetMetadata.SerializeToString,
            rpc__pb2.CommandAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCameraParam(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Hover/GetCameraParam',
            rpc__pb2.ParamNone.SerializeToString,
            camera__pb2.Metadata.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterCameraEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pb.Hover/RegisterCameraEvent',
            rpc__pb2.ParamNone.SerializeToString,
            camera__pb2.Event.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadCameraEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Hover/ReadCameraEvent',
            rpc__pb2.ParamNone.SerializeToString,
            camera__pb2.Event.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartPreview(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Hover/StartPreview',
            rpc__pb2.ParamNone.SerializeToString,
            rpc__pb2.CommandAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopPreview(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Hover/StopPreview',
            rpc__pb2.ParamNone.SerializeToString,
            rpc__pb2.CommandAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartVideo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Hover/StartVideo',
            rpc__pb2.ParamNone.SerializeToString,
            rpc__pb2.CommandAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopVideo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Hover/StopVideo',
            rpc__pb2.ParamNone.SerializeToString,
            rpc__pb2.CommandAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TakeSnapshot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Hover/TakeSnapshot',
            rpc__pb2.ParamNone.SerializeToString,
            rpc__pb2.CommandAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopSnapshot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Hover/StopSnapshot',
            rpc__pb2.ParamNone.SerializeToString,
            rpc__pb2.CommandAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RockerControl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Hover/RockerControl',
            common__types__pb2.RockerControlCommand.SerializeToString,
            rpc__pb2.ParamNone.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import booking_pb2 as booking__pb2


class BookingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBooking = channel.unary_stream(
                '/Booking/GetBooking',
                request_serializer=booking__pb2.EmptyTwo.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )
        self.GetBookingByUserId = channel.unary_unary(
                '/Booking/GetBookingByUserId',
                request_serializer=booking__pb2.UserID.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )
        self.AddBooking = channel.unary_unary(
                '/Booking/AddBooking',
                request_serializer=booking__pb2.BookingData.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )
        self.DeleteBooking = channel.unary_unary(
                '/Booking/DeleteBooking',
                request_serializer=booking__pb2.BookingData.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )
        self.UpdateBooking = channel.unary_unary(
                '/Booking/UpdateBooking',
                request_serializer=booking__pb2.BookingData.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )
        self.GetShowtimeTwo = channel.unary_stream(
                '/Booking/GetShowtimeTwo',
                request_serializer=booking__pb2.EmptyTwo.SerializeToString,
                response_deserializer=booking__pb2.ShowtimeDataTwo.FromString,
                )
        self.GetShowtimeByDateTwo = channel.unary_unary(
                '/Booking/GetShowtimeByDateTwo',
                request_serializer=booking__pb2.ShowtimeIDTwo.SerializeToString,
                response_deserializer=booking__pb2.ShowtimeDataTwo.FromString,
                )
        self.GetShowtimeByMovieTwo = channel.unary_unary(
                '/Booking/GetShowtimeByMovieTwo',
                request_serializer=booking__pb2.ShowtimeDateTwo.SerializeToString,
                response_deserializer=booking__pb2.ShowtimeDataTwo.FromString,
                )


class BookingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetBooking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBookingByUserId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddBooking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBooking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBooking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetShowtimeTwo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetShowtimeByDateTwo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetShowtimeByMovieTwo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBooking': grpc.unary_stream_rpc_method_handler(
                    servicer.GetBooking,
                    request_deserializer=booking__pb2.EmptyTwo.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
            'GetBookingByUserId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBookingByUserId,
                    request_deserializer=booking__pb2.UserID.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
            'AddBooking': grpc.unary_unary_rpc_method_handler(
                    servicer.AddBooking,
                    request_deserializer=booking__pb2.BookingData.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
            'DeleteBooking': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteBooking,
                    request_deserializer=booking__pb2.BookingData.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
            'UpdateBooking': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBooking,
                    request_deserializer=booking__pb2.BookingData.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
            'GetShowtimeTwo': grpc.unary_stream_rpc_method_handler(
                    servicer.GetShowtimeTwo,
                    request_deserializer=booking__pb2.EmptyTwo.FromString,
                    response_serializer=booking__pb2.ShowtimeDataTwo.SerializeToString,
            ),
            'GetShowtimeByDateTwo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetShowtimeByDateTwo,
                    request_deserializer=booking__pb2.ShowtimeIDTwo.FromString,
                    response_serializer=booking__pb2.ShowtimeDataTwo.SerializeToString,
            ),
            'GetShowtimeByMovieTwo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetShowtimeByMovieTwo,
                    request_deserializer=booking__pb2.ShowtimeDateTwo.FromString,
                    response_serializer=booking__pb2.ShowtimeDataTwo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Booking', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Booking(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetBooking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Booking/GetBooking',
            booking__pb2.EmptyTwo.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBookingByUserId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/GetBookingByUserId',
            booking__pb2.UserID.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddBooking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/AddBooking',
            booking__pb2.BookingData.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteBooking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/DeleteBooking',
            booking__pb2.BookingData.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateBooking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/UpdateBooking',
            booking__pb2.BookingData.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetShowtimeTwo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Booking/GetShowtimeTwo',
            booking__pb2.EmptyTwo.SerializeToString,
            booking__pb2.ShowtimeDataTwo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetShowtimeByDateTwo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/GetShowtimeByDateTwo',
            booking__pb2.ShowtimeIDTwo.SerializeToString,
            booking__pb2.ShowtimeDataTwo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetShowtimeByMovieTwo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/GetShowtimeByMovieTwo',
            booking__pb2.ShowtimeDateTwo.SerializeToString,
            booking__pb2.ShowtimeDataTwo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

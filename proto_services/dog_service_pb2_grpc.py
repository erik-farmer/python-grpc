# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import protoc.dog_service_pb2 as dog__service__pb2
import protoc.dogs_pb2 as dogs__pb2


class DogServiceStub(object):
  """A service consumes/returns a protobuf
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PetDog = channel.unary_unary(
        '/DogService/PetDog',
        request_serializer=dogs__pb2.Dog.SerializeToString,
        response_deserializer=dog__service__pb2.ServiceResponse.FromString,
        )


class DogServiceServicer(object):
  """A service consumes/returns a protobuf
  """

  def PetDog(self, request, context):
    """format: 'rpc <rpc_name> (<input_proto>) returns (<output_proto>)'
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DogServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PetDog': grpc.unary_unary_rpc_method_handler(
          servicer.PetDog,
          request_deserializer=dogs__pb2.Dog.FromString,
          response_serializer=dog__service__pb2.ServiceResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'DogService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

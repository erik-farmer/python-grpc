"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc

import greeter_service_pb2
import greeter_service_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = greeter_service_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(greeter_service_pb2.HelloRequest(name='Erik Farmer'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
from protoc.dogs_pb2 import Dog
from proto_services.dog_service_pb2_grpc import DogServiceStub
import grpc


def run():
    # Where are we communicating to?
    channel = grpc.insecure_channel('localhost:50051')
    stub = DogServiceStub(channel)
    # make our input as defined by our service
    wedge = Dog(name='Wedge', breed='Terrier/Chi', age=8)
    response = stub.PetDog(wedge, metadata=[('token', 'sample_token')])
    # our response has a message attribute as defined by ServiceResponse
    print(response.message)


if __name__ == '__main__':
    run()

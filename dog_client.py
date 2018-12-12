from protoc.dogs_pb2 import Dog
from proto_services.dog_service_pb2_grpc import DogServiceStub
import grpc


def run():
    creds = grpc.ssl_channel_credentials(open('server.crt').read().encode('utf8'))
    # Where are we communicating to?
    # channel = grpc.insecure_channel('localhost:50051')
    channel = grpc.secure_channel('localhost:50051', creds)
    stub = DogServiceStub(channel)
    # make our input as defined by our service
    wedge = Dog(name='Wedge', breed='Terrier/Chi', age=8)
    response = stub.PetDog(wedge, metadata=[('token', 'sample_token')])
    # our response has a message attribute as defined by ServiceResponse
    print(response.message)


if __name__ == '__main__':
    run()

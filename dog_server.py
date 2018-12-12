import time
from concurrent.futures import ThreadPoolExecutor
from functools import wraps

# The service and server registration code
from proto_services.dog_service_pb2_grpc import DogServiceServicer, add_DogServiceServicer_to_server
from protoc.dog_service_pb2 import ServiceResponse # The response definition

import grpc


def validate_token_metadata(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        metadata = args[2].invocation_metadata()
        meta_dict = {}
        for md in metadata:
            meta_dict[md.key] = md.value
        if 'token' not in meta_dict:
            return ServiceResponse(message='No token provided error')
        elif meta_dict.get('token') != 'sample_token':
            return ServiceResponse(message='Invalid token provided error')
        else:
            return f(*args, **kwargs)
    return wrapper


# We need to create a class that inherits from the python output of the service proto file.
class DogInterface(DogServiceServicer):
    # Similarly we need to create a method for each rpc in that service definition
    @validate_token_metadata
    def PetDog(self, request, context):
        print('Request: ', request)
        print('Context: ', context)
        print('Metadata: ', context.invocation_metadata())
        return ServiceResponse(message='WHOSE A GOOD BOY? Its {}'.format(request.name))




def serve():
    server = grpc.server(ThreadPoolExecutor())
    add_DogServiceServicer_to_server(DogInterface(), server)
    private_key = open('server.key').read().encode('utf8')
    cert_chain = open('server.crt').read().encode('utf8')
    server_credentials = grpc.ssl_server_credentials(((private_key, cert_chain),))
    # server.add_insecure_port('[::]:50051')
    server.add_secure_port('localhost:50051', server_credentials)
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()

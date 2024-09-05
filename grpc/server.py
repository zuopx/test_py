"""grpc server

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. example.proto
"""


from concurrent import futures
import grpc
import example_pb2
import example_pb2_grpc


class ExampleServiceServicer(example_pb2_grpc.ExampleServiceServicer):
    def SayHello(self, request, context):
        response = example_pb2.HelloResponse()
        response.message = 'Hello, {}!'.format(request.name)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_ExampleServiceServicer_to_server(ExampleServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on port 50051")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

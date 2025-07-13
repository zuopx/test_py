"""
stub.SayHello -> channel.unary_unary

channel有4种调用方式：
    channel.unary_unary -> grpc.UnaryUnaryMultiCallable
    channel.unary_stream -> grpc.UnaryStreamMultiCallable
    channel.stream_unary -> StreamUnaryMultiCallable
    channel.stream_stream -> StreamStreamMultiCallable
"""

import grpc
import example_pb2
import example_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = example_pb2_grpc.ExampleServiceStub(channel)
        request = example_pb2.HelloRequest(name='World')
        response = stub.SayHello(request)
        print(response.message)


if __name__ == '__main__':
    run()

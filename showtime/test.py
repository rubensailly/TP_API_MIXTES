import grpc
import showtime_pb2
import showtime_pb2_grpc

def get_showtime_by_date(stub,id):
    showtime = stub.GetShowtimeByDate(id)
    print(showtime)

def get_list_movies(stub):
    allmovies = stub.GetShowtime(showtime_pb2.Empty())
    for movie in allmovies:
        print(movie)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('127.0.0.1:3002') as channel:
        stub = showtime_pb2_grpc.ShowtimeStub(channel)

        print("-------------- GetShowtimeByDate --------------")
        showtimeid = showtime_pb2.ShowtimeID(id="20151201")
        get_showtime_by_date(stub, showtimeid)

        print("-------------- GetListShowtime --------------")
        get_list_movies(stub)

    channel.close()



if __name__ == '__main__':
    run()
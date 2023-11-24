import grpc
from concurrent import futures
import showtime_pb2
import showtime_pb2_grpc
import json

class ShowtimeServicer(showtime_pb2_grpc.ShowtimeServicer):

    def __init__(self):
        with open('{}/data/times.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["schedule"]

    def GetShowtime(self, request, context):
        for show in self.db:
            yield showtime_pb2.ShowtimeData(date= show["date"], movies= show["movies"])

    def GetShowtimeByDate(self, request, context):
        for show in self.db:
            if request.id == show["date"]:
                return showtime_pb2.ShowtimeData(date= show["date"], movies= show["movies"])
        return showtime_pb2.ShowtimeData(date="", movies="")
    def GetShowtimeByMovie(self, request, context):
        for show in self.db:
            if request.id in show["movies"]:
                yield showtime_pb2.ShowtimeData(date= show["date"], movies= show["movies"])
        return showtime_pb2.ShowtimeData(date="", movies="")
    


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    showtime_pb2_grpc.add_ShowtimeServicer_to_server(ShowtimeServicer(), server)
    server.add_insecure_port('127.0.0.1:3002')
    server.start()
    print("Serveur démaré")
    server.wait_for_termination()
    print("Serveur stoppé")


if __name__ == '__main__':
    serve()

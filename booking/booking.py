import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc
import json
import showtime_pb2
import showtime_pb2_grpc
from google.protobuf.json_format import MessageToJson

class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self):
        with open('{}/data/bookings.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["bookings"]

    def GetShowtimeTwo(self, request, context):
        with grpc.insecure_channel('127.0.0.1:3002') as channel:
            stub = showtime_pb2_grpc.ShowtimeStub(channel)
            result = stub.GetShowtime(showtime_pb2.Empty())
            print(result)
            for i in result:
                #print("new date ? ", i)

                new_i = MessageToJson(i)
                #print(new_i, type(new_i))
                json_obj = json.loads(new_i)
                #print(json_obj["date"])
                yield booking_pb2.ShowtimeDataTwo(date=json_obj["date"], movies=json_obj["movies"])


    def GetBooking(self, request, context):
        for booking in self.db:
            yield booking_pb2.BookingData(userid=booking["userid"], dates=[{"date": d["date"], "movies": d["movies"]} for d in booking["dates"]])

    def GetBookingByUserId(self, request, context):
        for booking in self.db:
            print(booking)
            if booking["userid"] == request.userid:
                return booking_pb2.BookingData(userid=booking["userid"],dates=[{"date": d["date"], "movies": d["movies"]} for d in booking["dates"]])
        return booking_pb2.BookingData()

    def GetBookingByDate(self, request, context):
        for booking in self.db:
            for date in booking["dates"]:
                if date["date"] == request.date:
                    return booking_pb2.BookingData(userid=booking["userid"],dates=[{"date": d["date"], "movies": d["movies"]} for d in booking["dates"]])
        return booking_pb2.BookingData()

    def GetBookingByMovie(self, request, context):
        for booking in self.db:
            for date in booking["dates"]:
                if request.movie in date["movies"]:
                    return booking_pb2.BookingData(userid=booking["userid"],dates=[{"date": d["date"], "movies": d["movies"]} for d in booking["dates"]])
        return booking_pb2.BookingData()
        
    def AddBooking(self, request, context):
        booking = {"userid": request.userid, "dates": [{"date": d.date, "movies": d.movies} for d in request.dates]}
        date_concernerd = booking["dates"][0]["date"]
        movie_concernerd = booking["dates"][0]["movies"][0]
        #print("-------------")
        #print(date_concernerd, movie_concernerd)
        #print("-------------")
        #self.db.append(booking)
        z = 0
        for booking in self.db:
            #print(booking)
            if booking['userid'] == request.userid :
                i = 0
                date_dont_exist = True
                for date in booking['dates']:
                    #print(date)
                    if date['date'] == date_concernerd:
                        #print(date['movies'], movie_concernerd)
                        date_dont_exist = False
                        if movie_concernerd in date['movies']:
                            print("movie already booked this day")
                            #print("print self :", self.db[z]['dates'][i])
                        else:
                            self.db[z]['dates'][i]['movies'].append(movie_concernerd)
                    i += 1
                if date_dont_exist == True:
                    #print("print self :::", self.db[z]['dates'])
                    self.db[z]['dates'].append({'date': date_concernerd, 'movies': [movie_concernerd]})
            z+=1
        return booking_pb2.BookingData(userid=booking["userid"],dates=[{"date": d["date"], "movies": d["movies"]} for d in booking["dates"]])
    
    def DeleteBooking(self, request, context):
        z = 0
        for booking in self.db:
            if booking["userid"] == request.userid:
                json_obj = json.loads(MessageToJson(request))['dates'][0]
                print(json_obj)
                print(booking['dates'])
                j = 0
                for date in booking['dates']:
                    if date['date'] == json_obj['date']:
                        movies_to_del = json_obj['movies']
                        i = 0
                        for movie in date['movies']:
                            print(movie, movies_to_del[0])
                            if movie in movies_to_del:
                                print("movie to del : ", movie)
                                print("print self", self.db[z]['dates'][j]['movies'][i])
                                self.db[z]['dates'][j]['movies'].remove(self.db[z]['dates'][j]['movies'][i])
                            i+=1
                    j+=1
                return booking_pb2.BookingData(userid=booking["userid"],dates=[{"date": d["date"], "movies": d["movies"]} for d in booking["dates"]])
            z += 1
        return booking_pb2.BookingData()
    
    def UpdateBooking(self, request, context):
        for booking in self.db:
            if booking["userid"] == request.userid:
                booking["dates"] = [{"date": d.date, "movies": d.movies} for d in request.dates]
                return booking_pb2.BookingData(userid=booking["userid"],dates=[{"date": d["date"], "movies": d["movies"]} for d in booking["dates"]])
        return booking_pb2.BookingData()

    def GetShowtimeByDateTwo(self, request, context):
        return booking_pb2.ShowtimeDataTwo()

    def GetShowtimeByMovieTwo(self, request, context):
        with grpc.insecure_channel('127.0.0.1:3002') as channel:
            stub = showtime_pb2_grpc.ShowtimeStub(channel)
            result = stub.GetShowtimeByMovie(showtime_pb2.ShowtimeDate(date="20151201"))
            print(result)
            for i in result:
                # print("new date ? ", i)

                new_i = MessageToJson(i)
                # print(new_i, type(new_i))
                json_obj = json.loads(new_i)
                # print(json_obj["date"])
                yield booking_pb2.ShowtimeDataTwo(date=json_obj["date"], movies=json_obj["movies"])
        """
        with grpc.insecure_channel('127.0.0.1:3002') as channel:
            stub = showtime_pb2_grpc.ShowtimeStub(channel)
            result = stub.GetShowtime(showtime_pb2.Empty())
            for i in result:
                print(i)
            channel.close()"""





def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('127.0.0.1:3003')
    server.start()

    """ 
        with grpc.insecure_channel('127.0.0.1:3002') as channel:
        stub = showtime_pb2_grpc.ShowtimeStub(channel)
        result = stub.GetShowtime(showtime_pb2.Empty())
        print(result)
        for i in result:
            print(i)
        channel.close()
    """
    print("Serveur démarré")

    server.wait_for_termination()
    print("Serveur stoppé")


if __name__ == '__main__':
    serve()

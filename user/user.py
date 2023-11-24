import grpc
from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound
from google.protobuf.json_format import MessageToJson


import booking_pb2_grpc, booking_pb2

app = Flask(__name__)

PORT = 3203
HOST = '127.0.0.1'

with open('{}/data/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the User service!</h1>"

@app.route("/user/", methods=['GET'])
def get_users():
   res = make_response(jsonify(users), 200)
   return res

@app.route("/user/<id>", methods=['GET'])
def get_userid(id):
   for user in users:
      if str(user["id"]) == str(id):
         res = make_response(jsonify(user))
         return res
   res = make_response(jsonify("message: user not found"), 200)
   return res

#Pouvoir voir les réservations de tout les utilisateurs
@app.route("/reservations", methods=['GET'])
def get_reservations():
    data = {
        "reservations": [

        ]
    }

    with grpc.insecure_channel('127.0.0.1:3003') as channel:

        booking_stub = booking_pb2_grpc.BookingStub(channel)
        reservations = booking_stub.GetBooking(booking_pb2.EmptyTwo())

        for reservation in reservations:
            reservation = MessageToJson(reservation)

            json_obj = json.loads(reservation)
            date_entry = {"userid": json_obj["userid"], "dates": []}
            for dates in json_obj["dates"]:
                print(dates, dates["date"])
                one_date_entry = {"date": dates["date"], "movies": []}

                for movie in dates["movies"]:
                    query = '''
                                    query {
                                        movie_with_id(_id: "''' + movie + '''") {
                                            title
                                        }
                                    }
                                    '''
                    response = requests.post("http://127.0.0.1:3001/graphql", json={'query': query})
                    film = response.json()["data"]["movie_with_id"]
                    one_date_entry["movies"].append(film)
                date_entry["dates"].append(one_date_entry)
            data["reservations"].append(date_entry)

        return jsonify(data), 200

    res = make_response(jsonify("message: user not found"), 200)
    return res


#Faire à la toute fin...
@app.route("/reservations/<userid>", methods=['GET'])
def get_reservation(userid):
    for user in users:
        if str(user["id"]) == str(userid):
            print(user)
            print(user["id"])
            data = {
                "reservations": [

                ]
            }

            with grpc.insecure_channel('127.0.0.1:3003') as channel:
                #showtime_stub = showtime_pb2_grpc.ShowtimeStub(channel)
                booking_stub = booking_pb2_grpc.BookingStub(channel)

                #user = user.json()
                #print(user)
                #booking_request = booking_pb2.GetBookingByUserId(userid=userid)
                user_id_request = booking_pb2.UserID(userid=userid)
                print(user_id_request)
                reservations = booking_stub.GetBookingByUserId(user_id_request)
                print("ici ça bug")
                print(reservations)



                for reservation in reservations.dates:
                    date_entry = {"date": reservation.date, "movies": []}
                    for movie in reservation.movies:
                        print(movie)
                        query = '''
                                        query {
                                            movie_with_id(_id: "''' + movie + '''") {
                                                title
                                            }
                                        }
                                        '''
                        response = requests.post("http://127.0.0.1:3001/graphql", json={'query': query})
                        film = response.json()["data"]["movie_with_id"]
                        date_entry["movies"].append(film)
                    data["reservations"].append(date_entry)


                return jsonify(data), 200

    res = make_response(jsonify("message: user not found"), 200)
    return res

@app.route("/user/", methods=['POST'])
def add_user():
   user = request.get_json()
   users.append(user)
   res = make_response(jsonify(user), 200)
   return res

@app.route("/user/<id>", methods=['PUT'])
def update_user(id):
   user = request.get_json()
   for i in range(len(users)):
      if str(users[i]["id"]) == str(id):
         users[i] = user
         res = make_response(jsonify(user), 200)
         return res
   res = make_response(jsonify("message: user not found"), 200)
   return res

@app.route("/user/<id>", methods=['DELETE'])
def delete_user(id):
   for i in range(len(users)):
      if str(users[i]["id"]) == str(id):
         del users[i]
         res = make_response(jsonify("message: user deleted"), 200)
         return res
   res = make_response(jsonify("message: user not found"), 200)
   return res

#Pouvoir faire une réservation
@app.route("/user/<userid>/reservation", methods=['POST'])
def add_reservation(userid):
    user = request.get_json()
    print(user)
    concernerd_date = user['dates'][0]['date']
    concernerd_movie = user['dates'][0]['movies'][0]
    print(concernerd_date, concernerd_movie)
    with grpc.insecure_channel('127.0.0.1:3003') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)
        data = stub.GetShowtimeTwo(booking_pb2.EmptyTwo())
        # print("stub ? ", data)
        for i in data:
            json_obj = json.loads(MessageToJson(i))
            print(json_obj)
            if json_obj['date'] == concernerd_date:
                print(json_obj['movies'])
                if concernerd_movie in json_obj['movies']:
                    for date in user['dates']:
                        with grpc.insecure_channel('127.0.0.1:3003') as channel:
                            stub = booking_pb2_grpc.BookingStub(channel)
                            Dates = booking_pb2.Dates(date=date['date'], movies=date['movies'])
                            stub.AddBooking(booking_pb2.BookingData(userid=userid, dates=[Dates]))
                        res = make_response(jsonify(user), 200)
                    return res
        res = make_response(jsonify({"erreur": "séance inexistante"}), 400)
        return res


#Pouvoir supprimer une réservation
@app.route("/user/<userid>/reservation", methods=['DELETE'])
def delete_reservation(userid):
    user = request.get_json()
    #print(user['dates'])
    for date in user['dates']:
        #print(date['date'], date['movies'])
        with grpc.insecure_channel('127.0.0.1:3003') as channel:
            stub = booking_pb2_grpc.BookingStub(channel)
            Dates = booking_pb2.Dates(date=date['date'], movies=date['movies'])
            stub.DeleteBooking(booking_pb2.BookingData(userid=userid, dates=[Dates]))
        res = make_response(jsonify(user), 200)
    return res

#Pouvoir modifier une réservation
@app.route("/user/<userid>/reservation", methods=['PUT'])
def update_reservation(userid):
    user = request.get_json()
    with grpc.insecure_channel('127.0.0.1:3003') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)
        stub.UpdateBooking(user)
    res = make_response(jsonify(user), 200)
    return res

#Voir tout les films disponibles ::::: Faire en sorte de voir la date ?
@app.route("/movies", methods=['GET'])
def get_movies():
    query = '''
        query GetAllMovies {
            getAllMovies {
                id
                title
            }
        }
        '''
    response = requests.post("http://127.0.0.1:3001/graphql", json={'query': query})
    print(response.json())
    movies = response.json()["data"]["getAllMovies"]
    res = make_response(jsonify(movies), 200)
    return res

#Voir les films disponibles à une date donnée //pour l'instant inutile car c'est un autre truc
@app.route("/movies/<date>", methods=['GET'])
def get_movies_by_date(date):
    #On va devoir faire appel à showtime ainsi qu'à movies
    with grpc.insecure_channel('127.0.0.1:3003') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)
        data = stub.GetShowtimeTwo(booking_pb2.EmptyTwo())
        #print("stub ? ", data)
        for i in data:
            json_obj = json.loads(MessageToJson(i))
            print(json_obj)
            if json_obj["date"] == date:
                print(json_obj["movies"])
                saved_movies = []
                for movie in json_obj["movies"]:
                    print("movie", movie)
                    query = '''
                                                            query {
                                                                movie_with_id(_id: "''' + movie + '''") {
                                                                    title
                                                                }
                                                            }
                                                            '''
                    response = requests.post("http://127.0.0.1:3001/graphql", json={'query': query})
                    film = response.json()["data"]["movie_with_id"]
                    print(film['title'])
                    saved_movies.append(film['title'])
    to_ret={"date": date, "movies":saved_movies}
    res = make_response(jsonify(to_ret), 200)
    return res


if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)

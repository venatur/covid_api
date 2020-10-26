from . import covid
from app.models import Estados, Municipios, Registros, Cambios, Historia, Nuevos
import json
from flask import jsonify, make_response


@covid.route('/municipios/')
def muni():
    municipios = Municipios.query.all()
    return make_response(jsonify(municipios), 200)


@covid.route('/estados/')
def estados():

    estados = Estados.query.all()
    return make_response(jsonify(estados), 200)

@covid.route('/casosdiarios1/')
def diarios1():
    diarios1 = Registros.query.all()
    return make_response(jsonify(diarios1), 200)

@covid.route('/cambios/')
def cambios():
    cambios = Cambios.query.yield_per(10000).enable_eagerloads(False).all()
    print(Cambios.query.count())
    return make_response(jsonify(cambios), 200)

@covid.route('/historia/')
def historia():
    historia = Historia.query.yield_per(10000).enable_eagerloads(False).all()
    print(Historia.query.count())
    return make_response(jsonify(historia), 200)

@covid.route('/nuevos/')
def nuevos():
    nuevos = Nuevos.query.yield_per(10000).enable_eagerloads(False).all()
    print(nuevos.query.count())
    return make_response(jsonify(nuevos), 200)

@covid.route('/hola/')
def hola():
    return 'hola mundo'
from . import covid
from sqlalchemy import text
from app.models import Estados, Municipios, Registros, Cambios, Historia, Nuevos, Nacionalidad, Origen, Resultado,\
    Sector, Sexo, Tipo_paciente
from app import connecta
from app import pandita
from flask import jsonify, make_response, send_file, Response, request
import json


@covid.route('/sector/')
def sector():
    sector = Sector.query.all()
    return make_response(jsonify(sector), 200)


@covid.route('/sexo/')
def sexo():
    sexo = Sexo.query.all()
    return make_response(jsonify(sexo), 200)


@covid.route('/tipo_paciente/')
def tipo_paciente():
    tipo_paciente = Tipo_paciente.query.all()
    return make_response(jsonify(tipo_paciente), 200)


@covid.route('/resultado/')
def resultado():
    resultado = Resultado.query.all()
    return make_response(jsonify(resultado), 200)


@covid.route('/origen/')
def origen():
    origen = Origen.query.all()
    return make_response(jsonify(origen), 200)


@covid.route('/nacionalidad/')
def nacionalidad():
    nacionalidad = Nacionalidad.query.all()
    return make_response(jsonify(nacionalidad), 200)


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
    stmt = text("select historia.id_registro from historia limit 100000")
    historia = Historia.query.from_statement(stmt).all()
    #print(historia)
    return make_response(jsonify(historia), 200)


@covid.route('/nuevos/')
def nuevos():
    nuevos = Nuevos.query.yield_per(10000).enable_eagerloads(False).all()
    print(nuevos.query.count())
    return make_response(jsonify(nuevos), 200)


@covid.route('/home', methods=['GET'])
def home():
    obj = connecta.connect()
    headers = pandita.get_headers(obj, 'nuevos')
    month = request.args["month"]
    if request.args:
        print(month)
        df = pandita.postgresql_to_dataframe(obj, "select * from nuevos where to_char(fecha_actualizacion,'MM') = '%s'" % month, headers)
        return Response(df.to_json(orient='split'), mimetype='application/json')
    else:
        df = pandita.postgresql_to_dataframe(obj, 'select * from nuevos', headers)
        return Response(df.to_json(orient='split'), mimetype='application/json')
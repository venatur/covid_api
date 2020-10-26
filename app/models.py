from . import db
from dataclasses import dataclass

@dataclass
class Estados(db.Model):
    __tablename__='estados'
    clave_entidad = db.Column(db.Text(), primary_key=True, nullable=False)
    entidad_federativa = db.Column(db.Text(),nullable=False)
    abreviatura = db.Column(db.Text(),nullable=False)

    clave_entidad: int
    entidad_federativa: str
    abreviatura: int

    def __init__(self, clave_entidad, entidad_federativa, abreviatura):
        self.clave = clave_entidad
        self.entidad = entidad_federativa
        self.abrev = abreviatura

@dataclass
class Municipios(db.Model):
    __tablename__ = 'municipios'
    clave_municipio = db.Column(db.Text(), primary_key=True, nullable=False)
    municipio = db.Column(db.Text(), nullable=False)
    clave_entidad = db.Column(db.Text(), nullable=False)

    clave_municipio: int
    municipio: str
    clave_entidad: int

    def __init__(self, clave_municipio, municipio, clave_entidad):
        self.clave_municipio = clave_municipio
        self.municipio = municipio
        self.clave_entidad = clave_entidad

@dataclass
class Registros(db.Model):
    __tablename__ = 'registros'
    diarios = db.Column(db.Text(), nullable=False)
    fecha = db.Column(db.Text(), primary_key=True, nullable=False)

    diarios: int
    fecha: int

@dataclass
class Cambios(db.Model):
    __tablename__ = 'cambios'
    id_registro = db.Column(db.Text(), primary_key=True, nullable=False)
    origen = db.Column(db.Integer)
    sector = db.Column(db.Integer)
    entidad_um = db.Column(db.Integer)
    sexo = db.Column(db.String(1))
    entidad_nac = db.Column(db.Integer)
    entidad_res = db.Column(db.Integer)
    municipio_res = db.Column(db.Integer)
    tipo_paciente = db.Column(db.Integer)
    fecha_ingreso = db.Column(db.Text())
    fecha_sintomas = db.Column(db.Text())
    fecha_def = db.Column(db.Text())
    intubado = db.Column(db.Integer)
    neumonia = db.Column(db.Integer)
    edad = db.Column(db.Integer)
    nacionalidad = db.Column(db.Integer)
    embarazo = db.Column(db.Integer)
    habla_lengua = db.Column(db.Integer)
    diabetes = db.Column(db.Integer)
    epoc = db.Column(db.Integer)
    asma = db.Column(db.Integer)
    inmunospr = db.Column(db.Integer)
    hipertension = db.Column(db.Integer)
    otra_com = db.Column(db.Integer)
    cardiovascular = db.Column(db.Integer)
    obesidad = db.Column(db.Integer)
    renal_cronica = db.Column(db.Integer)
    tabaquismo = db.Column(db.Integer)
    otro_caso = db.Column(db.Integer)
    resultado_lab = db.Column(db.Integer)
    migrante = db.Column(db.Integer)
    pais_nacionalidad = db.Column(db.Text())
    pais_origen = db.Column(db.Text())
    uci = db.Column(db.Integer)
    fecha = db.Column(db.Date)
    indigena = db.Column(db.Integer)
    toma_muestra = db.Column(db.Integer)
    clasificacion_final = db.Column(db.Integer)

    id_registro: str
    origen: int
    sector: int
    entidad_um: int
    sexo: int
    entidad_nac: int
    entidad_res: int
    municipio_res: int
    tipo_paciente: int
    fecha_ingreso: int
    fecha_sintomas: int
    fecha_def: int
    intubado: int
    neumonia: int
    edad: int
    nacionalidad: int
    embarazo: int
    habla_lengua: int
    diabetes: int
    epoc: int
    asma: int
    inmunospr: int
    hipertension: int
    otra_com: int
    cardiovascular: int
    obesidad: int
    renal_cronica: int
    tabaquismo: int
    otro_caso: int
    resultado_lab: int
    migrante: int
    pais_nacionalidad: int
    pais_origen: int
    uci: int
    fecha: int
    indigena: int
    toma_muestra: int
    clasificacion_final: int

@dataclass()
class Historia(db.Model):
    __tablename__ = 'historia'
    fecha_actualizacion = db.Column(db.Text())
    id_registro = db.Column(db.Text(), primary_key=True, nullable=False)
    origen = db.Column(db.Integer)
    sector = db.Column(db.Integer)
    entidad_um = db.Column(db.Integer)
    sexo = db.Column(db.String(1))
    entidad_nac = db.Column(db.Integer)
    entidad_res = db.Column(db.Integer)
    municipio_res = db.Column(db.Integer)
    tipo_paciente = db.Column(db.Integer)
    fecha_ingreso = db.Column(db.Text())
    fecha_sintomas = db.Column(db.Text())
    fecha_def = db.Column(db.Text())
    intubado = db.Column(db.Integer)
    neumonia = db.Column(db.Integer)
    edad = db.Column(db.Integer)
    nacionalidad = db.Column(db.Integer)
    embarazo = db.Column(db.Integer)
    habla_lengua_indig = db.Column(db.Integer)
    diabetes = db.Column(db.Integer)
    epoc = db.Column(db.Integer)
    asma = db.Column(db.Integer)
    inmusupr = db.Column(db.Integer)
    hipertension = db.Column(db.Integer)
    otra_com = db.Column(db.Integer)
    cardiovascular = db.Column(db.Integer)
    obesidad = db.Column(db.Integer)
    renal_cronica = db.Column(db.Integer)
    tabaquismo = db.Column(db.Integer)
    otro_caso = db.Column(db.Integer)
    resultado_lab = db.Column(db.Integer)
    migrante = db.Column(db.Integer)
    pais_nacionalidad = db.Column(db.Text())
    pais_origen = db.Column(db.Text())
    uci = db.Column(db.Integer)
    indigena = db.Column(db.Integer)
    toma_muestra = db.Column(db.Integer)
    clasificacion_final = db.Column(db.Integer)

    fecha_actualizacion: str
    id_registro: str
    origen: int
    sector: int
    entidad_um: int
    sexo: int
    entidad_nac: int
    entidad_res: int
    municipio_res: int
    tipo_paciente: int
    fecha_ingreso: int
    fecha_sintomas: int
    fecha_def: int
    intubado: int
    neumonia: int
    edad: int
    nacionalidad: int
    embarazo: int
    habla_lengua_indig: int
    diabetes: int
    epoc: int
    asma: int
    inmusupr: int
    hipertension: int
    otra_com: int
    cardiovascular: int
    obesidad: int
    renal_cronica: int
    tabaquismo: int
    otro_caso: int
    resultado_lab: int
    migrante: int
    pais_nacionalidad: int
    pais_origen: int
    uci: int
    indigena: int
    toma_muestra: int
    clasificacion_final: int

@dataclass()
class Nuevos(db.Model):
    __tablename__ = 'nuevos'
    fecha_actualizacion = db.Column(db.Text())
    id_registro = db.Column(db.Text(), primary_key=True, nullable=False)
    origen = db.Column(db.Integer)
    sector = db.Column(db.Integer)
    entidad_um = db.Column(db.Integer)
    sexo = db.Column(db.String(1))
    entidad_nac = db.Column(db.Integer)
    entidad_res = db.Column(db.Integer)
    municipio_res = db.Column(db.Integer)
    tipo_paciente = db.Column(db.Integer)
    fecha_ingreso = db.Column(db.Text())
    fecha_sintomas = db.Column(db.Text())
    fecha_def = db.Column(db.Text())
    intubado = db.Column(db.Integer)
    neumonia = db.Column(db.Integer)
    edad = db.Column(db.Integer)
    nacionalidad = db.Column(db.Integer)
    embarazo = db.Column(db.Integer)
    habla_lengua_indig = db.Column(db.Integer)
    diabetes = db.Column(db.Integer)
    epoc = db.Column(db.Integer)
    asma = db.Column(db.Integer)
    inmusupr = db.Column(db.Integer)
    hipertension = db.Column(db.Integer)
    otra_com = db.Column(db.Integer)
    cardiovascular = db.Column(db.Integer)
    obesidad = db.Column(db.Integer)
    renal_cronica = db.Column(db.Integer)
    tabaquismo = db.Column(db.Integer)
    otro_caso = db.Column(db.Integer)
    resultado_lab = db.Column(db.Integer)
    migrante = db.Column(db.Integer)
    pais_nacionalidad = db.Column(db.Text())
    pais_origen = db.Column(db.Text())
    uci = db.Column(db.Integer)
    indigena = db.Column(db.Integer)
    toma_muestra = db.Column(db.Integer)
    clasificacion_final = db.Column(db.Integer)

    fecha_actualizacion: str
    id_registro: str
    origen: int
    sector: int
    entidad_um: int
    sexo: int
    entidad_nac: int
    entidad_res: int
    municipio_res: int
    tipo_paciente: int
    fecha_ingreso: int
    fecha_sintomas: int
    fecha_def: int
    intubado: int
    neumonia: int
    edad: int
    nacionalidad: int
    embarazo: int
    habla_lengua_indig: int
    diabetes: int
    epoc: int
    asma: int
    inmusupr: int
    hipertension: int
    otra_com: int
    cardiovascular: int
    obesidad: int
    renal_cronica: int
    tabaquismo: int
    otro_caso: int
    resultado_lab: int
    migrante: int
    pais_nacionalidad: int
    pais_origen: int
    uci: int
    indigena: int
    toma_muestra: int
    clasificacion_final: int
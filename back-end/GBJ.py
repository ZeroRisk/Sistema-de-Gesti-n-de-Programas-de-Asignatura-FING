from flask import Flask,request,render_template, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

mysql = MySQL()
app = Flask(__name__)
CORS(app)
# Datos de configuracion de la app. Principalmente de la conexión a MySql. 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mydb'
app.config['MYSQL_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/")
def home():
	return 'HELLO WORLD! '

@app.route("/dejavu")
def dejaVu():
	return 'I\'ve just been in this place before...'

#----------------------------------------------#
# LOS SERVICIOS GET DEL SISTEMA                #
#----------------------------------------------#


#----------------------------------------------#
# Funcion: Obtiene todos los usuarios del sistema, con sus datos.
#
# Entrada: No posee entrada.
#
# Salida: Objeto json conteniendo todos los usuarios del sistema.
#----------------------------------------------#

@app.route("/userAsign", methods=['GET'])
def getUsersAsign():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from usuario")
    data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'Users' : data})

#----------------------------------------------#
# Funcion: Obtiene todos los programas del sistema, con sus datos.
#
# Entrada: No posee entrada.
#
# Salida: Objeto json conteniendo todos los programas del sistema.
#----------------------------------------------#

@app.route("/programs", methods=['GET'])
def getPrograms():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from programa")
    data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'programs' : data})


#----------------------------------------------#
# Funcion: Obtiene todas los asignaturas del sistema, con sus datos.
#
# Entrada: No posee entrada.
#
# Salida: Objeto json conteniendo todas las asignaturas del sistema.
#----------------------------------------------#


@app.route("/asignaturas", methods=['GET'])
def getAsignaturas():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from asignatura")
    data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'asignaturas' : data})


#----------------------------------------------#
# Funcion: Obtiene todos los planes del sistema, con sus datos.
#
# Entrada: No posee entrada.
#
# Salida: Objeto json conteniendo todos los planes del sistema.
#----------------------------------------------#


@app.route("/planes", methods=['GET'])
def getPlanes():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from plan_estudio")
    data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'planes' : data})


#----------------------------------------------#
# Funcion: Obtiene todos los programas del sistema, con sus datos. Junto a estos,
#          se adhiere los datos de la asignatura a la que corresponde el programa y el
#          el detalle del programa.
#
# Entrada: No posee entrada.
#
# Salida: Objeto json conteniendo todos los programas del sistema, junto con los datos de la asignatura y el detalle del programa.
#----------------------------------------------#


@app.route("/programsComplete", methods=['GET'])
def getProgramsCOM():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM mydb.programa as p INNER JOIN mydb.detalle_programa as dp on p.detalle_programa_iddetalle_programa = dp.iddetalle_programa INNER JOIN mydb.asignatura as asig on p.asignatura_idasignatura = asig.idasignatura")
    data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'programs' : data})

#----------------------------------------------#
# Funcion: Obtiene todos los programas del sistema, con sus datos. Junto al detalle del programa,
#          y la asignatura. El programa esta asignado a un usuario en especifico.
#
# Entrada: ID del usuario del cual se obtiene sus programas asignados ("userid"). 
#          Se entrega mediante url.
#
# Salida: Objeto json conteniendo todos los programas del sistema, que el usuario tenga asignado.
#         Incluye el detalle del programa y la asignatura.
#----------------------------------------------#


@app.route("/getAsignedPrograms", methods=['GET'])
def getAsignedPrograms():
	userID = request.args.get('userid')
	cursor = mysql.connection.cursor()
	cursor.execute("SELECT * FROM mydb.programa as p INNER JOIN mydb.detalle_programa as dp on p.detalle_programa_iddetalle_programa = dp.iddetalle_programa INNER JOIN mydb.asignatura as asig on p.asignatura_idasignatura = asig.idasignatura INNER JOIN mydb.usuario_programa as usp on p.idprograma = usp.programa_idprograma where usp.usuario_idusuario = "+userID+"")
	data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
	return jsonify({'programs' : data})

#----------------------------------------------#
# Funcion: Obtiene todo el detalle de un programa, y sus unidades, en base al id de la asignatura.
#
# Entrada: ID de la asignatura ("asignaId"). 
#          Se entrega mediante url.
#
# Salida: Objeto json conteniendo el detalle del programa y de sus unidades.
#----------------------------------------------#


@app.route("/getAllDetalle", methods=['GET'])
def getAllDetalle():
	idAsignatura = request.args.get('asignaId')
	cursor = mysql.connection.cursor()
	cursor.execute("SELECT * FROM detalle_programa as d_p INNER JOIN unidades as u on u.detalle_programa_iddetalle_programa = d_p.iddetalle_programa INNER JOIN unidad_tematica as u_t on u_t.unidades_idunidades = u.idunidades INNER JOIN programa as p on p.detalle_programa_iddetalle_programa = d_p.iddetalle_programa where p.asignatura_idasignatura = "+idAsignatura+"")
	data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
	return jsonify({'AllDetalle' : data})


#----------------------------------------------#
# Funcion: Obtención de todo el contenido del programa, a traves del id del detalle.
#          Incluye detalle del programa, evaluacion, unidades y subunidades.
#
# Entrada: ID del detalle del programa ("iddetalle"). 
#          Se entrega mediante url.
#
# Salida: Objeto json conteniendo el detalle del programa, evaluacion, unidades y subunidades.
#----------------------------------------------#


@app.route("/desarrolloP", methods=['GET'])
def getDesarrolloP():
	detalleid = request.args.get('iddetalle')

	cursor = mysql.connection.cursor()
	cursor.execute("SELECT * FROM detalle_programa WHERE iddetalle_programa = "+detalleid+"")
	dataD= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]

	cursor.execute("SELECT * FROM unidades WHERE detalle_programa_iddetalle_programa = "+detalleid+"")
	dataU= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]

	cursor.execute("SELECT * FROM unidad_tematica WHERE unidades_idunidades IN (SELECT idunidades FROM unidades WHERE detalle_programa_iddetalle_programa = "+detalleid+")")
	dataSU= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]

	cursor.execute("SELECT * FROM evaluacion WHERE detalle_programa_iddetalle_programa = "+detalleid+"")
	dataE= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
    
	return jsonify({'Desarrollo' : dataD, 'Unidades' : dataU, 'SubUnidades' : dataSU, 'Evaluacion' : dataE})


#----------------------------------------------#
# Funcion: Busqueda de programa por nombre de asignatura y fecha de creación.
#          Retorna los datos del programa.
#
# Entrada: nombre de la asignatura ("asignatura").
#          fecha de creacion del programa ("fecha"). 
#          Se entrega mediante url.
#
# Salida: Objeto json conteniendo los datos del programa.
#----------------------------------------------#


@app.route("/programNF", methods=['GET'])
def getProgramNF():
    asignatura = request.args.get('asignatura')
    fecha = request.args.get('fecha')
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM programa WHERE asignatura_idasignatura = (SELECT idasignatura FROM asignatura WHERE nombreAsignatura = '"+ asignatura+"') AND fechacreacion = '"+fecha+"'")
    data = [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
    if data is None:
     return "Data not valid"
    else:
     return jsonify({'program' : data})

#----------------------------------------------#
# Funcion: Busqueda de programa por código de asignatura.
#          Retorna los datos del programa.
#
# Entrada: codigo de la asignatura ("codigo").
#          Se entrega mediante url.
#
# Salida: Objeto json conteniendo los datos del programa.
#----------------------------------------------#


@app.route("/programCodigo", methods=['GET'])
def getProgramCodigo():
    codigo = request.args.get('codigo')
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM programa WHERE asignatura_idasignatura = (SELECT idasignatura FROM asignatura WHERE codigo = '"+codigo+"')")
    data = [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
    if data is None:
     return "Data not valid"
    else:
     return jsonify({'program' : data})

#----------------------------------------------#
# Funcion: Busqueda de programa por nivel de asignatura.
#          Retorna los datos del programa.
#
# Entrada: nivel de la asignatura ("nivel").
#          Se entrega mediante url.
#
# Salida: Objeto json conteniendo los datos del programa.
#----------------------------------------------#


@app.route("/programNivel", methods=['GET'])
def getProgramNivel():
    nivel = request.args.get('nivel')
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM programa WHERE asignatura_idasignatura = (SELECT idasignatura FROM asignatura WHERE nivel = "+nivel+")")
    data = [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
    if data is None:
     return "Data not valid"
    else:
     return jsonify({'program' : data})

#----------------------------------------------#
# Funcion: Busqueda de programa por tipo de asignatura.
#          Retorna los datos del programa.
#
# Entrada: tipo de la asignatura ("tipo").
#          Se entrega mediante url.
#
# Salida: Objeto json conteniendo los datos del programa.
#----------------------------------------------#


@app.route("/programTipo", methods=['GET'])
def getProgramTipo():
    tipo = request.args.get('tipo')
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM programa WHERE asignatura_idasignatura = (SELECT idasignatura FROM asignatura WHERE tipo = '"+tipo+"')")
    data = [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
    if data is None:
     return "Data not valid"
    else:
     return jsonify({'program' : data})

#----------------------------------------------#
# Funcion: Busqueda de programa por multiples parametros de asignatura.
#          Estos pueden ser nivel y/o tipo y/o codigo.
#          Retorna los datos del programa.
#
# Entrada: codigo de la asignatura ("codigo").
#          nivel de la asignatura ("nivel").
#          tipo de la asignatura ("tipo").
#          Se entrega mediante url. No es necesario ingresar todas las entradas.
#          La busqueda se genera en base a que entradas se encuentren ingresadas.
#
# Salida: Objeto json conteniendo los datos del programa.
#----------------------------------------------#


@app.route("/programMultiple", methods=['GET'])
def getProgramMultiple():
    nivel = request.args.get('nivel')
    tipo = request.args.get('tipo')
    codigo = request.args.get('codigo')

    cursor = mysql.connection.cursor()

    if nivel is None and tipo is None and codigo is None:
    	return "No hay filtro de busqueda!"

    if nivel is None and tipo is None:
	    cursor.execute("SELECT * FROM programa WHERE asignatura_idasignatura = (SELECT idasignatura FROM asignatura WHERE codigo = '"+codigo+"')")
	    data = [dict((cursor.description[i][0], value)
			for i, value in enumerate(row)) for row in cursor.fetchall()]
	    if data is None:
	    	return "Data not valid"
	    else:
	    	return jsonify({'program' : data})
    if nivel is None and codigo is None:
	    cursor.execute("SELECT * FROM programa WHERE asignatura_idasignatura = (SELECT idasignatura FROM asignatura WHERE tipo = '"+tipo+"')")
	    data = [dict((cursor.description[i][0], value)
			for i, value in enumerate(row)) for row in cursor.fetchall()]
	    if data is None:
	    	return "Data not valid"
	    else:
	    	return jsonify({'program' : data})
    if tipo is None and codigo is None:
	    cursor.execute("SELECT * FROM programa WHERE asignatura_idasignatura = (SELECT idasignatura FROM asignatura WHERE nivel = "+nivel+")")
	    data = [dict((cursor.description[i][0], value)
			for i, value in enumerate(row)) for row in cursor.fetchall()]
	    if data is None:
	    	return "Data not valid"
	    else:
	    	return jsonify({'program' : data})	
    if nivel is None:
	    cursor.execute("SELECT * FROM programa WHERE asignatura_idasignatura = (SELECT idasignatura FROM asignatura WHERE tipo = '"+tipo+"' AND codigo = '"+codigo+"')")
	    data = [dict((cursor.description[i][0], value)
			for i, value in enumerate(row)) for row in cursor.fetchall()]
	    if data is None:
	    	return "Data not valid"
	    else:
	    	return jsonify({'program' : data})
    if tipo is None:
	    cursor.execute("SELECT * FROM programa WHERE asignatura_idasignatura = (SELECT idasignatura FROM asignatura WHERE nivel = "+nivel+" AND codigo = '"+codigo+"')")
	    data = [dict((cursor.description[i][0], value)
			for i, value in enumerate(row)) for row in cursor.fetchall()]
	    if data is None:
	    	return "Data not valid"
	    else:
	    	return jsonify({'program' : data})
    if codigo is None:
	    cursor.execute("SELECT * FROM programa WHERE asignatura_idasignatura = (SELECT idasignatura FROM asignatura WHERE tipo = '"+tipo+"' AND nivel = "+nivel+")")
	    data = [dict((cursor.description[i][0], value)
			for i, value in enumerate(row)) for row in cursor.fetchall()]
	    if data is None:
	    	return "Data not valid"
	    else:
	    	return jsonify({'program' : data})
    else:
	    cursor.execute("SELECT * FROM programa WHERE asignatura_idasignatura = (SELECT idasignatura FROM asignatura WHERE tipo = '"+tipo+"' AND nivel = "+nivel+" AND codigo = '"+codigo+"')")
	    data = [dict((cursor.description[i][0], value)
			for i, value in enumerate(row)) for row in cursor.fetchall()]
	    if data is None:
	    	return "Data not valid"
	    else:
	    	return jsonify({'program' : data})

#----------------------------------------------#
# Funcion: Busqueda de asignatura por id de asignatura.
#          Retorna los datos de la asignatura.
#
# Entrada: id de la asignatura ("identificadorAsig").
#          Se entrega mediante url.
#
# Salida: Objeto json conteniendo los datos de la asignatura.
#----------------------------------------------#


@app.route("/asignaturaid", methods=['GET'])
def getAsignaturasid():
	asignaturaid = request.args.get('identificadorAsig')
	cursor = mysql.connection.cursor()
	cursor.execute("SELECT * from asignatura WHERE idasignatura = "+asignaturaid+"")
	data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
	return jsonify({'asignatura' : data})

#----------------------------------------------#
# Funcion: Busqueda de plan por id de la carrera.
#
# Entrada: id de la carrera ("id_carrera").
#          Se entrega mediante url.
#
# Salida: Objeto json conteniendo el id del plan y la resolucion del plan.
#----------------------------------------------#


@app.route("/plancarrera", methods=['GET'])
def getPlanCarrera():
	carreraid = request.args.get('id_carrera')
	cursor = mysql.connection.cursor()
	cursor.execute("SELECT idplan_estudio, resolucion FROM plan_estudio WHERE idplan_estudio IN (SELECT idplan_estudio from plan_estudio WHERE carrera_idcarrera ="+carreraid+")")
	data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
	return jsonify({'plan' : data})

#----------------------------------------------#
# Funcion: Busqueda de asignatura por id del plan.
#
# Entrada: id del plan ("id_plan").
#          Se entrega mediante url.
#
# Salida: Objeto json conteniendo el codigo, id y nombre de la asignatura.
#----------------------------------------------#


@app.route("/asignaturaplan", methods=['GET'])
def getAsginaturaPlan():
	planid = request.args.get('id_plan')
	cursor = mysql.connection.cursor()
	cursor.execute("SELECT idasignatura, nombreAsignatura, codigo FROM asignatura WHERE idasignatura IN (SELECT asignatura_idasignatura FROM plan_asignatura WHERE plan_estudio_idplan_estudio="+planid+")")
	data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
	return jsonify({'asignaturas' : data})


#----------------------------------------------#
# Funcion: Busqueda de datos del plan y aisgnatura por id del plan y de la asignatura.
#
# Entrada: id de la asignatura ("id_asignatura").
#          id del plan ("id_plan").
#          Se entrega mediante url.
#
# Salida: Objeto json conteniendo datos de plan y asignatura.
#         Incluye: codigo, TEL, nivel, nombre asignatura, requisitos, resolucion, SCT y tipo.
#----------------------------------------------#


# Busqueda de datos por id PLAN
@app.route("/datosplanasig", methods=['GET'])
def getDatosPlanAsig():
	idplan = request.args.get('id_plan')
	idasignatura = request.args.get('id_asignatura')
	cursor = mysql.connection.cursor()
	cursor.execute("SELECT P.resolucion,P.idplan_estudio, A.idasignatura, A.codigo, A.nombreAsignatura, A.horasT, A.horasE, A.horasL, A.sct, A.tipo, A.requisitos, A.nivel FROM plan_estudio P, asignatura A,plan_asignatura C WHERE C.plan_estudio_idplan_estudio="+idplan+" AND C.asignatura_idasignatura="+idasignatura+" AND P.idplan_estudio = C.plan_estudio_idplan_estudio")
	data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
	cursor.execute("SELECT detalle_programa_iddetalle_programa FROM programa WHERE asignatura_idasignatura="+idasignatura)
	dataDetalle= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
	return jsonify({'datos' : data, 'id_detalle' : dataDetalle})

#----------------------------------------------#
# LOS SERVICIOS DE AUTENTIFICACION DEL SISTEMA #
#----------------------------------------------#

#----------------------------------------------#
# Funcion: Servicio de autentificacion para administrador, en el login.
#
# Entrada: correo del admin ("CorreoA").
#          contraseña del admin ("PasswordA").
#          Se entrega mediante url.
#
# Salida: Objeto json conteniendo los datos del admin.
#----------------------------------------------#


@app.route("/AuthenticateAdmin", methods=['GET'])
def AuthenticateAdmin():	
	admincorreo = request.args.get('CorreoA')
	adminpassword = request.args.get('PasswordA')
	cursor = mysql.connection.cursor()
	cursor.execute("SELECT * FROM admin WHERE correoAdmin='"+admincorreo+"' AND passwordAdmin='"+adminpassword+"'")
	data = cursor.fetchone()
	if data is None:
		return "You are in GBJ!"
	else:
		return jsonify({'admin' : data})


#----------------------------------------------#
# Funcion: Servicio de autentificacion para usuario, en el login.
#
# Entrada: correo del usuario ("CorreoU").
#          contraseña del usuario ("PasswordU").
#          Se entrega mediante url.
#
# Salida: Objeto json conteniendo los datos del usuario.
#----------------------------------------------#


@app.route("/AuthenticateUser", methods=['GET'])
def AuthenticateUser():	
	usercorreo = request.args.get('CorreoU')
	userpassword = request.args.get('PasswordU')
	cursor = mysql.connection.cursor()
	cursor.execute("SELECT * FROM usuario WHERE correousuario='"+usercorreo+"' AND passwordusuario='"+userpassword+"'")
	data = cursor.fetchone()
	if data is None:
		return "You are in GBJ!"
	else:
		return jsonify({'user' : data})


#----------------------------------------------#
# Funcion: Servicio de autentificacion para administrador o usuario, en el login.
#
# Entrada: correo del admin/usuario ("Correo").
#          contraseña del admin/usuario ("Password").
#          Se entrega mediante url.
#
# Salida: Objeto json conteniendo los datos del admin o usuario.
#----------------------------------------------#


@app.route("/Authenticate", methods=['GET'])
def Authenticate():	
	correo = request.args.get('Correo')
	password = request.args.get('Password')
	if correo is None or password is None:
		return "FALTA AGREGAR CORREO O CONTRASEÑA!"
	cursor = mysql.connection.cursor()
	cursor.execute("SELECT * FROM usuario WHERE correousuario='"+correo+"' AND passwordusuario='"+password+"'")
	dataU = cursor.fetchone()
	if dataU is None:
		cursor.execute("SELECT * FROM admin WHERE correoAdmin='"+correo+"' AND passwordAdmin='"+password+"'")
		dataA = cursor.fetchone()
		if dataA is None:
			return "NO EXISTE ADMIN/USER"
		else:
			return jsonify({'admin' : dataA, 'Type' : 'Admin'})
		
	else:
		return jsonify({'user' : dataU,'Type' : 'User'})


#----------------------------------------------#
# LOS SERVICIOS DE UPDATE DEL SISTEMA #
#----------------------------------------------#


#----------------------------------------------#
# Funcion: Actualiza el detalle de un programa en especifico.
#
# Entrada: id del detalle ("iddetalle").
#          descripAsign del detalle ("descripAsign")
#          objPE del detalle ("objPE")
#          objAsign del detalle ("objAsign")
#          estratMeto del detalle ("estratMeto")
#          infoAd del detalle ("infoAd")
#          fuenteInfo del detalle ("fuenteInfo")
#          Se entrega mediante url.
#
# Salida: Retorna mensaje de exito de realizarse exitosamente el update.
#----------------------------------------------#


@app.route("/updateProgram", methods=['POST'])
def updateProgram():
	if request.method == 'POST':
		detalleid = request.json['iddetalle']
		descripAsign = request.json['descripAsign']
		objPE = request.json['objPE']
		objAsign = request.json['objAsign']
		estratMeto = request.json['estratMeto']
		infoAd = request.json['infoAd']
		fuenteInfo = request.json['fuenteInfo']


		cursor = mysql.connection.cursor()
		cursor.execute("Update detalle_programa SET descripAsign = "+descripAsign+", objetivoPerfilEgreso = "+objPE+", objetivoAsign = "+objAsign+", estratMeto = "+estratMeto+", infoAd = "+infoAd+", fuenteInfo = "+fuenteInfo+" WHERE iddetalle_programa = "+detalleid+"")
		mysql.connection.commit()
		return "LOCKED AND LOADED"
	else:
		return "But nothing happens..."

#----------------------------------------------#
# LOS SERVICIOS DELETE DEL SISTEMA             #
#----------------------------------------------#


#----------------------------------------------#
# Funcion: Borra una unidad del sistema, junto con sus subunidades.
#
# Entrada: id de la unidad ("idUnidad")
#          Se entrega mediante url.
#
# Salida: Retorna mensaje de exito de realizarse exitosamente el delete.
#----------------------------------------------#


@app.route("/deleteUnidad", methods=['POST'])
def deleteUnidad():
	if request.method == 'POST':
		idUnidad = request.json['idUnidad']

		cursor = mysql.connection.cursor()

		cursor.execute("DELETE FROM unidad_tematica WHERE unidades_idunidades = %s",idUnidad)
		mysql.connection.commit()
		cursor.execute("DELETE FROM unidades WHERE idunidades = %s",idUnidad)
		mysql.connection.commit()
		return "LOCKED AND LOADED"
	else:
		return "But nothing happens..."



#----------------------------------------------#
# LOS SERVICIOS DE INSERT DEL SISTEMA          #
#----------------------------------------------#


#----------------------------------------------#
# Funcion: Inserta una relacion entre usuario y un programa, junto con el nivel de permiso.
#
# Entrada: nivel del permiso ("nivelpermiso").
#          id del usuario ("idus")
#          id del programa ("idpro")
#          Se entrega mediante url.
#
# Salida: Retorna mensaje de exito de realizarse exitosamente el update.
#----------------------------------------------#



@app.route("/programausuario", methods=['POST'])
def newProgramaUsuario():
	if request.method == 'POST':
		nivelpermiso = request.json['nivelpermiso']
		idusuario = request.json['idus']
		idprograma = request.json['idpro']

		cursor = mysql.connection.cursor()

		cursor.execute("SELECT MAX(idusuario_programa) FROM usuario_programa")
		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(idusuario_programa)')
		print(maxID)

		cursor.execute("INSERT INTO usuario_programa (idusuario_programa,nivelpermiso,usuario_idusuario,programa_idprograma) VALUES (%s,%s,%s,%s)",((maxID)+1,nivelpermiso,idusuario,idprograma))
		mysql.connection.commit()
		return "LOCKED AND LOADED"

	else:
		return "But nothing happens..."



#----------------------------------------------#
# Funcion: Inserta un usuario nuevo en el sistema.
#
# Entrada:
#          nombre del usuario ("nameusuario")
#          cargo del usuario ("cargousuario")
#          departamento del usuario ("deptousuario")
#          correo del usuario ("correousuario")
#          contraseña del usuario ("passwordusuario")
#          Se entrega mediante url.
#
# Salida: Retorna mensaje de exito de realizarse exitosamente el update.
#----------------------------------------------#


@app.route("/newUsuario", methods=['POST'])
def newUsuario():
	if request.method == 'POST':
		usuarioid = request.json['idusuario']
		usuarioname = request.json['nameusuario']
		usuariocargo = request.json['cargousuario']
		usuariodepto = request.json['deptousuario']
		usuariocorreo = request.json['correousuario']
		usuariopassword = request.json['passwordusuario']
		cursor = mysql.connection.cursor()

		cursor.execute("SELECT MAX(idusuario) FROM usuario")

		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(idusuario)')
		print(maxID)


		cursor.execute("INSERT INTO usuario (idusuario,nameusuario,cargousuario,deptousuario,correousuario,passwordusuario) VALUES (%s,%s,%s,%s,%s,%s)",((maxID)+1,usuarioname,usuariocargo,usuariodepto,usuariocorreo,usuariopassword))
		mysql.connection.commit()
		return "LOCKED AND LOADED"

	else:
		return "But nothing happens..."


#----------------------------------------------#
# Funcion: Inserta un plan nuevo en el sistema.
#
# Entrada: id del admin que desarrolla el plan ("idadmin").
#          resoluacion del plan ("resolu")
#          dia de la fecha del plan ("fechadia")
#          mes de la fecha del plan ("fechames")
#          año de la fecha del plan ("fechaano")
#          id de la carrera a la que pertenece el plan ("idcarrera")
#          Se entrega mediante url.
#
# Salida: Retorna mensaje de exito de realizarse exitosamente el update.
#----------------------------------------------#

@app.route("/newPlan", methods=['POST'])
def newPlan():
	if request.method == 'POST':
		planid = request.json['idplan']
		adminid = request.json['idadmin']
		resolu = request.json['resolu']
		fech_dia = request.json['fechadia']
		fech_mes = request.json['fechames']
		fech_ano = request.json['fechaano']
		carreraid = request.json['idcarrera']
		cursor = mysql.connection.cursor()

		cursor.execute("SELECT MAX(idplan_estudio) FROM plan_estudio")
		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(idplan_estudio)')
		print(maxID)

		cursor.execute("INSERT INTO plan_estudio (idplan_estudio,admin_idadmin,resolucion,fecha_resol_dia,fecha_resol_mes,fecha_resol_año,carrera_idcarrera) VALUES (%s,%s,%s,%s,%s,%s,%s)",((maxID)+1,adminid,resol,fech_dia,fech_mes,fech_ano,carreraid))
		mysql.connection.commit()
		return "LOCKED AND LOADED"

	else:
		return "But nothing happens..."

#----------------------------------------------#
# Funcion: Inserta una carrera nueva en el sistema.
#
# Entrada: nombre de la carrera ("nombrecarrera").
#          id del departamento de la carrera ("iddepto")
#          Se entrega mediante url.
#
# Salida: Retorna mensaje de exito de realizarse exitosamente el update.
#----------------------------------------------#


@app.route("/newCarrera", methods=['POST'])
def newCarrera():
	if request.method == 'POST':
		carreraid = request.json['idcarrera']
		carreranombre = request.json['nombrecarrera']
		carreraiddepto = request.json['iddepto']
		cursor = mysql.connection.cursor()

		cursor.execute("SELECT MAX(idcarrera) FROM carrera")
		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(idcarrera)')
		print(maxID)
		cursor.execute("INSERT INTO carrera (idcarrera,nombrecarrera,departamento_iddepartamento) VALUES (%s,%s,%s)",((maxID)+1,carreranombre,carreraiddepto))
		mysql.connection.commit()
		return "LOCKED AND LOADED"

	else:
		return "But nothing happens..."


#----------------------------------------------#
# Funcion: Inserta un detalle de programa nuevo en el sistema.
#
# Entrada: nombre de la carrera ("carrera").
#          nombre de la asignatura ("asignatura")
#          codigo de la asignatura del programa ("codigo")
#          numero de creditos del sistema de creditos transferible ("sct")
#          nombre del departamento ("depto")
#          año-semestre-nivel ("a_s_n")
#          categoria del programa ("categoria")
#          numero de horas presenciales ("horasPre")
#          perfil del profesor ("perfilProfe")
#          version del programa ("version")
#          resolucion de la facultad ("resolFacu")
#          autor del prgorama ("autor")
#          descripcion de la asignatura ("descripAsign")
#          objetivos perfil de egreso  ("objPE")
#          objetivos de la asignatura ("objAsign")
#          estrategias metodologicas ("estratMeto")
#          informacion adicional ("infoAd")
#          fuentes de informacion ("fuenteInfo")
#          Se entrega mediante url.
#
# Salida: Retorna mensaje de exito de realizarse exitosamente el update.
#----------------------------------------------#


@app.route("/newDetalle", methods=['POST'])
def newDetalle():
	if request.method == 'POST':
		detalleid = request.json['iddetalle']
		carrera = request.json['carrera']
		asignatura = request.json['asignatura']
		codigo = request.json['codigo']
		sct = request.json['sct']
		depto = request.json['depto']
		a_s_n = request.json['a_s_n']
		categoria = request.json['categoria']
		horasPre = request.json['horasPre']
		perfilProfe = request.json['perfilProfe']
		version = request.json['version']
		resolFacu = request.json['resolFacu']
		autor = request.json['autor']
		descripAsign = request.json['descripAsign']
		objPE = request.json['objPE']
		objAsign = request.json['objAsign']
		estratMeto = request.json['estratMeto']
		infoAd = request.json['infoAd']
		fuenteInfo = request.json['fuenteInfo']

		cursor = mysql.connection.cursor()

		cursor.execute("SELECT MAX(iddetalle_programa) FROM detalle_programa")
		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(iddetalle_programa)')
		print(maxID)

		cursor.execute("INSERT INTO detalle_programa (iddetalle_programa,carrera,asignatura,codigo,sct,departamento,año_semestre_nivel,categoria,horasPre,perfilProfe,version,resolFacu,autor,descripAsign,objetivoPerfilEgreso,objetivoAsign,estratMeto,infoAd,fuenteInfo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",((maxID)+1,carrera,asignatura,codigo,sct,depto,a_s_n,categoria,horasPre,perfilProfe,version,resolFacu,autor,descripAsign,objPE,objAsign,estratMeto,infoAd,fuenteInfo))
		mysql.connection.commit()
		return "LOCKED AND LOADED"

	else:
		return "But nothing happens..."

#----------------------------------------------#
# Funcion: Inserta una unidad nueva, perteneciente a un detalle de programa existente.
#
# Entrada: numero de la unidad ("numerounidad")
#          titulo de la unidad ("titulounidad")
#          horas presenciales de la unidad ("horasPunidad")
#          capacidades a desarrollar en la unidad ("capDes")
#          topicos evaluados en la unidad ("topicosEva")
#          id del detalle al que pertenece ("detalle_programa_iddetalle_programa")
#          Se entrega mediante url.
#
# Salida: Retorna mensaje de exito de realizarse exitosamente el update.
#----------------------------------------------#

		
@app.route("/newUnidad", methods=['POST'])
def newUnidad():
	if request.method == 'POST':
		unidadid = request.json['idunidad']
		numero = request.json['numerounidad']
		titulo = request.json['titulounidad']
		horasP = request.json['horasPunidad']
		capaDes = request.json['capDes']
		topicosEva = request.json['topicosEva']
		unidadiddetalle = request.json['detalle_programa_iddetalle_programa']

		cursor = mysql.connection.cursor()
		cursor.execute("SELECT MAX(idunidades) FROM unidades")
		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(idunidades)')
		print(maxID)

		cursor.execute("INSERT INTO unidades (idunidades,numeroUnidad,tituloUnidad,horasPeda,capaDesarrolla,topicosEvalua,detalle_programa_iddetalle_programa) VALUES (%s,%s,%s,%s,%s,%s,%s)",((maxID)+1,numero,titulo,horasP,capaDes,topicosEva,unidadiddetalle))
		mysql.connection.commit()
		return "LOCKED AND LOADED"
	else:
		return "But nothing happens..."


#----------------------------------------------#
# Funcion: Inserta una subunidad nueva, perteneciente a una unidad existente.
#
# Entrada: primer contenido de la tabla contenidos ("contUno")
#          segundo contenido de la tabla contenidos ("contDos")
#          horas presenciales de la subunidad ("horasPres")
#          id de la unidad a la que pertenece ("unidades_idunidades")
#          Se entrega mediante url.
#
# Salida: Retorna mensaje de exito de realizarse exitosamente el update.
#----------------------------------------------#


@app.route("/newUnidadTem", methods=['POST'])
def newUnidadTem():
	if request.method == 'POST':
		unidadTemid = request.json['idunidadtem']
		cont_1 = request.json['contUno']
		cont_2 = request.json['contDos']
		horasPres = request.json['horasPres']
		unidadTemidunidad = request.json['unidades_idunidades']

		cursor = mysql.connection.cursor()
		cursor.execute("SELECT MAX(idunidad_tematica) FROM unidad_tematica")
		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(idunidad_tematica)')
		print(maxID)

		cursor.execute("INSERT INTO unidad_tematica (idunidades,contenidos1,contenidos2,horasPresen,unidades_idunidades) VALUES (%s,%s,%s,%s,%s)",((maxID)+1,cont_1,cont_2,horasPres,unidadTemidunidad))
		mysql.connection.commit()
		return "LOCKED AND LOADED"
	else:
		return "But nothing happens..."

#----------------------------------------------#
# Funcion: Inserta una evaluacion nueva, perteneciente a un detalle de programa existente.
#
# Entrada: evento a evaluar ("evaEvento")
#          contenido/objetivo/resultado a evaluar ("contObjResult")
#          ponderacion de la evaluacion ("ponderacion")
#          semana de la evaluacion ("semana")
#          id del detalle al que pertenece ("detalle_programa_iddetalle_programa")
#          Se entrega mediante url.
#
# Salida: Retorna mensaje de exito de realizarse exitosamente el update.
#----------------------------------------------#


@app.route("/newEvaluacion", methods=['POST'])
def newEvaluacion():
	if request.method == 'POST':
		evaluacionid = request.json['idevaluacion']
		eventoEva = request.json['evaEvento']
		contObjResult = request.json['contObjResult']
		ponderacion = request.json['ponderacion']
		semana = request.json['semana']
		evaluacioniddetalle = request.json['detalle_programa_iddetalle_programa']

		cursor = mysql.connection.cursor()
		cursor.execute("SELECT MAX(idevaluacion) FROM evaluacion")
		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(idevaluacion)')
		print(maxID)

		cursor.execute("INSERT INTO evaluacion (idevaluacion,eventoEva,contObjeResult,ponderacion,semana,detalle_programa_iddetalle_programa) VALUES (%s,%s,%s,%s,%s,%s)",((maxID)+1,eventoEva,contObjResult,ponderacion,semana,evaluacioniddetalle))
		mysql.connection.commit()
		return "LOCKED AND LOADED"
	else:
		return "But nothing happens..."

#----------------------------------------------#
# Funcion: Inserta un programa nuevo.
#
# Entrada: nombre del programa ("nameprograma")
#          departamento al que pertenece el programa ("deptoprograma")
#          fecha de creacion del programa ("fechacreacion")
#          fecha de la ultima modificacion del programa ("fechaultmod")
#          estado del programa ("estadoprograma")
#          id del detalle del programa ("detalle_programa_iddetalle_programa")
#          id de la asignatura a la que pertenece ("asignatura_idasignatura")
#          Se entrega mediante url.
#
# Salida: Retorna mensaje de exito de realizarse exitosamente el update.
#----------------------------------------------#


@app.route("/newPrograma", methods=['POST'])
def newPrograma():
	if request.method == 'POST':
		programaid = request.json['idprograma']
		programaname = request.json['nameprograma']
		programadepto = request.json['deptoprograma']
		programafechcrea = request.json['fechacreacion']
		programafechult = request.json['fechaultmod']
		programaestado = request.json['estadoprograma']
		programaiddetalle = request.json['detalle_programa_iddetalle_programa']
		programaidasignatura = request.json['asignatura_idasignatura']
		
		cursor = mysql.connection.cursor()
		cursor.execute("SELECT MAX(idprograma) FROM programa")
		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(idprograma)')
		print(maxID)

		cursor.execute("INSERT INTO programa (idprograma,nameprograma,deptoprograma,fechacreacion,fechaultmod,estadoprograma,detalle_programa_iddetalle_programa,asignatura_idasignatura) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",((maxID)+1,programaname,programadepto,programafechcrea,programafechult,programaestado,programaiddetalle,programaidasignatura))
		mysql.connection.commit()
		return "LOCKED AND LOADED"

	else:
		return "But nothing happens..."


#----------------------------------------------#
# Funcion: Inserta una asignatura nueva.
#
# Entrada: codigo de la asignatura ("codigoasignatura")
#          nombre de la asignatura ("nombreasignatura")
#          horas de teoria ("horasT")
#          horas de ejercicio ("horasE")
#          horas de laboratorio ("horasL")
#          creditos transferibles ("sct")
#          tipo de la asignatura ("tipo")
#          requisitos de la asignatura ("requisitos")
#          nivel de la asignatura ("nivel")
#          Se entrega mediante url.
#
# Salida: Retorna mensaje de exito de realizarse exitosamente el update.
#----------------------------------------------#


@app.route("/newAsignatura", methods=['POST'])
def newAsignatura():
	if request.method == 'POST':
		asignaturaid = request.json['idasignatura']
		asignaturacodigo = request.json['codigoasignatura']
		asignaturanombre = request.json['nombreasignatura']
		horasT = request.json['horasT']
		horasE = request.json['horasE']
		horasL = request.json['horasL']
		sct = request.json['sct']
		tipo = request.json['tipo']
		requisitos = request.json['requisitos']
		nivel = request.json['nivel']
		cursor = mysql.connection.cursor()
		cursor.execute("SELECT MAX(idasignatura) FROM asignatura")
		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(idasignatura)')
		print(maxID)

		cursor.execute("INSERT INTO asignatura (idasignatura,codigo,nombreAsignatura,horasT,horasE,horasL,sct,tipo,requisitos,nivel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",((maxID)+1,asignaturacodigo,asignaturanombre,horasT,horasE,horasL,sct,tipo,requisitos,nivel))
		mysql.connection.commit()
		return "LOCKED AND LOADED"

	else:
		return "But nothing happens..."

#-------------------------------------------------#
# LOS SERVICIOS DE INSERT INTERMEDIOS DEL SISTEMA #
#-------------------------------------------------#


#----------------------------------------------#
# Funcion: Inserta una relacion nueva entre plan y asignatura.
#
# Entrada: id del plan ("idplan")
#          id de la asignatura ("idasig")
#          Se entrega mediante url.
#
# Salida: Retorna mensaje de exito de realizarse exitosamente el update.
#----------------------------------------------#



@app.route("/newPlanAsig", methods=['POST'])
def newPlanAsig():
	if request.method == 'POST':
		planasigid = request.json['idplanasig']
		planid = request.json['idplan']
		asigid = request.json['idasig']

		cursor = mysql.connection.cursor()
		cursor.execute("SELECT MAX(idplan_asignatura) FROM plan_asignatura")
		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(idplan_asignatura)')
		print(maxID)

		cursor.execute("INSERT INTO plan_asignatura (asignatura_idasignatura,plan_estudio_idplan_estudio,idplan_asignatura) VALUES (%s,%s,%s)",(asigid,planid,(maxID)+1))
		mysql.connection.commit()
		return "LOCKED AND LOADED"
	else:
		return "But nothing happens..."

#----------------------------------------------#
# Funcion: Inserta una relacion nueva entre usuario y programa.
#
# Entrada: id del usuario ("iduser")
#          id del programa ("idprogram")
#          nivel de permiso ("nivelPermiso")
#          Se entrega mediante url.
#
# Salida: Retorna mensaje de exito de realizarse exitosamente el update.
#----------------------------------------------#


@app.route("/newUsuarioProgram", methods=['POST'])
def newUserProgram():
	if request.method == 'POST':
		userprogramid = request.json['iduserprogram']
		nivelPermiso = request.json['nivelPermiso']
		userid = request.json['iduser']
		programid = request.json['idprogram']

		cursor = mysql.connection.cursor()
		cursor.execute("SELECT MAX(idusuario_programa) FROM usuario_programa")
		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(idusuario_programa)')
		print(maxID)

		cursor.execute("INSERT INTO usuario_programa (idusuario_programa,nivelpermiso,usuario_idusuario,programa_idprograma) VALUES (%s,%s,%s)",((maxID)+1,nivelPermiso,userid,programid))
		mysql.connection.commit()
		return "LOCKED AND LOADED"
	else:
		return "But nothing happens..."



if __name__ == "__main__":
	app.run()

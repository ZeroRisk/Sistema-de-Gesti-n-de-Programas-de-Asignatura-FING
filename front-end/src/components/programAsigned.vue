<template>
  <div class="main_file">
    <!-- botones que invocan las funciones del componente
    -->
    <table class="tabla" >
    <button class="botones" v-on:click="saveData">Guardar</button>
    <button class="botones" v-on:click="genPDF">Descargar</button>
    <button class="botones">Atras</button>
    
    <div class="all" >
    <!-- 
      Datos del programa que no se pueden modificar
    --> 
    <div class="test" ref="test">
    <h4>1. PROGRAMA DE LA ASIGNATURA </h4>
    <table class="bloque1">
    <table class="tabla1">
    <td align="left">Resolución</td>
    <td  align="left" class="texto_input" ref="resolucion"> </td>
    
    <tr>
      <td>Carrera :</td>
      <td colspan="7" id="carreraNombre" class="texto_input" ref="carrera"> </td>
    </tr>
    <tr>
      <td>ASIGNATURA :</td>
      <td colspan="7"  class="texto_input" ref="asignatura"> </td>
    </tr>
    <tr>
      <td>CÓDIGO :</td>
      <td  class="texto_input" width="50" height="16" ref="codigo"> </td>
      <td >T: </td>
      <td  class="texto_input" width="50" height="16" ref="T"> </td>
      <td>E: </td>
      <td  class="texto_input" width="50" height="16" ref="E"> </td>
      <td>L: </td>
      <td class="texto_input" width="50" height="16" ref="L"> </td>
    </tr>
    <tr>
      <td>REQUISITOS: </td>
      <td colspan="7" class="texto_input" ref="requisitos"> </td>
    </tr>
    <tr>
      <th align="left">DICTA DEPARTAMENTO: </th>
      <td colspan="7"  class="texto_input" ref="dicta_departamento">Departamento Mecánica</td>
    </tr>
    <tr>
      <th align="left">AÑO - SEMESTRE - NIVEL: </th>
      <td  colspan="7" contenteditable="true" class="texto_input" ref="annio_semestre_nivel"></td>
    </tr>
    <tr>
      <th align="left">Tipo: </th>
      <td colspan="7"  class="texto_input" ref="categoria"> </td>
    </tr>
    <tr>
      <th align="left" >HORAS PRESENCIALES A LA SEMANA: </th>
      <td colspan="7" contenteditable="true" class="texto_input" ref="horas_presenciales_a_la_semana"></td>
    </tr>
    <tr>
      <th align="left">PERFIL PROFESOR:</th>
      <td colspan="7" contenteditable="true" class="texto_input" ref="perfil_profesor"></td>
    </tr>
    <tr>
    <td align="right">SCT</td>
      <td  class="texto_input" ref="SCT"> </td>
      <td align="left">Versión</td>
      <td contenteditable="true" class="texto_input" ref="version"></td>
      
      
    </tr>
    
    
    </table>
    </table>
    <!-- 
      Descripcion y objetivos de la asignatura
    -->
    <h4>2. DESCRIPCION DE LA ASIGNATURA </h4>
    <textarea ref="descripcion_de_la_asignatura" />
    <h4>3. OBJETIVOS DE APRENDIZAJE </h4>
    <h5>3.1 ASOCIADOS A PERFIL DE EGRESO</h5>
    <div id="listaAgregar">
    <input id="OAPE1" type="text" ref="asociados_a_perfil_de_egreso" style="width:400px;"/>
    <button class="botones2" v-on:click="agregar(1)" id="NO1">+</button>
    <button  class="botones2" v-on:click="quitar(1)" id="NO">- </button>
    </div>
    <h5>3.2 ASOCIADOS A LA ASIGNATURA</h5>
    <h5>Objetivos Generales</h5>
    <div id="listaAgregarOG">
    <input type="text" id="OG1" ref="objetivos_generales"  style="width:400px;"/>
    <button  class="botones2" v-on:click="agregar(2)"  id="NO1">+</button>
    <button  class="botones2" v-on:click="quitar(2)" id="NO">- </button>
    </div>
    
    </div>
    <div class="componente2" ref="test2">
    <h5>Objetivos específicos</h5>
    <div id="listaAgregarOE">
      <input type="text" id="OE1" ref="objetivos_especificos"  style="width:400px;"/>
      <button  class="botones2" v-on:click="agregar(3)"  id="NO">+</button>
      <button  class="botones2"  v-on:click="quitar(3)" id="NO">-</button>
    </div>
    <!-- 
      Contenido de UNIDADES y sub unidades
    -->
      <h4>4. UNIDADES CONTENIDO </h4>
       <div id="unidades">
      </div>
      <input type="button" class="botones2" id="boton" value="+ Agregar Unidad" v-on:click="agregarUnidades" />
      <input type="button" class="botones2" id="botonElim" value="- Eliminar Unidad" v-on:click="eliminarUnidades" />
     
      <br/>
      
    
    </div>
    <div class= "pagina3"> 
   <!-- 
      Estrategias metodologicas , informacion adicional y fuentes de informacion de la asignatura  
    -->
      <h4>6. ESTRATEGIAS METODOLÓGICAS</h4>
      <textarea ref="estrategias_metodologicas" rows="8" cols="80"></textarea>
      <h4>7. INFORMACIÓN ADICIONAL</h4>
        <textarea ref="informacion_adicional" rows="8" cols="80"></textarea>
       <h4>8. FUENTE DE INFORMACIÓN</h4>
         <textarea ref="fuente_de_informacion" rows="8" cols="80"></textarea>
    </div>
   
<br>    
<button class="botones" v-on:click="saveData">Guardar</button>
<button class="botones">Asignar</button>
<button class="botones">Atras</button>

    </div> 
    </table>
<!-- 
    Menu lateral    
  -->
<div id='cssmenu' >
<ul>
  <li> 
     <router-link :to="{ name: 'Home', params: { user: user , type: type }}"> 
      <a><span>Home</span></a> 
      </router-link> 
  </li> 
  <li class='active has-sub'> 
     <router-link :to="{ name: 'verPrograma', params: { user: user , type: type }}"> 
     <a><span>ver programa asignados</span></a> 
     </router-link> 
  </li> 
  <li> 
     <router-link :to="{ name: 'BuscarPorFecha', params: { user: user , type: type }}"> 
     <a><span>Buscar por Fecha/Asignatura</span></a> 
     </router-link> 
  </li> 

</ul>

</div>
<!-- 
      encabezado pagina 
    -->
<div class="content-box-top">Bienvenido al portal.<a href="#"><span class="cerrar">Cerrar sesión</span></a></div>
<div class="content-box-left"><img src="../assets/usach.png" height="100" width="200"></div>


</div>

  
</template>

<script>
//Componente similar a programManage , difiere en algunas funciones
import html2canvas from 'html2canvas'
// Variables globales
var globalBoton = 0;
var cantUnid = 0;
var cantSU= [];
/** Funcion que agrega a la pagina una formulario donde añadir datos de una nueva sub-unidad 

 */
function agregarSU(num) {
    //alert('Agregar SU'+ num);
    console.log("principio SU"+ cantSU);
    var auxCantSU = cantSU[(Number(num)-1)][1];
    var nuevaCantSU = Number(auxCantSU)+1;
    //cantSU[(Number(num)-1)].splice(1,0,'pepe');
    cantSU[(Number(num)-1)][1]=nuevaCantSU;
    console.log("SU antes "+auxCantSU+" y "+cantSU);
    var div = document.getElementById("divSU"+num);
    var tituloCont = document.createElement("H5");
    var titulo = document.createTextNode("UNIDAD TEMATICA "+nuevaCantSU);
    tituloCont.appendChild(titulo);
    var tabla = document.createElement("table")
    var titulo1 = document.createElement("P");
    var titulo2 = document.createElement("P");
    var titulo3 = document.createElement("P");
    var textoCelda1 = document.createTextNode("Unidad Tema ");
    var textoCelda2 = document.createTextNode("Contenidos ");
    var textoCelda3 = document.createTextNode("Horas presenciales");
    titulo1.appendChild(textoCelda1);
    titulo2.appendChild(textoCelda2);
    titulo3.appendChild(textoCelda3);
    var textoSUB = document.createTextNode(num+"."+nuevaCantSU);
    //input1.setAttribute("id", num+"."+nuevaCantSU);
    var textArea2 = document.createElement("textarea");
    textArea2.setAttribute("id","SU_"+num+"."+nuevaCantSU);
    textArea2.setAttribute("rows","8");
    textArea2.setAttribute("cols","80");
    var input2 = document.createElement("input");
    input2.setAttribute("id", "n_horas_unidad_SU_"+num+"."+nuevaCantSU);
    input2.setAttribute("type", "text");
    input2.setAttribute("style","width:40px;");
    div.appendChild(tituloCont);
    div.appendChild(titulo1);
    div.appendChild(textoSUB);
    div.appendChild(titulo2);
    div.appendChild(textArea2);
    div.appendChild(titulo3);
    div.appendChild(input2);
   
}
/*
  Funcion que se encarga de obtener la informacion de la subunidad
  Estos datos son el numero de la subunidad, tamaño y su id
*/
function obtenerInfo(numUnidad){
    alert('info SU'+ numUnidad);
    var div = document.getElementById("divSU"+numUnidad);
    var children = document.getElementById("divSU"+numUnidad).children;
    var tamano = children.length;
    console.log("este es el tamano :"+tamano);
    var ultimoID = children[tamano-1].className;
    console.log("este es el hijito "+ultimoID);

}
//Funcion que elimina de la pagina el formulario donde se elimina una SU 
function eliminarSU(numUnidad){
    
    var div = document.getElementById("divSU"+numUnidad);
    var tamano = div.children.length;
    var auxCantSU = cantSU[(Number(numUnidad)-1)][1];
    if(Number(auxCantSU)>0){
        var nuevaCantSU = Number(auxCantSU)-1;
        
        cantSU[(Number(numUnidad)-1)][1]=nuevaCantSU;
        console.log("final al eliminar "+nuevaCantSU);
    }
    
    if (Number(tamano)>0){
        console.log("tamanoo  "+tamano);
        div.removeChild(div.lastChild);
        div.removeChild(div.lastChild);
        div.removeChild(div.lastChild);
        div.removeChild(div.lastChild);
        div.removeChild(div.lastChild);
        div.removeChild(div.lastChild);
        div.removeChild(div.lastChild);
    }
   
}
export default {
  props: ['user','type', 'Programa'],
  // Funcion que se encarga de obtener los datos de los campos de la pagina para completar
  // Para su posterior guardado a la base de datos por un servicio rest
  mounted: function (){ 
      console.log(this.Programa.carrera)
      this.$refs.carrera.textContent = this.Programa.carrera
      this.$refs.asignatura.textContent = this.Programa.asignatura
      this.$refs.codigo.textContent = this.Programa.codigo
      this.$refs.T.textContent = this.Programa.horasT
      this.$refs.E.textContent = this.Programa.horasE
      this.$refs.L.textContent = this.Programa.horasL
      this.$refs.requisitos.textContent = this.Programa.requisitos
      this.$refs.dicta_departamento.textContent = this.Programa.deptoprograma
      this.$refs.annio_semestre_nivel.textContent = this.Programa.año_semestre_nivel
      this.$refs.categoria.textContent = this.Programa.categoria
      this.$refs.horas_presenciales_a_la_semana.textContent = this.Programa.horasPre
      this.$refs.perfil_profesor.textContent = this.Programa.perfilProfe
      this.$refs.version.textContent = this.Programa.version
      this.$refs.resolucion.textContent = this.Programa.resolFacu
      this.$refs.descripcion_de_la_asignatura.value = this.Programa.resolFacu
      this.$refs.estrategias_metodologicas.value = this.Programa.estratMeto
      this.$refs.informacion_adicional.value = this.Programa.infoAd
      this.$refs.fuente_de_informacion.value = this.Programa.fuenteInfo
  }, 
  data () {
    
    return {
      msg: 'Welcome to Your Vue.js App',
      carrera: "",
      asignatura: "",
      codigo:"",
      HT:"",
      HE:"",
      HL:"",
      requisitos:"",
      dictaDepartamento:"",
      fechaDictado:"",
      categoria:"",
      hrspresenciales:"",
      perfil_profesor:"",
      version:"",
      resolucionFacultad:"",
      sistemaCreditoTransferible:4,
      Autor:"subdirector",
      desAsignatura:"",
      ObjPegreso:"",
      ObjAsignatura:"",
      nombrePrograma:"",
      fechaCreacion:"",
      fechaUltimaModificacion:"",
      cantidad:3,
      estadoprograma:"incompleto",
      Unidades:[],
      cantidadSu:1,
      Datos:[]
   }
  },
  methods: {
   //Debe cambiarse por servicios rest UPDATES
   //Funcion que realiza a traves de un metodo post, la informacion nueva 
    //del programa
    postPrograma: function(){
      this.$http.post('http://localhost:5000/newDetalle',{
        iddetalle: this.cantidad,
        carrera: this.carrera,
        asignatura: this.asignatura,
        codigo: this.codigo,
        sct: this.sistemaCreditoTransferible,
        depto: this.dictaDepartamento,
        a_s_n: this.fechaDictado,
        categoria: this.categoria,
        horasPre: this.hrspresenciales,
        perfilProfe: this.perfil_profesor,
        version: this.version,
        resolFacu: this.resolucionFacultad,
        autor: this.Autor,
        descripAsign: this.desAsignatura,
        objPE: this.ObjPegreso,
        objAsign: this.ObjAsignatura,
        estratMeto:this.estMeto,
        infoAd: this.infoAdicional,
        fuenteInfo: this.fInfo
        
      }).then(response=>{
        console.log("conexion realizada, ahora siguiente fase")
        
        this.$http.post('http://localhost:5000/newPrograma',{
        idprograma: this.cantidad,
        nameprograma: this.nombrePrograma,
        deptoprograma: this.dictaDepartamento,
        fechacreacion: this.fechaCreacion,
        fechaultmod: this.fechaUltimaModificacion,
        estadoprograma: this.estadoprograma,
        detalle_programa_iddetalle_programa: this.cantidad,
        asignatura_idasignatura: 1
        }).then(response=>{
          console.log("se realizo la transaccion programa")
          var i;
          for(i=0;i<this.Unidades.length;i++){
            this.postUnidad(this.Unidades[i])
          }
          this.cantidad++
          alert("se guardo la informacion del programa exitosamente")
        }, response=>{
          console.log("no se pudo")
          alert("hubo un error al guardado de datos, checkee su conexion")
        });
        
      }, response=>{
        console.log("no se agrego detalle")
      });
      
    },
    //Debe cambiarse por servicios rest UPDATES
    //Funcion que realiza a traves de un metodo post, la informacion nueva 
    //de la unidad
    postUnidad: function(unidad){
       this.$http.post('http://localhost:5000/newUnidad',{
         idunidad: unidad[0],
         numerounidad: unidad[0],
         titulounidad: unidad[1],
         horasPunidad: unidad[2],
         capDes: unidad[3],
         topicosEva: unidad[4],
         detalle_programa_iddetalle_programa: this.cantidad
       }).then(response =>{
         console.log("ingreso unidad")
         var i=0;
         while(i<unidad[6].length){
           this.postSubUnidad(unidad[6],unidad[0],i) 
           i=i+3
         }
       }, response =>{
         console.log("falle en enviar el post unidad")
       })
    },
    //Debe cambiarse por servicios rest UPDATES
    //Funcion que realiza a traves de un metodo post, la informacion nueva 
    //de la subunidad
    postSubUnidad: function(SubUnidad,numeroUnidad,n){
    
      var cont1= ("subunidad numero " + SubUnidad[n])
      this.$http.post('http://localhost:5000/newUnidadTem',{
        contUno: cont1 ,
        contDos: SubUnidad[n+1],
        horasPres: parseInt(SubUnidad[n+2]),
        unidades_idunidades: numeroUnidad
      }).then(response =>{
        console.log("ingreso subUnidad ")
      }, response =>{
        console.log("falle en enviar subunidad")
      })
    },
    //Funcion que se encarga de generar un pdf utilizando la libreria jsPDF
    genPDF: function(event){
      console.log("elemento :", this.$refs.test)
      html2canvas(this.$refs.test).then(canvas =>{
          var doc = new jsPDF()
         
          var img = canvas.toDataURL("image/png",1)
          doc.addImage(img,'PNG',5,10)
          doc.save('test.pdf')
          
        })
      },
    /*//  
      Funcion que guarda los datos ingresados en los campos de la pagina, para
      posteriormente enviarlos a la base de datos mediante servicios rest
    //*/
    saveData: function(event){
      console.log( this.$refs.descripcion_de_la_asignatura) 
      this.carrera = this.$refs.carrera.textContent
      this.asignatura= this.$refs.asignatura.textContent
      this.codigo = this.$refs.codigo.textContent
      this.HT = this.$refs.T.textContent
      this.HE = this.$refs.E.textContent
      this.HL = this.$refs.L.textContent
      this.requisitos = this.$refs.requisitos.textContent
      this.dictaDepartamento = this.$refs.dicta_departamento.textContent
      this.fechaDictado = this.$refs.annio_semestre_nivel.textContent
      this.categoria = this.$refs.categoria.textContent
      this.hrspresenciales = this.$refs.horas_presenciales_a_la_semana.textContent
      this.perfil_profesor = this.$refs.perfil_profesor.textContent
      this.version = this.$refs.version.textContent
      this.resolucionFacultad = this.$refs.resolucion.textContent
      this.desAsignatura = this.$refs.descripcion_de_la_asignatura.value
      this.estMeto= this.$refs.estrategias_metodologicas.value
      this.infoAdicional= this.$refs.informacion_adicional.value
      this.fInfo= this.$refs.fuente_de_informacion.value
      
      // Juntar datos de obj asociados perfil egreso
      var OPE = "";
      var children = document.getElementById("listaAgregar").children;
      var tamano = children.length;
      var j=0;
      for (var i=0;i<Number(tamano);i++){
          var ID = children[i].id;
          if (ID.localeCompare("NO")!=0 && ID.localeCompare("NO1")!=0 && ID.localeCompare("")!=0){
              j=j+1;
              var auxRef = "OAPE"+j
              var auxOPE = document.getElementById(auxRef).value;
              OPE= OPE+""+j+". "+auxOPE+"\n";
              
          }
      }
      this.ObjPegreso = OPE;
      // juntar datos de objetivos generales y especificos 
      var OAS = "Objetivos generales\n";
      var children = document.getElementById("listaAgregarOG").children;
      var tamano = children.length;
      var j=0;
      for (var i=0;i<Number(tamano);i++){
          var ID = children[i].id;
          if (ID.localeCompare("NO")!=0 && ID.localeCompare("NO1")!=0 && ID.localeCompare("")!=0){
              j=j+1;
              var auxRef = "OG"+j
              var auxOA = document.getElementById(auxRef).value;
              OAS= OAS+""+j+". "+auxOA+"\n";
              
          }
      }
      OAS=OAS+ "Objetivos específicos\n"
      var children = document.getElementById("listaAgregarOE").children;
      var tamano = children.length;
      var j=0;
      for (var i=0;i<Number(tamano);i++){
          var ID = children[i].id;
          if (ID.localeCompare("NO")!=0 && ID.localeCompare("NO1")!=0 && ID.localeCompare("")!=0){
              j=j+1;
              var auxRef = "OE"+j
              var auxOA = document.getElementById(auxRef).value;
              OAS= OAS+""+j+". "+auxOA+"\n";
              
          }
      }
      this.ObjAsignatura = OAS;
      this.nombrePrograma = "Programa de "+this.asignatura
      this.fechaCreacion="2018-06-10"
      this.fechaUltimaModificacion="2018-06-10"
      //UNIDADES
      this.unidades = [];
      var auxUnidades = [];
      /*
          Hacer total automatico
      */
      var totalHoras = 5;
      for (var i=1; i<=Number(cantUnid); i++){
        auxUnidades.push(i);
        var idSU = "CantSU"+i;
        var cantidadSU = cantSU[i-1][1];
        console.log("esto es cantidad SU "+ cantidadSU+ " de la unidad "+i);
        var idTITULO = "titulo_unidad_"+i;
        var tituloUnidad = document.getElementById(idTITULO).value;
        console.log("eL TITULO "+ tituloUnidad);
        var idHORAS = "n_horas_unidad_"+i;
        var horasUnidad = document.getElementById(idHORAS).value;
        console.log("esto N horas unidad "+ horasUnidad);
        var capID = "capacidades_a_desarrollar"+i;
        var capacidades = document.getElementById(capID).value;
        console.log("capacidades "+ capacidades);
        var topID = "topicos_a_ser_evaluados"+i;
        var topicos = document.getElementById(topID).value;
        console.log("topicos "+ topicos);
        //verificar si hay Sub unidades
        var auxSU = [];
        if (Number(cantidadSU) > 0){
          console.log("Agregando sub unidades ");
          //obtener datos sub unidades
          
          for (var k=1; k<=Number(cantidadSU);k++){
              var contID = "SU_"+i+"."+k;
              var contenido = document.getElementById(contID).value;
              console.log("contenido SU "+contenido);
              var horasSuID = "n_horas_unidad_SU_"+i+"."+k;
              var horasSU = document.getElementById(horasSuID).value;
              console.log("horas SU "+ horasSU);
              auxSU.push(k);
              auxSU.push(contenido);
              auxSU.push(horasSU);
          }
        }
        else{
              auxSU.push("");
              auxSU.push("");
              auxSU.push("");
        }
        
        auxUnidades.push(tituloUnidad);
        auxUnidades.push(horasUnidad);
        //auxUnidades.push(totalHoras);
        auxUnidades.push(capacidades);
        auxUnidades.push(topicos);
        auxUnidades.push(cantidadSU);
        auxUnidades.push(auxSU);
        this.unidades.push(auxUnidades);
        auxUnidades= [];
      }
      this.Unidades = this.unidades
      console.log("esto es unidades "+this.Unidades);
      console.log("cantidad de unidades :" + this.Unidades.length)
      this.postPrograma()
    },
    //Funcion que se encarga de añadir campos de la pagina 
    // para posteriormente agregar mas campos de objetivos especifico o generales 
    // En el formato del programa
    agregar:function(tipo){
        console.log("es es el tipo"+tipo);
        if (Number(tipo)==1){
          var nombreDiv="listaAgregar";
          var nombreId="OAPE";
        } else if(Number(tipo)==2){
          var nombreDiv="listaAgregarOG";
          var nombreId="OG";
        } else{
          var nombreDiv="listaAgregarOE";
          var nombreId="OE";
        }
        console.log("datos "+nombreDiv+ "y "+nombreId);
        var children = document.getElementById(nombreDiv).children;
        var tamano = children.length;
        console.log("este es el tamano :"+tamano);
        var ultimoID = children[tamano-1].id;
        
        console.log("este es el hijito :"+ultimoID);
        if (ultimoID.localeCompare("NO")!=0){
          console.log("SI");
          var res = ultimoID.split(nombreId);
          var numID=res[1];
          var div = document.getElementById(nombreDiv);
          var input = document.createElement("input");
          var espacio = document.createElement("br");
          var ID= Number(numID)+1;
          input.setAttribute("id", nombreId + ID);
          input.setAttribute("type", "text");
          input.setAttribute("style","width:400px;");
          input.className = "input";
          div.appendChild(espacio);  
          div.appendChild(input);
        }
        else{
          console.log("NO :");
          var div = document.getElementById(nombreDiv);
          var input = document.createElement("input");
          var espacio = document.createElement("br");
          var ID= 2;
          input.setAttribute("id", nombreId + ID);
          input.setAttribute("type", "text");
          input.setAttribute("style","width:400px;");
          input.className = "input";
          div.appendChild(espacio);  
          div.appendChild(input);
        }
        
    },
    //Funcion que se encarga de eliminar campos de la pagina 
    // correspondientes a  objetivos especifico o generales 
    quitar:function(tipo){
         if (Number(tipo)==1){
          var nombreDiv="listaAgregar";  
        } else if(Number(tipo)==2){
          var nombreDiv="listaAgregarOG";
        } else{
          var nombreDiv="listaAgregarOE";
        }
        var children = document.getElementById(nombreDiv).children;
        var tamano = children.length;
        var dselectedProgramiv = document.getElementById(nombreDiv);
        console.log("este es el tamano :"+tamano);
        var ultimoID = children[tamano-1].id;
        console.log("este es el hijito :"+ultimoID);
        if (ultimoID.localeCompare("NO")!=0){
          div.removeChild(div.lastChild);
          div.removeChild(div.lastChild);
        }
        
    },
    //Funcion que se encarga de agregar unidades en los campos de la pagina 
    //Para poder añadir esta informacion al formato del programa 
    agregarUnidades:function(){
        console.log("principio "+ cantUnid);
        var cantU = Number(cantUnid) + 1;
        cantUnid = cantU;
        console.log("ultima "+cantUnid);
        var div = document.getElementById("unidades");
        var divUnid = document.createElement("div");
        divUnid.setAttribute("id","unidad"+cantUnid);
        var unidad= document.createElement("H4");
        var titulo= document.createElement("P");
        var n_horas= document.createElement("P");
        var texto1 = document.createTextNode("UNIDAD "+cantU);
        var texto2 = document.createTextNode("Título ");
        var texto3 = document.createTextNode("N° Horas pedagogicas");
        unidad.appendChild(texto1);
        titulo.appendChild(texto2);
        n_horas.appendChild(texto3);
       // var textoUnid = document.createTextNode(cantU);
        divUnid.appendChild(unidad);
        //divUnid.appendChild(textoUnid);
        
        var inputName = document.createElement("input");
        inputName.setAttribute("id", "titulo_unidad_"+cantU);
        divUnid.appendChild(titulo);
        divUnid.appendChild(inputName);
        
        var inputHoras = document.createElement("input");
        inputHoras.setAttribute("id", "n_horas_unidad_"+cantU);
        divUnid.appendChild(n_horas);
        divUnid.appendChild(inputHoras);
        var textArea   = document.createElement("textarea");
        textArea.setAttribute("id","capacidades_a_desarrollar"+cantU);
        textArea.setAttribute("rows","8");
        textArea.setAttribute("cols","80");
        var subTituloCont= document.createElement("P");
        var texto = document.createTextNode("Capacidades a desarrollar ");
        subTituloCont.appendChild(texto);
        divUnid.appendChild(subTituloCont);
        divUnid.appendChild(textArea);
        var textArea2   = document.createElement("textarea");
        textArea2.setAttribute("id","topicos_a_ser_evaluados"+cantU);
        textArea2.setAttribute("rows","8");
        textArea2.setAttribute("cols","80");
        var subTituloCont2= document.createElement("P");
        var texto2 = document.createTextNode("Topicos a ser evaluados ");
        subTituloCont2.appendChild(texto2);
        divUnid.appendChild(subTituloCont2);
        divUnid.appendChild(textArea2);
          var auxSU=[cantU,0];
          cantSU.splice((cantU-1),0,auxSU);
          var espacio2 = document.createElement("br");
          divUnid.appendChild(espacio2);
          var espacio3 = document.createElement("br");
          divUnid.appendChild(espacio3);
          var campoSU= document.createElement("P");
          var textoSU = document.createTextNode("Subunidades ");
          campoSU.appendChild(textoSU);
          divUnid.appendChild(campoSU);
          var boton = document.createElement("button");
          var textoBoton = document.createTextNode("+ Subunidad");
          boton.setAttribute("id", "hellobutton"+cantU);
          boton.setAttribute("style","background:#ea7500e3;color: #FFFFFF;  font-size: 12pt");
          boton.appendChild(textoBoton);
          divUnid.appendChild(boton);
          var botonElim = document.createElement("button");
          var textoBotonElim = document.createTextNode("- Subunidad");
          botonElim.setAttribute("id", "menosButton"+cantU);
          botonElim.setAttribute("style","background:#ea7500e3;color: #FFFFFF; font-size: 12pt");
          botonElim.appendChild(textoBotonElim);
          divUnid.appendChild(botonElim);
          var divSU = document.createElement("div");
          divSU.setAttribute("id","divSU"+cantU);
          divUnid.appendChild(divSU);
          var espacio = document.createElement("br");
          divUnid.appendChild(espacio);
          var linea= document.createElement("P");
          var textoLinea = document.createTextNode("________________________________________________________________________");
          linea.appendChild(textoLinea);
          divUnid.appendChild(linea);
          div.appendChild(divUnid);
          document.getElementById("menosButton"+cantU).addEventListener("click", function(){eliminarSU(cantU)}, false );
          document.getElementById("hellobutton"+cantU).addEventListener("click", function(){agregarSU(cantU)}, false );
    },
    //Funcion que se encarga de eliminar la unidad de los campos de la pagina
    eliminarUnidades: function(){
     console.log("eliminar unidad ");
    if (Number(cantUnid)!=0){
        var div = document.getElementById("unidad"+cantUnid);
        var tamano = div.children.length;
        console.log("Cantidad principio al eliminar"+ cantUnid);
        var cantU = Number(cantUnid) - 1;
        cantUnid = cantU;
        console.log("cantidad ultima al eliminar "+cantUnid);
        cantSU.pop();
        console.log("estas son la sSU finales "+cantSU);
         if(div !== null){
            var parent = div.parentElement;
            parent.removeChild(div);
        }   
      }
    } 
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import '../fondo.css';
.tabla1 , th, td {
   border: 0px solid #1700ea3b;
  
  height: 0px;
  
}
.texto_input{
  background-color: #ffffff48;
  
}
.tabla{ position:relative; top:80px; left: 350px; 
  }
.bloque1 {
  background-color: #002f6c21;
  padding: 10px;
  
}
textarea { 
   height: 12em;
   width: 700px;
}
.botones {
  background: #ea7500e3;
  block-size: 40px;
  font-size: 16px;
  margin-left: 20px;
  position: relative; left: 200px;
  border-radius: 5px 10px 5px 10px;
  color: #e6e3e3;
  font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}
.botones2 {
  background: #ea7500e3;
  block-size: 30px;
  font-size: 14px;
  position: relative; left: 0px;
  border-radius: 5px 10px 5px 10px;
  color: #ffffff;
  font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}
</style>
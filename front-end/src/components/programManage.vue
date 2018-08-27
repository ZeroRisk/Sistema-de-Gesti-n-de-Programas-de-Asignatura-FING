<template>
  <div class="main_file">

     <div class="botonesUP" >
      <button class="botones" v-on:click="saveData">Guardar</button>
      <button class="botones"  v-on:click="asignarUser" >Asignar</button>
      <button class="botones" v-on:click="genPDF">Descargar</button>
      <button class="botones">Atras</button>
    </div>

    <!-- 
      Itera sobre la variables Datos y almacena la informacion en dato
    -->
    <table class="tabla"  v-for="dato in Datos" >
   
    
    <div class="all" >
      
    <div class="test" ref="test">
    <!-- 
      Datos del programa que no se pueden modificar
    -->
    <h4>1. PROGRAMA DE LA ASIGNATURA </h4>
    <table class="bloque1">
    <table class="tabla1">
    <td align="left">Resolución</td>
    <td  align="left"><input type="text" readonly class="texto_input" ref="resolucion" :value="dato.resolucion"></td>
    
    <tr>
      <td>Carrera :</td>
      <td ><input type="text" readonly id="carreraNombre" class="texto_input" ref="carrera" :value="detallePrograma[0].carrera"></td>
    </tr>
    <tr>
      <td>Asignatura :</td>
      <td ><input type="text" readonly class="texto_input" ref="asignatura" :value="dato.nombreAsignatura"></td>
    </tr>
    <tr>
      <td>Código :</td>
      <td><input type="text"  readonly class="texto_input" width="50" height="16" ref="codigo" :value="dato.codigo"></td>
    </tr>
    <tr>  
      <td align="right" >T: </td>
      <td><input type="text"  readonly class="texto_input"  style="width:35px;" ref="T" :value="dato.horasT">
      E:<input type="text"  readonly class="texto_input"  style="width:35px;" ref="E" :value="dato.horasE">
      L:<input type="text" readonly class="texto_input"  style="width:35px;" ref="L" :value="dato.horasL"></td>
    </tr>
    <tr>
      <td>Requisitos: </td>
      <td ><input type="text" readonly class="texto_input" ref="requisitos" :value="dato.requisitos"></td>
    </tr>
    <tr>
      <td align="left">Dicta Departamento: </td>
      <td ><input type="text"  readonly class="texto_input" ref="dicta_departamento" value="Departamento Mecánica"></td>
    </tr>
    <tr>
      <td align="left">Año - Semestre - Nivel: </td>
      <td  ><input type="text" readonly  class="texto_input" ref="annio_semestre_nivel" value="2018-1-1"></td>
    </tr>
    <tr>
      <td align="left">Tipo: </td>
      <td  ><input type="text" readonly class="texto_input" ref="categoria" :value="dato.tipo"></td>
    </tr>
    <tr>
      <td align="left" >Horas presenciales: </td>
      <td ><input type="text"  readonly class="texto_input" id="horas_presenciales_a_la_semana" ref="horas_presenciales_a_la_semana" :value="detallePrograma[0].horasPre"></td>
    </tr>
    <tr>
      <td align="left">Perfil profesor:</td>
      <td ><input type="text"  class="texto_input" ref="perfil_profesor" :value="detallePrograma[0].perfilProfe"></td>
    </tr>
    <tr>
    <td align="right">SCT</td>
      <td><input type="text" readonly  class="texto_input" ref="SCT" :value="dato.sct"></td>
    </tr>
    <tr>
      <td align="left">Versión</td>
      <td><input type="text" readonly class="texto_input" ref="version" :value="detallePrograma[0].version"></td>
    </tr>
  </table>
  </table>
  
    <!-- 
      Descripcion y objetivos de la asignatura
    -->
    <h4>2. DESCRIPCION DE LA ASIGNATURA </h4>
    <textarea id="descripcion_de_la_asignatura" ref="descripcion_de_la_asignatura">{{detallePrograma[0].descripAsign}}</textarea>
    <h4>3. OBJETIVOS DE APRENDIZAJE </h4>
    <h5>3.1 ASOCIADOS A PERFIL DE EGRESO</h5>
    <div id="listaAgregar">
    <input id="OAPE1" type="text" ref="asociados_a_perfil_de_egreso" style="width:400px;"/>
    <button class="botones2" v-on:click="agregar(1,'')" id="NO1">+</button>
    <button  class="botones2" v-on:click="quitar(1,'')" id="NO">- </button>
    </div>
    <h5>3.2 ASOCIADOS A LA ASIGNATURA</h5>
    <h5>Objetivos Generales</h5>
    <div id="listaAgregarOG">
    <input type="text" id="OG1" ref="objetivos_generales"  style="width:400px;"/>
    <button  class="botones2" v-on:click="agregar(2,'')"  id="NO1">+</button>
    <button  class="botones2" v-on:click="quitar(2,'')" id="NO">- </button>
    </div>
    
    </div>
    <div class="componente2" ref="test2">
    <h5>Objetivos específicos</h5>
    <div id="listaAgregarOE">
      <input type="text" id="OE1" ref="objetivos_especificos"  style="width:400px;"/>
      <button  class="botones2" v-on:click="agregar(3,'')"  id="NO">+</button>
      <button  class="botones2"  v-on:click="quitar(3,'')" id="NO">-</button>
    </div>
    

    <!-- 
      Contenido de UNIDADES y sub unidades
    -->
    <h4>4. UNIDADES CONTENIDO </h4>
       <div id="unidades">
      </div>
      <input type="button" class="botones2" id="boton" value="+ Agregar Unidad" v-on:click="agregarUnidades('')" />
      <input type="button" class="botones2" id="botonElim" value="- Eliminar Unidad" v-on:click="eliminarUnidades" />   
      <br/>
    </div>

    <!-- 
      Estrategias metodologicas , informacion adicional y fuentes de informacion de la asignatura  
    -->
    <div class= "pagina3"> 
      <h4>6. ESTRATEGIAS METODOLÓGICAS</h4>
      <textarea id="estrategias_metodologicas" ref="estrategias_metodologicas" rows="8" cols="80">{{detallePrograma[0].estratMeto}}</textarea>
      <h4>7. INFORMACIÓN ADICIONAL</h4>
        <textarea  id="informacion_adicional" ref="informacion_adicional" rows="8" cols="80">{{detallePrograma[0].infoAd}}</textarea>
       <h4>8. FUENTE DE INFORMACIÓN</h4>
         <textarea id="fuente_de_informacion" ref="fuente_de_informacion" rows="8" cols="80">{{detallePrograma[0].fuenteInfo}}</textarea>
    </div>
   <br/>    
  </div> 
</table>


  <!-- 
    Menu lateral    
  -->
<div id='cssmenu' >
<ul>

     <li v-show="!isAdmin" > 
     <router-link :to="{ name: 'Home', params: { user: user , type: type }}"> 
      <a><span>Home</span></a> 
      </router-link> 
   </li> 
    <li v-show="isAdmin" > 
      <router-link :to="{ name: 'HomeAdmin', params: { user: user , type: type }}"> 
      <a><span>Home</span></a> 
      </router-link> 
      </li> 
   <li class='active has-sub'> 
     <router-link :to="{ name: 'MenuPrograma', params: { user: user , type: type }}"> 
     <a><span>Editar Programa</span></a> 
     </router-link> 
     </li> 
    <li> 
      <router-link :to="{ name: 'PlanEstudio', params: { user: user , type: type }}"> 
      <a><span>Crear Plan de Estudio</span></a> 
      </router-link> 
      </li> 
 
   <li v-show="!isAdmin"> 
     <router-link :to="{ name: 'BuscarPorFecha', params: { user: user , type: type }}"> 
     <a><span>Buscar por Fecha/Asignatura</span></a> 
     </router-link> 
     </li> 
    <li v-show="isAdmin"> 
     <router-link :to="{ name: 'BuscarPorFechaAdmin', params: { user: user , type: type }}"> 
     <a><span>Buscar por Fecha/Asignatura</span></a> 
     </router-link> 
     </li> 

</ul>

</div>
  <!-- 
      encabezado pagina 
    -->
<div class="content-box-top2">Bienvenido al portal.<a href="#/"><span class="cerrar">Cerrar sesión</span></a></div>
<div class="content-box-left"><img src="../assets/usach.png" height="100" width="200"></div>


</div>

  
</template>

<script>
import html2canvas from 'html2canvas'
var globalBoton = 0;
var cantUnid = 0;
var cantSU= [];

/** Funcion que agrega a la pagina una formulario donde añadir datos de una nueva sub-unidad 

 */
function agregarSU(num, texto) {
    // Dependiendo del contenido de la variable texto se setean CONT y HP
    // Si no es vacio se recupera el contenido de las sub-unidades exitentes
    if(texto==''){
      var CONT='';
      var HP='';
    }
    else{
      var CONT=texto.contenidos1;
      var HP=texto.horasPresen;
    }

    // Se aumenta contador de Sub-unidades
    var auxCantSU = cantSU[(Number(num)-1)][1];
    var nuevaCantSU = Number(auxCantSU)+1;
    cantSU[(Number(num)-1)][1]=nuevaCantSU;

    // Se crean los elementos del formulario
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
    var textArea2 = document.createElement("textarea");
    var textoArea2 = document.createTextNode(CONT);
    textArea2.appendChild(textoArea2);
    textArea2.setAttribute("id","SU_"+num+"."+nuevaCantSU);
    textArea2.setAttribute("rows","8");
    textArea2.setAttribute("cols","80");

    var input2 = document.createElement("input");
    input2.setAttribute("id", "n_horas_unidad_SU_"+num+"."+nuevaCantSU);
    input2.setAttribute("type", "text");
    input2.setAttribute("style","width:40px;");
    input2.setAttribute("value",HP);
    div.appendChild(tituloCont);
    div.appendChild(titulo1);
    div.appendChild(textoSUB);
    div.appendChild(titulo2);
    div.appendChild(textArea2);
    div.appendChild(titulo3);
    div.appendChild(input2);
   
}

/** Elimina un sub-unidad
    Entrada : numero de unidad a la cual pertenece la sub-unidad
 */
function eliminarSU(numUnidad){

    var div = document.getElementById("divSU"+numUnidad);
    var tamano = div.children.length;
    var auxCantSU = cantSU[(Number(numUnidad)-1)][1];
    // Disminuye cantidad de sub-unidades si es que hay sub-unidades
    if(Number(auxCantSU)>0){
        var nuevaCantSU = Number(auxCantSU)-1;
        cantSU[(Number(numUnidad)-1)][1]=nuevaCantSU;
    }
    // Quita los elementos de formulario de la sub-unidad agregados 
    if (Number(tamano)>0){
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
  // variables que se reciben desde otras paginas
  props: ['user','type', 'idRes', 'idAsig', 'idCarrera'],
  
  
  /** Antes de que cargue la pagina se obtiene los datos asociados al programa de asignatura seleccionado
  desde la pagina MenuPrograma
   */
  mounted: function (){ 
      this.cantUnid = 0;
      if(this.type != "Admin"){ 
        this.isAdmin=false 
      }
      //obtiene datos relacionados a una asignatura
       this.$http.get("http://localhost:5000/datosplanasig?id_plan="+this.idRes+"&id_asignatura="+this.idAsig)
        .then(response =>{
            this.Datos = response.body.datos
            var auxIdDetalle = response.body.id_detalle
            console.log(this.Datos)
            console.log(auxIdDetalle[0].detalle_programa_iddetalle_programa)
            this.idDetalle = auxIdDetalle[0].detalle_programa_iddetalle_programa
            //console.log("Esto es el id que se guarda "+this.idDetalle);
            if(this.Datos.length==0){
                alert("No existen planes para esta carrera");
              
            }
            // Obtiene datos de detalle programa, unidades y sub-unidades
            else if(this.Datos.length!=0){
                        var id_det = this.idDetalle;
                        console.log("Esto es el id que se manda "+this.idDetalle);
                  this.$http.get("http://localhost:5000/desarrolloP?iddetalle="+id_det)
                    .then(response =>{
                        this.detallePrograma = response.body.Desarrollo
                        this.dataU = response.body.Unidades
                        this.dataSU = response.body.SubUnidades

                        console.log(this.detallePrograma)
                        console.log(this.dataU)
                        console.log(this.dataSU)
                        this.carrera = this.detallePrograma[0].carrera
                        if(this.detallePrograma.length==0){
                            alert("No existen detalles para este programa");
                          
                        }
                        }, response =>{
                            console.log("falla detalle programa")
                        });
            }
            }, response =>{
                console.log("falla asignatura ")
            }); 
  }, 


  /**Esto Se ejecuta luego de cargar los datos
    Carga, si existen, datos dinamicos del programa (objetivos, unidades y sub-unidades)
  */
  updated: function () {
        this.$nextTick(function () {
          //cargar perfiles de egreso
          var auxOPE = this.detallePrograma[0].objetivoPerfilEgreso;
          var res = auxOPE.split("-");
          var tamano = res.length-1;
          if (tamano>=1){
              document.getElementById("OAPE1").setAttribute('value',res[0]);
              for (var i=1; i<tamano;i++){
                  this.agregar(1,res[i]);
              }
              
          }

          //cargar objetivos de la asignatura
          var auxOA = this.detallePrograma[0].objetivoAsign;
          var res = auxOA.split("-");
            //objetivos generales
            var auxOG = res[0].split("/");
            var tamano = auxOG.length-1;
            if (tamano>=1){
              document.getElementById("OG1").setAttribute('value',auxOG[0]);
              for (var i=1; i<tamano;i++){
                  this.agregar(2,auxOG[i]);
              }

            //objetivos especificos
            var auxOE = res[1].split("/");
             var tamano = auxOE.length-1;
             if (tamano>=1){
              document.getElementById("OE1").setAttribute('value',auxOE[0]);
              for (var i=1; i<tamano;i++){
                  this.agregar(3,auxOE[i]);
              }
             }
          }

          //Unidades
          var tamanoU= this.dataU.length;
          console.log("tamano unidades ya escritas "+tamanoU)
          if (tamanoU!=0){
            for (var i=0;i<tamanoU;i++){
              this.agregarUnidades(this.dataU[i]);
            }
            var tamanoSU = this.dataSU.length;
            if(tamanoSU!=0){
              //verificar a que unidad pertenece
              for(var i=0;i<tamanoSU;i++){
                //console.log("Pertenece a la unidad "+this.dataSU[i].unidades_idunidades);
                var idU= this.dataSU[i].unidades_idunidades;
                var textoSU= this.dataSU[i];
                agregarSU(idU, textoSU);
              }
            }
          }
        })
  },
  data () {
    
    return {
      isAdmin:true,
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
      Datos:[],
      idDetalle:0,
      detallePrograma:[],
      dataU:[],
      dataSU:[] 
   }
  },
  methods: {

    /**
      Guarda datos del detalle del programa
     */
    postPrograma: function(){
      this.$http.post('http://localhost:5000/newDetalle',{
        iddetalle: this.cantidad,
        carrera: this.carrera,
        asignatura: this.asignatura,
        codigo: this.Datos[0].codigo,
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
          //alert("se guardo la informacion del programa exitosamente")
        }, response=>{
          console.log("no se pudo")
          //alert("hubo un error al guardado de datos, checkee su conexion")
        });
        
      }, response=>{
        console.log("no se agrego detalle")
        this.$router.push({ name: 'HomeAdmin', params: { user: this.user , type: this.type}})
      });
      
    },
    /**
      Agrega unidades
     */
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
    postSubUnidad: function(SubUnidad,numeroUnidad,n){
    
      var cont1= ("subunidad numero " + SubUnidad[n])

      this.$http.post('http://localhost:5000/newUnidadTem',{
        contUno: cont1 ,
        contDos: SubUnidad[n+1],
        horasPres: parseInt(SubUnidad[n+2]),
        unidades_idunidades: numeroUnidad
      }).then(response =>{
        console.log("ingreso subUnidad ")
        //alert("Datos guardados")
        this.$router.push({ name: 'HomeAdmin', params: { user: this.user , type: this.type}})

      }, response =>{
        console.log("falle en enviar subunidad")
        //alert("Datos guardados")
        this.$router.push({ name: 'HomeAdmin', params: { user: this.user , type: this.type}})

      })
    },

    /**

        FUNCIONES CREACION PDF PENDIENTES

     */
    createPDF: function(event) {
      var doc = new jsPDF()
      //.text(texto que se desea guardar,X,Y) "X" posicion en la linea e 
      //"Y" corresponde al numero de la linea
      doc.text('Hello world!', 50, 40)
      doc.save('a4.pdf')
    },
    genPDF: function(event){
      console.log("elemento :", this.$refs.test)
      html2canvas(this.$refs.test).then(canvas =>{
          var doc = new jsPDF()
         
          var img = canvas.toDataURL("image/png",1)
          doc.addImage(img,'PNG',5,10)
          doc.save('test.pdf')
          
        })
      },

    /**
      Carga pagina para asignar programa
     */
    asignarUser: function(event) {
      

      var verifica = true;

      // Revisa que los campos obligatorios esten completos.
      // De estarlos, cambia la var "verifica" a "false".

      if(this.$refs.carrera.textContent!="" && this.$refs.asignatura.textContent != "" && 
      this.$refs.codigo.textContent!="" && this.$refs.T.textContent!="" && this.$refs.E.textContent!="" && this.$refs.L.textContent!="" && this.$refs.requisitos.textContent!="" && this.$refs.dicta_departamento.textContent!="" && this.$refs.annio_semestre_nivel.textContent!="" && this.$refs.categoria.textContent!="" && this.$refs.horas_presenciales_a_la_semana.textContent!="" && this.$refs.perfil_profesor.textContent!="" && this.$refs.version.textContent!="" && this.$refs.version.textContent!="" && this.$refs.resolucion.textContent!=""){
        console.log("ESTAN COMPLETADOS")
        verifica = false;
      }

      // Si la var "verifica" es "true", no permite asignar.
      // Si la var "verifica" es "false", permite comenzar a asignar.

      if(verifica){
        alert("Faltan campos obligatorios por completar!\nNo se puede asignar un documento con campos obligatorios vacios.");
        console.log("Existen campos obligatorios sin completar.")


      }else{
        if (confirm("Desea asignar este documento a un usuario?")){
        console.log("Se asignará documento a un user")

        //window.open("http://localhost:8081/#/asignarPrograma");
        this.$router.push({ name: 'asignarPrograma', params: { user: this.user , type: this.type}})

        }else{
          console.log("No se asignará documento")
        }
      } 
    },

    /**
      Funcion que reune la informacion para guardarla
     */
    saveData: function(event){
      //this.carrera = detallePrograma[0].carrera
      this.codigo = this.$refs.codigo.textContent
      this.HT = this.$refs.T.textContent
      this.HE = this.$refs.E.textContent
      this.HL = this.$refs.L.textContent
      this.requisitos = this.$refs.requisitos.textContent
      this.dictaDepartamento = "Departamento Mecanica"
      this.fechaDictado = "2018-1-1"
      this.categoria = this.Datos[0].tipo
      this.hrspresenciales = document.getElementById("horas_presenciales_a_la_semana").value;
      // this.$refs.horas_presenciales_a_la_semana.textContent
      console.log("horas presenciales a guardar "+this.hrspresenciales)
      console.log("algo como HT "+this.HT)
      this.perfil_profesor = "Cool profe"
      //this.$refs.perfil_profesor.textContent
      this.version = "version1"
      //this.$refs.version.textContent
      this.resolucionFacultad = this.Datos[0].resolucion
      this.desAsignatura = document.getElementById("descripcion_de_la_asignatura").value
      console.log("------------------------------------------------ "+this.desAsignatura)
      // this.$refs.descripcion_de_la_asignatura.value
      this.estMeto= document.getElementById("estrategias_metodologicas").value
      //this.$refs.estrategias_metodologicas.value
      this.infoAdicional= document.getElementById("informacion_adicional").value
      //this.$refs.informacion_adicional.value
      this.fInfo= document.getElementById("fuente_de_informacion").value
      //this.$refs.fuente_de_informacion.value
      
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
      //console.log("esto se guardara "+OPE);

      // Prepara los datos de objetivos / juntar datos de objetivos generales y especificos 
      var OAS = "";
      var children = document.getElementById("listaAgregarOG").children;
      var tamano = children.length;
      var j=0;
      for (var i=0;i<Number(tamano);i++){
          var ID = children[i].id;
          if (ID.localeCompare("NO")!=0 && ID.localeCompare("NO1")!=0 && ID.localeCompare("")!=0){
              j=j+1;
              var auxRef = "OG"+j
              var auxOA = document.getElementById(auxRef).value;
              OAS= OAS+""+j+". "+auxOA+"/";
              
          }
      }
      OAS=OAS+ "-";
      var children = document.getElementById("listaAgregarOE").children;
      var tamano = children.length;
      var j=0;
      for (var i=0;i<Number(tamano);i++){
          var ID = children[i].id;
          if (ID.localeCompare("NO")!=0 && ID.localeCompare("NO1")!=0 && ID.localeCompare("")!=0){
              j=j+1;
              var auxRef = "OE"+j
              var auxOA = document.getElementById(auxRef).value;
              OAS= OAS+""+j+". "+auxOA+"/";
              
          }
      }
      OAS=OAS+"-";
      this.ObjAsignatura = OAS;
      console.log("esto se guardara "+OAS);
      this.nombrePrograma = "Programa de "+this.asignatura
      this.fechaCreacion="2018-06-10"
      this.fechaUltimaModificacion="2018-06-10"


      //UNIDADES
      //this.cantidadU = this.$refs.cantidadAsig.value
      console.log("esto es la cantidad de unidades "+cantUnid);
      this.unidades = [];
      var auxUnidades = [];
      var totalHoras = 5;
      console.log("esto es total"+ totalHoras);
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
      //console.log("esto es unidades "+this.Unidades);
      //console.log("cantidad de unidades :" + this.Unidades.length)
      
      
      // Sigue con la funcion postPrograma
      this.postPrograma()
    },

    /** 
      Agrega objetivos (generales , especificos , asociados a perfil de egreso)
      Entrada : tipo que contiene el tipo de objetivo a agregar
                texto que contiene una cadena vacia o un dato almacenado anteriormente 
     */
    agregar:function(tipo,texto){
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
        var children = document.getElementById(nombreDiv).children;
        var tamano = children.length;
        var ultimoID = children[tamano-1].id;
        
        // si es el primer objetivo a agregar
        if (ultimoID.localeCompare("NO")!=0){
          var res = ultimoID.split(nombreId);
          var numID=res[1];
          var div = document.getElementById(nombreDiv);
          var input = document.createElement("input");
          var espacio = document.createElement("br");
          var ID= Number(numID)+1;
          input.setAttribute("id", nombreId + ID);
          input.setAttribute("type", "text");
          input.setAttribute("style","width:400px;");
          input.setAttribute("value",texto);
          input.className = "input";
          div.appendChild(espacio);  
          div.appendChild(input);
        }
        else{
          // Si es el segundo objetivo a agregar
          var div = document.getElementById(nombreDiv);
          var input = document.createElement("input");
          var espacio = document.createElement("br");
          var ID= 2;
          input.setAttribute("id", nombreId + ID);
          input.setAttribute("type", "text");
          input.setAttribute("style","width:400px;");
          input.setAttribute("value",texto);
          input.className = "input";
          div.appendChild(espacio);  
          div.appendChild(input);
        }
        
    },

    /** 
      Elimina objetivos (generales , especificos , asociados a perfil de egreso)
      Entrada : tipo que contiene el tipo de objetivo a eliminar
                 
     */
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
        var div = document.getElementById(nombreDiv);
        var ultimoID = children[tamano-1].id;
        if (ultimoID.localeCompare("NO")!=0){
          div.removeChild(div.lastChild);
          div.removeChild(div.lastChild);
        }
        
    }, 

    /** 
      Agrega de forma dinamica una unidad
      Entrada : variable texto que contiene una cadena vacia o un dato almacenado anteriormente 
     */
    agregarUnidades:function(texto){
      // Si texto contiene cadena vacia de setean las variables con vacio, si no se setean con los datos obtenidos
        if (texto==''){
          var tit='';
          var nHP='';
          var cap='';
          var topE='';
        }
        else{
          var tit=texto.tituloUnidad;
          var nHP=texto.horasPeda;
          var cap=texto.capaDesarrolla;
          var topE=texto.topicosEvalua;    
        }

        // Aumenta contador de unidades
        var cantU = Number(cantUnid) + 1;
        cantUnid = cantU;
        // Crea elementos del formulario de unidad
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
        divUnid.appendChild(unidad);

        var inputName = document.createElement("input");
        inputName.setAttribute("id", "titulo_unidad_"+cantU);
        inputName.setAttribute("value", tit);
        divUnid.appendChild(titulo);
        divUnid.appendChild(inputName);

        var inputHoras = document.createElement("input");
        inputHoras.setAttribute("id", "n_horas_unidad_"+cantU);
        inputHoras.setAttribute("value",  nHP);
        divUnid.appendChild(n_horas);
        divUnid.appendChild(inputHoras);

        var textArea   = document.createElement("textarea");
        textArea.setAttribute("id","capacidades_a_desarrollar"+cantU);
        textArea.setAttribute("rows","8");
        textArea.setAttribute("cols","80");
        var textoArea1 = document.createTextNode(cap);
        textArea.appendChild(textoArea1);
        var subTituloCont= document.createElement("P");
        var texto = document.createTextNode("Capacidades a desarrollar ");
        subTituloCont.appendChild(texto);
        divUnid.appendChild(subTituloCont);
        divUnid.appendChild(textArea);

        var textArea2   = document.createElement("textarea");
        textArea2.setAttribute("id","topicos_a_ser_evaluados"+cantU);
        textArea2.setAttribute("rows","8");
        textArea2.setAttribute("cols","80");
        var textoArea2 = document.createTextNode(topE);
        textArea2.appendChild(textoArea2);

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
          var textoSU = document.createTextNode("Subunidades Unidad "+cantU);
          campoSU.appendChild(textoSU);
          divUnid.appendChild(campoSU);
          //Crea boton para agregar sub-unidadeds
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
          /**
          Agrega listener para los botones de agregar y eliminar Sub-unidades
           */
          document.getElementById("menosButton"+cantU).addEventListener("click", function(){eliminarSU(cantU)}, false );
          document.getElementById("hellobutton"+cantU).addEventListener("click", function(){agregarSU(cantU,'')}, false );
      
    
    },

    /**
        Permite eliminar la ultima unidad
     */
    eliminarUnidades: function(){
      if (Number(cantUnid)!=0){
          var div = document.getElementById("unidad"+cantUnid);
          var tamano = div.children.length;
          //Disminuye contador de unidades
          var cantU = Number(cantUnid) - 1;
          cantUnid = cantU;
          cantSU.pop();
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
  
  
  
}
.texto_input{
  background-color: #ffffffde;
  height: 20px;
  font-size: 18px;
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
  background: #ea7500;
  block-size: 40px;
  font-size: 16px;
  margin-left: 20px;
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

.botonesUP{
   position:fixed;  
    font-family:verdana,arial;  
            font-size:11pt;  
            text-align:left;  
            top: 60px;                    /* Distancia hasta el borde superior */  
            left: 350px;            /* Distancia hasta el borde izquierdo */ 
            width:800px;  
           /* background-color:#ea7500e3;  */
        z-index: 1;             /* hace que la capa sea opaca  */  
}

.content-box-top2 { 
background-color: #002f6c;
position:fixed;  
font-family:verdana,arial;  
        font-size:11pt;  
        text-align:left;  
        top: 0px;                    /* Distancia hasta el borde superior */  
        left: 0px;            /* Distancia hasta el borde izquierdo */ 
        z-index: 1;
        width: 1310px;
    margin: 0 0 25px;
    overflow: hidden;
    padding: 21px;
    color: #b1b1b1;
}


</style>
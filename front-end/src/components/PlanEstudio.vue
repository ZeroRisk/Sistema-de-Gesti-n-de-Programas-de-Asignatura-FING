<template>
<div class="main_file" id="main_file">
 
<div id='cssmenu' >
<ul>


 
    <li >
 
      <router-link :to="{ name: 'HomeAdmin', params: { user: user , type: type }}">
 
      <a><span>Home</span></a>
 
      </router-link>
 
      </li>
 
   <li>
 
     <router-link :to="{ name: 'MenuPrograma', params: { user: user , type: type}  }">
 
       <a ><span>Editar Programa</span></a>
 
       </router-link>
 
     </li>
 
    <li  class='active has-sub'>
 
      <router-link :to="{ name: 'PlanEstudio', params: { user: user , type: type}  }">
 
        <a><span>Crear Plan de Estudio</span></a>
 
        </router-link>
 
        </li>
    <li> 
      <router-link :to="{ name: 'BuscarPorFechaAdmin', params: { user: user , type: type }}">
 
         <a><span>Buscar por Fecha/Asignatura</span></a>
 
        </router-link>
     </li> 
 
</ul>

</div>

<div class="content-box-top">Bienvenido al portal.<a href="#/"><span class="cerrar">Cerrar sesión</span></a></div>
<div class="content-box-left"><img src="../assets/usach.png" height="100" width="200"></div>
<div class="content-box-down">Abajo.</div>

<div >

<table  class="tabla">
    <button class="botones" v-on:click="saveData">Guardar!</button>
    <button class="botones">Atras</button>
    
   
      
    <h4>1. PLAN DE ESTUDIO </h4>
    <table class="bloque1">
    
    <tr>
      <td>Resolución :</td>
      <td  class="texto_input" >
      <input type="text" id='resolucionP' ref="resolucion"/></td>
    </tr>
    <tr>
      <td>Fecha :</td>
      <td  >
      <input   type="date" id='fechaP' ref="fecha" name="fecha" step="1" min="2018-01-01" max="2030-12-31" value="2018-05-10">
      </td>
    </tr>
    <tr>
      <td>Departamento :</td>
      <td>
        <select id='deptoP'>
          <option value="Mecanica">Mecánica </option>
        </select>
      </td>
    </tr>
     <tr>
      <td>Carrera :</td>
      <td>
        <select id='carreraP' >
          <option value="Ingenieria Civil Mecanica">Ing. Civil Mecánica</option>
          <option value="Ingenieria Ejecucion Mecanica">Ing. Ejecución Mecánica</option>
          <option value="Ingenieria Ejecucion Climatizacion">Ing. Ejecución Climatización</option>
        </select>
      </td>
    </tr>
   </table>
</table>

</div>


 <div class="dinamic">
        <h4 >Asignaturas NIVEL 1 </h4>
        <div id="NIVEL1" >
        </div>
        <input type="button"  class="botones2" value="Agregar Asignatura" v-on:click="agregarAsignatura(1)" />
        <br>

        <h4 >Asignaturas NIVEL 2 </h4>
        <div id="NIVEL2" >
        </div>
        <input type="button" class="botones2" value="Agregar Asignatura" v-on:click="agregarAsignatura(2)" />
        <br>

        <h4 >Asignaturas NIVEL 3 </h4>
        <div id="NIVEL3" >
        </div>
        <input type="button" class="botones2" value="Agregar Asignatura" v-on:click="agregarAsignatura(3)" />
        <br>

        <h4 >Asignaturas NIVEL 4 </h4>
        <div id="NIVEL4" >
        </div>
        <input type="button" class="botones2" value="Agregar Asignatura" v-on:click="agregarAsignatura(4)" />
        <br>

        <h4 >Asignaturas NIVEL 5 </h4>
        <div id="NIVEL5" >
        </div>
        <input type="button" class="botones2" value="Agregar Asignatura" v-on:click="agregarAsignatura(5)" />
        <br>

        <h4 >Asignaturas NIVEL 6 </h4>
        <div id="NIVEL6" >
        </div>
        <input type="button" class="botones2" value="Agregar Asignatura" v-on:click="agregarAsignatura(6)" />
        <br>

        <h4 >Asignaturas NIVEL 7 </h4>
        <div id="NIVEL7" >
        </div>
        <input type="button" class="botones2" value="Agregar Asignatura" v-on:click="agregarAsignatura(7)" />
        <br>

        <h4 >Asignaturas NIVEL 8 </h4>
        <div id="NIVEL8" >
        </div>
        <input type="button" class="botones2" value="Agregar Asignatura" v-on:click="agregarAsignatura(8)" />
        <br>

        <h4 >Asignaturas NIVEL 9 </h4>
        <div id="NIVEL9" >
        </div>
        <input type="button" class="botones2" value="Agregar Asignatura" v-on:click="agregarAsignatura(9)" />
        <br>

        <h4 >Asignaturas NIVEL 10 </h4>
        <div id="NIVEL10" >
        </div>
        <input type="button" class="botones2" value="Agregar Asignatura" v-on:click="agregarAsignatura(10)" />
        <br>

        <h4 >Asignaturas NIVEL 11 </h4>
        <div id="NIVEL11" >
        </div>
        <input type="button" class="botones2" value="Agregar Asignatura" v-on:click="agregarAsignatura(11)" />
        <br>

        <h4 >Asignaturas NIVEL 12 </h4>
        <div id="NIVEL12" >
        </div>
        <input type="button" class="botones2" value="Agregar Asignatura" v-on:click="agregarAsignatura(12)" />
        <br>
        <br>
  </div>
</div>
</template>

<script>
var asign1=0;
var asign2=0;
var asign3=0;
var asign4=0;
var asign5=0;
var asign6=0;
var asign7=0;
var asign8=0;
var asign9=0;
var asign10=0;
var asign11=0;
var asign12=0;
var totalAsign=0;

var numeroAsignaturasTotal = 0;

var numeroAsignatura = 0;
var nivel = 1;

var conjuntoAsignaturas =[]; /** LISTA DE LISTAS DE ASIGNATURA */
var idAsignaturas = [];
var idCarrera = 0;
var idPlanfinal = 0;
var resolucion = "";
var estaListo=0;



export default {
    props: ['user','type'],
    data(){
      return{
        Asignaturas:[],
        isAdmin:false
      }
    },
    
    mounted: function(){
     console.log(this.type)
       if(this.type == "Admin"){
 
        this.isAdmin=true
 
      }
      asign1=0;
      asign2=0;
      asign3=0;
      asign4=0;
      asign5=0;
      asign6=0;
      asign7=0;
      asign8=0;
      asign9=0;
      asign10=0;
      asign11=0;
      asign12=0;
      totalAsign=0;

      numeroAsignaturasTotal = 0;

      numeroAsignatura = 0;
      nivel = 1;

      conjuntoAsignaturas =[]; /** LISTA DE LISTAS DE ASIGNATURA */
      idAsignaturas = [];
      idPlanfinal = 0;
      idCarrera = 0;
      resolucion = "";

      estaListo=0;
 
    },
    methods: {


    /** Añade a la pagina una tabla para agregar asignaturas
        Entrada : nivel de la asignatura
     */
    agregarAsignatura: function (num){
        
        if(num==1){numeroAsignaturasTotal=asign1;asign1=asign1+1;}
        else if(num==2){numeroAsignaturasTotal=asign2;asign2=asign2+1;}
        else if(num==3){numeroAsignaturasTotal=asign3;asign3=asign3+1;}
        else if(num==4){numeroAsignaturasTotal=asign4;asign4=asign4+1;}
        else if(num==5){numeroAsignaturasTotal=asign5;asign5=asign5+1;}
        else if(num==6){numeroAsignaturasTotal=asign6;asign6=asign6+1;}
        else if(num==7){numeroAsignaturasTotal=asign7;asign7=asign7+1;}
        else if(num==8){numeroAsignaturasTotal=asign8;asign8=asign8+1;}
        else if(num==9){numeroAsignaturasTotal=asign9;asign9=asign9+1;}
        else if(num==10){numeroAsignaturasTotal=asign10;asign10=asign10+1;}
        else if(num==11){numeroAsignaturasTotal=asign11;asign11=asign11+1;}
        else if(num==12){numeroAsignaturasTotal=asign12;asign12=asign12+1;}
        else{return}

      // Obtiene el div donde se agregara la tabla
        var div = document.getElementById("NIVEL"+num);
      // Se crea la tabla y sus elementos 
        var tabla   = document.createElement("table");
        var hilera = document.createElement("tr");
        var celda1 = document.createElement("th");
        var celda2 = document.createElement("td");
        var celda3 = document.createElement("th");
        var celda4 = document.createElement("th");
        var celda5 = document.createElement("th");
        var celda6 = document.createElement("th");
        var celda7 = document.createElement("td");
        var celda8 = document.createElement("td");
        var textoCelda1 = document.createTextNode("CODIGO ");
        var textoCelda2 = document.createTextNode("ASIGNATURA ");
        var textoCelda3 = document.createTextNode("T");
        var textoCelda4 = document.createTextNode("E");
        var textoCelda5 = document.createTextNode("L");
        var textoCelda6 = document.createTextNode("SCT");
        var textoCelda7 = document.createTextNode("Tipo");
        var textoCelda8 = document.createTextNode("REQUISITOS");
        celda1.appendChild(textoCelda1);
        celda2.appendChild(textoCelda2);
        celda3.appendChild(textoCelda3);
        celda4.appendChild(textoCelda4);
        celda5.appendChild(textoCelda5);
        celda6.appendChild(textoCelda6);
        celda7.appendChild(textoCelda7);
        celda8.appendChild(textoCelda8);
        hilera.appendChild(celda1);
        hilera.appendChild(celda2);
        hilera.appendChild(celda3);
        hilera.appendChild(celda4);
        hilera.appendChild(celda5);
        hilera.appendChild(celda6);
        hilera.appendChild(celda7);
        hilera.appendChild(celda8);
        tabla.appendChild(hilera);

        var hilera2 = document.createElement("tr");
        var celda9 = document.createElement("td");
        var celda10 = document.createElement("td");
        var celda11 = document.createElement("td");
        var celda12 = document.createElement("td");
        var celda13 = document.createElement("td");
        var celda14 = document.createElement("td");
        var celda15 = document.createElement("td");
        var celda16 = document.createElement("td");
        
        var inputCod = document.createElement("input");
        inputCod.setAttribute("id", "codigo_"+num+"_"+numeroAsignaturasTotal);
        inputCod.setAttribute("style","width:60px;");
        celda9.appendChild(inputCod);
        hilera2.appendChild(celda9);

        var inputName = document.createElement("input");
        inputName.setAttribute("id", "asignatura_"+num+"_"+numeroAsignaturasTotal);
        inputName.setAttribute("style","width:210px;");
        celda10.appendChild(inputName);
        hilera2.appendChild(celda10);
      
        var inputT = document.createElement("input");
        inputT.setAttribute("id", "T_"+num+"_"+numeroAsignaturasTotal);
        inputT.setAttribute("style","width:30px;");
        celda11.appendChild(inputT);
        hilera2.appendChild(celda11);
        
        var inputE = document.createElement("input");
        inputE.setAttribute("id", "E_"+num+"_"+numeroAsignaturasTotal);
        inputE.setAttribute("style","width:30px;");
        celda12.appendChild(inputE);
        hilera2.appendChild(celda12);

        var inputL = document.createElement("input");
        inputL.setAttribute("id", "L_"+num+"_"+numeroAsignaturasTotal);
        inputL.setAttribute("style","width:30px;");
        celda13.appendChild(inputL);
        hilera2.appendChild(celda13);

        var inputSCT = document.createElement("input");
        inputSCT.setAttribute("id", "SCT_"+num+"_"+numeroAsignaturasTotal);
        inputSCT.setAttribute("style","width:50px;");
        celda14.appendChild(inputSCT);
        hilera2.appendChild(celda14);

        // Crear elemento select
        var miSelect=document.createElement("select");
        miSelect.setAttribute("id","tipo_"+num+"_"+numeroAsignaturasTotal);
        // Añadimos opciones
        var miOption=document.createElement("option");
        miOption.setAttribute("value","AP");
        miOption.setAttribute("label","AP-Asignatura profesional");
        miSelect.appendChild(miOption);
        
        var miOption2=document.createElement("option");
        miOption2.setAttribute("value","CB");
        miOption2.setAttribute("label","CB-Ciencia básica");  
        miSelect.appendChild(miOption2);
        
        
        var miOption3=document.createElement("option");
        miOption3.setAttribute("value","CH");
        miOption3.setAttribute("label","CH-Ciencia Humana/Economía/Admin.");
        miSelect.appendChild(miOption3);

        var miOption4=document.createElement("option");
        miOption4.setAttribute("value","CI");
        miOption4.setAttribute("label","CI-Ciencia de la Ing.");
        miSelect.appendChild(miOption4);

        hilera2.appendChild(miSelect);

        var inputReq = document.createElement("input");
        inputReq.setAttribute("id", "requisitos_"+num+"_"+numeroAsignaturasTotal);
        inputReq.setAttribute("style","width:250px;");
        celda16.appendChild(inputReq);
        hilera2.appendChild(celda16);

        tabla.appendChild(hilera2);
        tabla.setAttribute("style","background:#1700ea3b;");
        var espacio = document.createElement("br");
        // Agrega la tabla al div
        div.appendChild(tabla);
        div.appendChild(espacio);
    },
    funcionfinal: function(){
        /** AQUI TERMINA TODO*/
        
        console.log("ID ADMIN: "+this.user.id)
        console.log("NOMBRE USER: "+this.user.username)
        console.log("DATOS DE LAS ASIGNATURAS: "+conjuntoAsignaturas)

        console.log("ID CARRERA DEL PLAN: "+idCarrera)
        console.log("RESOLUCION DEL PLAN: "+resolucion)

        this.$http.get('http://localhost:5000/planRiA?resolucion='+resolucion+'&idcarrera='+idCarrera).then(response=>{
            console.log("SE ENCONTRÓ PLAN!")
            console.log(response.body.plan)
            idPlanfinal = response.body.plan[0].idplan_estudio;
            estaListo=0;
            var aux=0;
            while(aux<totalAsign){
                console.log(conjuntoAsignaturas[aux])
                this.$http.get('http://localhost:5000/asignaturaCN?codigoAsig='+conjuntoAsignaturas[aux][0]+'&nombreAsig='+conjuntoAsignaturas[aux][1]+'&tipoAsig='+conjuntoAsignaturas[aux][5]).then(response=>{
                    console.log("Encontró la asignatura!")
                    console.log(response.body.asignatura[0])
                    idAsignaturas.push(response.body.asignatura[0].idasignatura)

                    estaListo=estaListo+1;
                    console.log("Esta listo?: "+estaListo)
                    if(estaListo==totalAsign){
                      console.log(idAsignaturas)
                      this.funcionInsertIntermedio()
                    }


                },response=>{
                    console.log("Fail al encontrar asignatura")
                });
                aux=aux+1;
            }


        },response=>{
            console.log("Fail encontrar plan")
        });


        


      },
      funcionInsertIntermedio: function(){
        console.log(idPlanfinal)
        console.log(idAsignaturas)
        var aux = 0;
        while(aux<totalAsign){
            idAsignaturas[aux]
            
            this.$http.post('http://localhost:5000/newPlanAsig',{"idplanasig":0,"idplan":idPlanfinal,"idasig":idAsignaturas[aux]}).then(response=>{
                console.log("Intermedio P-A!")
            },response=>{
                console.log("Fail P-A!")
            });





          aux=aux+1;

        }



      },
  
    /** Guarda el plan de estudio 
        PENDIENTE
        Don't worry, I got this ;)
     */
    saveData: function(){
        conjuntoAsignaturas =[]; /** RESETEO LISTAS DE ASIGNATURA */


        resolucion = document.getElementById("resolucionP").value;
        var fecha = document.getElementById("fechaP").value;
        var depto = document.getElementById("deptoP").value;
        var carrera = document.getElementById("carreraP").value;
        console.log(resolucion)
        console.log(fecha)
        console.log(depto)
        console.log(carrera)

        var fechaDescompuesta = fecha.split("-")

        
        console.log("ANO: "+fechaDescompuesta[0])
        console.log("MES: "+fechaDescompuesta[1])
        console.log("DIA: "+fechaDescompuesta[2])



        console.log("-------------------------------")       
        
        console.log("Numero asignaturas nivel 1: "+asign1)

        console.log("-------------------------------")

        numeroAsignatura = 0;

        while(numeroAsignatura<asign1){
          var listAux =[];

          var codigo = document.getElementById("codigo_1_"+numeroAsignatura).value;
          var asignatura = document.getElementById("asignatura_1_"+numeroAsignatura).value;
          var T = document.getElementById("T_1_"+numeroAsignatura).value;
          var E = document.getElementById("E_1_"+numeroAsignatura).value;
          var L = document.getElementById("L_1_"+numeroAsignatura).value;
          var tipo = document.getElementById("tipo_1_"+numeroAsignatura).value;
          var requisito = document.getElementById("requisitos_1_"+numeroAsignatura).value;

          console.log(codigo)
          console.log(asignatura)
          console.log(T)
          console.log(E)
          console.log(L)
          console.log(tipo)
          console.log(requisito)
          console.log("-------------------------------")

          listAux.push(codigo)
          listAux.push(asignatura)
          listAux.push(T)
          listAux.push(E)
          listAux.push(L)
          listAux.push(tipo)
          listAux.push(requisito)
          listAux.push("1") /** NIVEL*/

          console.log("ASIGNATURA CREADA: "+listAux)

          conjuntoAsignaturas.push(listAux)

          console.log("TODAS LAS ASIGNATURAS HASTA AHORA: "+conjuntoAsignaturas)

          numeroAsignatura = numeroAsignatura+1;
        }



        console.log("-------------------------------")       
        
        console.log("Numero asignaturas nivel 2: "+asign2)

        console.log("-------------------------------")
        
        numeroAsignatura = 0;

        while(numeroAsignatura<asign2){
          var listAux =[];

          var codigo = document.getElementById("codigo_2_"+numeroAsignatura).value;
          var asignatura = document.getElementById("asignatura_2_"+numeroAsignatura).value;
          var T = document.getElementById("T_2_"+numeroAsignatura).value;
          var E = document.getElementById("E_2_"+numeroAsignatura).value;
          var L = document.getElementById("L_2_"+numeroAsignatura).value;
          var tipo = document.getElementById("tipo_2_"+numeroAsignatura).value;
          var requisito = document.getElementById("requisitos_2_"+numeroAsignatura).value;

          console.log(codigo)
          console.log(asignatura)
          console.log(T)
          console.log(E)
          console.log(L)
          console.log(tipo)
          console.log(requisito)
          console.log("-------------------------------")

          listAux.push(codigo)
          listAux.push(asignatura)
          listAux.push(T)
          listAux.push(E)
          listAux.push(L)
          listAux.push(tipo)
          listAux.push(requisito)
          listAux.push("2") /** NIVEL*/

          console.log("ASIGNATURA CREADA: "+listAux)

          conjuntoAsignaturas.push(listAux)

          console.log("TODAS LAS ASIGNATURAS HASTA AHORA: "+conjuntoAsignaturas)

          numeroAsignatura = numeroAsignatura+1;
        }


        console.log("-------------------------------")       
        
        console.log("Numero asignaturas nivel 3: "+asign3)

        console.log("-------------------------------")
        
        numeroAsignatura = 0;

        while(numeroAsignatura<asign3){
          var listAux =[];

          var codigo = document.getElementById("codigo_3_"+numeroAsignatura).value;
          var asignatura = document.getElementById("asignatura_3_"+numeroAsignatura).value;
          var T = document.getElementById("T_3_"+numeroAsignatura).value;
          var E = document.getElementById("E_3_"+numeroAsignatura).value;
          var L = document.getElementById("L_3_"+numeroAsignatura).value;
          var tipo = document.getElementById("tipo_3_"+numeroAsignatura).value;
          var requisito = document.getElementById("requisitos_3_"+numeroAsignatura).value;

          console.log(codigo)
          console.log(asignatura)
          console.log(T)
          console.log(E)
          console.log(L)
          console.log(tipo)
          console.log(requisito)
          console.log("-------------------------------")

          listAux.push(codigo)
          listAux.push(asignatura)
          listAux.push(T)
          listAux.push(E)
          listAux.push(L)
          listAux.push(tipo)
          listAux.push(requisito)
          listAux.push("3") /** NIVEL*/

          console.log("ASIGNATURA CREADA: "+listAux)

          conjuntoAsignaturas.push(listAux)

          console.log("TODAS LAS ASIGNATURAS HASTA AHORA: "+conjuntoAsignaturas)

          numeroAsignatura = numeroAsignatura+1;
        }


        console.log("-------------------------------")       
        
        console.log("Numero asignaturas nivel 4: "+asign4)

        console.log("-------------------------------")
        
        numeroAsignatura = 0;

        while(numeroAsignatura<asign4){
          var listAux =[];

          var codigo = document.getElementById("codigo_4_"+numeroAsignatura).value;
          var asignatura = document.getElementById("asignatura_4_"+numeroAsignatura).value;
          var T = document.getElementById("T_4_"+numeroAsignatura).value;
          var E = document.getElementById("E_4_"+numeroAsignatura).value;
          var L = document.getElementById("L_4_"+numeroAsignatura).value;
          var tipo = document.getElementById("tipo_4_"+numeroAsignatura).value;
          var requisito = document.getElementById("requisitos_4_"+numeroAsignatura).value;

          console.log(codigo)
          console.log(asignatura)
          console.log(T)
          console.log(E)
          console.log(L)
          console.log(tipo)
          console.log(requisito)
          console.log("-------------------------------")

          listAux.push(codigo)
          listAux.push(asignatura)
          listAux.push(T)
          listAux.push(E)
          listAux.push(L)
          listAux.push(tipo)
          listAux.push(requisito)
          listAux.push("4") /** NIVEL*/

          console.log("ASIGNATURA CREADA: "+listAux)

          conjuntoAsignaturas.push(listAux)

          console.log("TODAS LAS ASIGNATURAS HASTA AHORA: "+conjuntoAsignaturas)

          numeroAsignatura = numeroAsignatura+1;
        }

        console.log("-------------------------------")       
        
        console.log("Numero asignaturas nivel 5: "+asign5)

        console.log("-------------------------------")
        
        numeroAsignatura = 0;

        while(numeroAsignatura<asign5){
          var listAux =[];

          var codigo = document.getElementById("codigo_5_"+numeroAsignatura).value;
          var asignatura = document.getElementById("asignatura_5_"+numeroAsignatura).value;
          var T = document.getElementById("T_5_"+numeroAsignatura).value;
          var E = document.getElementById("E_5_"+numeroAsignatura).value;
          var L = document.getElementById("L_5_"+numeroAsignatura).value;
          var tipo = document.getElementById("tipo_5_"+numeroAsignatura).value;
          var requisito = document.getElementById("requisitos_5_"+numeroAsignatura).value;

          console.log(codigo)
          console.log(asignatura)
          console.log(T)
          console.log(E)
          console.log(L)
          console.log(tipo)
          console.log(requisito)
          console.log("-------------------------------")

          listAux.push(codigo)
          listAux.push(asignatura)
          listAux.push(T)
          listAux.push(E)
          listAux.push(L)
          listAux.push(tipo)
          listAux.push(requisito)
          listAux.push("5") /** NIVEL*/

          console.log("ASIGNATURA CREADA: "+listAux)

          conjuntoAsignaturas.push(listAux)

          console.log("TODAS LAS ASIGNATURAS HASTA AHORA: "+conjuntoAsignaturas)

          numeroAsignatura = numeroAsignatura+1;
        }


        console.log("-------------------------------")       
        
        console.log("Numero asignaturas nivel 6: "+asign6)

        console.log("-------------------------------")
        
        numeroAsignatura = 0;

        while(numeroAsignatura<asign6){
          var listAux =[];

          var codigo = document.getElementById("codigo_6_"+numeroAsignatura).value;
          var asignatura = document.getElementById("asignatura_6_"+numeroAsignatura).value;
          var T = document.getElementById("T_6_"+numeroAsignatura).value;
          var E = document.getElementById("E_6_"+numeroAsignatura).value;
          var L = document.getElementById("L_6_"+numeroAsignatura).value;
          var tipo = document.getElementById("tipo_6_"+numeroAsignatura).value;
          var requisito = document.getElementById("requisitos_6_"+numeroAsignatura).value;

          console.log(codigo)
          console.log(asignatura)
          console.log(T)
          console.log(E)
          console.log(L)
          console.log(tipo)
          console.log(requisito)
          console.log("-------------------------------")

          listAux.push(codigo)
          listAux.push(asignatura)
          listAux.push(T)
          listAux.push(E)
          listAux.push(L)
          listAux.push(tipo)
          listAux.push(requisito)
          listAux.push("6") /** NIVEL*/

          console.log("ASIGNATURA CREADA: "+listAux)

          conjuntoAsignaturas.push(listAux)

          console.log("TODAS LAS ASIGNATURAS HASTA AHORA: "+conjuntoAsignaturas)

          numeroAsignatura = numeroAsignatura+1;
        }


        console.log("-------------------------------")       
        
        console.log("Numero asignaturas nivel 7: "+asign7)

        console.log("-------------------------------")
        
        numeroAsignatura = 0;

        while(numeroAsignatura<asign7){
          var listAux =[];

          var codigo = document.getElementById("codigo_7_"+numeroAsignatura).value;
          var asignatura = document.getElementById("asignatura_7_"+numeroAsignatura).value;
          var T = document.getElementById("T_7_"+numeroAsignatura).value;
          var E = document.getElementById("E_7_"+numeroAsignatura).value;
          var L = document.getElementById("L_7_"+numeroAsignatura).value;
          var tipo = document.getElementById("tipo_7_"+numeroAsignatura).value;
          var requisito = document.getElementById("requisitos_7_"+numeroAsignatura).value;

          console.log(codigo)
          console.log(asignatura)
          console.log(T)
          console.log(E)
          console.log(L)
          console.log(tipo)
          console.log(requisito)
          console.log("-------------------------------")

          listAux.push(codigo)
          listAux.push(asignatura)
          listAux.push(T)
          listAux.push(E)
          listAux.push(L)
          listAux.push(tipo)
          listAux.push(requisito)
          listAux.push("7") /** NIVEL*/

          console.log("ASIGNATURA CREADA: "+listAux)

          conjuntoAsignaturas.push(listAux)

          console.log("TODAS LAS ASIGNATURAS HASTA AHORA: "+conjuntoAsignaturas)

          numeroAsignatura = numeroAsignatura+1;
        }


        console.log("-------------------------------")       
        
        console.log("Numero asignaturas nivel 8: "+asign8)

        console.log("-------------------------------")
        
        numeroAsignatura = 0;

        while(numeroAsignatura<asign8){
          var listAux =[];

          var codigo = document.getElementById("codigo_8_"+numeroAsignatura).value;
          var asignatura = document.getElementById("asignatura_8_"+numeroAsignatura).value;
          var T = document.getElementById("T_8_"+numeroAsignatura).value;
          var E = document.getElementById("E_8_"+numeroAsignatura).value;
          var L = document.getElementById("L_8_"+numeroAsignatura).value;
          var tipo = document.getElementById("tipo_8_"+numeroAsignatura).value;
          var requisito = document.getElementById("requisitos_8_"+numeroAsignatura).value;

          console.log(codigo)
          console.log(asignatura)
          console.log(T)
          console.log(E)
          console.log(L)
          console.log(tipo)
          console.log(requisito)
          console.log("-------------------------------")

          listAux.push(codigo)
          listAux.push(asignatura)
          listAux.push(T)
          listAux.push(E)
          listAux.push(L)
          listAux.push(tipo)
          listAux.push(requisito)
          listAux.push("8") /** NIVEL*/

          console.log("ASIGNATURA CREADA: "+listAux)

          conjuntoAsignaturas.push(listAux)

          console.log("TODAS LAS ASIGNATURAS HASTA AHORA: "+conjuntoAsignaturas)

          numeroAsignatura = numeroAsignatura+1;
        }


        console.log("-------------------------------")       
        
        console.log("Numero asignaturas nivel 9: "+asign9)

        console.log("-------------------------------")
        
        numeroAsignatura = 0;

        while(numeroAsignatura<asign9){
          var listAux =[];

          var codigo = document.getElementById("codigo_9_"+numeroAsignatura).value;
          var asignatura = document.getElementById("asignatura_9_"+numeroAsignatura).value;
          var T = document.getElementById("T_9_"+numeroAsignatura).value;
          var E = document.getElementById("E_9_"+numeroAsignatura).value;
          var L = document.getElementById("L_9_"+numeroAsignatura).value;
          var tipo = document.getElementById("tipo_9_"+numeroAsignatura).value;
          var requisito = document.getElementById("requisitos_9_"+numeroAsignatura).value;

          console.log(codigo)
          console.log(asignatura)
          console.log(T)
          console.log(E)
          console.log(L)
          console.log(tipo)
          console.log(requisito)
          console.log("-------------------------------")

          listAux.push(codigo)
          listAux.push(asignatura)
          listAux.push(T)
          listAux.push(E)
          listAux.push(L)
          listAux.push(tipo)
          listAux.push(requisito)
          listAux.push("9") /** NIVEL*/

          console.log("ASIGNATURA CREADA: "+listAux)

          conjuntoAsignaturas.push(listAux)

          console.log("TODAS LAS ASIGNATURAS HASTA AHORA: "+conjuntoAsignaturas)

          numeroAsignatura = numeroAsignatura+1;
        }


        console.log("-------------------------------")       
        
        console.log("Numero asignaturas nivel 10: "+asign10)

        console.log("-------------------------------")
        
        numeroAsignatura = 0;

        while(numeroAsignatura<asign10){
          var listAux =[];

          var codigo = document.getElementById("codigo_10_"+numeroAsignatura).value;
          var asignatura = document.getElementById("asignatura_10_"+numeroAsignatura).value;
          var T = document.getElementById("T_10_"+numeroAsignatura).value;
          var E = document.getElementById("E_10_"+numeroAsignatura).value;
          var L = document.getElementById("L_10_"+numeroAsignatura).value;
          var tipo = document.getElementById("tipo_10_"+numeroAsignatura).value;
          var requisito = document.getElementById("requisitos_10_"+numeroAsignatura).value;

          console.log(codigo)
          console.log(asignatura)
          console.log(T)
          console.log(E)
          console.log(L)
          console.log(tipo)
          console.log(requisito)
          console.log("-------------------------------")

          listAux.push(codigo)
          listAux.push(asignatura)
          listAux.push(T)
          listAux.push(E)
          listAux.push(L)
          listAux.push(tipo)
          listAux.push(requisito)
          listAux.push("10") /** NIVEL*/

          console.log("ASIGNATURA CREADA: "+listAux)

          conjuntoAsignaturas.push(listAux)

          console.log("TODAS LAS ASIGNATURAS HASTA AHORA: "+conjuntoAsignaturas)

          numeroAsignatura = numeroAsignatura+1;
        }


        console.log("-------------------------------")       
        
        console.log("Numero asignaturas nivel 11: "+asign11)

        console.log("-------------------------------")
        
        numeroAsignatura = 0;

        while(numeroAsignatura<asign11){
          var listAux =[];

          var codigo = document.getElementById("codigo_11_"+numeroAsignatura).value;
          var asignatura = document.getElementById("asignatura_11_"+numeroAsignatura).value;
          var T = document.getElementById("T_11_"+numeroAsignatura).value;
          var E = document.getElementById("E_11_"+numeroAsignatura).value;
          var L = document.getElementById("L_11_"+numeroAsignatura).value;
          var tipo = document.getElementById("tipo_11_"+numeroAsignatura).value;
          var requisito = document.getElementById("requisitos_11_"+numeroAsignatura).value;

          console.log(codigo)
          console.log(asignatura)
          console.log(T)
          console.log(E)
          console.log(L)
          console.log(tipo)
          console.log(requisito)
          console.log("-------------------------------")

          listAux.push(codigo)
          listAux.push(asignatura)
          listAux.push(T)
          listAux.push(E)
          listAux.push(L)
          listAux.push(tipo)
          listAux.push(requisito)
          listAux.push("11") /** NIVEL*/

          console.log("ASIGNATURA CREADA: "+listAux)

          conjuntoAsignaturas.push(listAux)

          console.log("TODAS LAS ASIGNATURAS HASTA AHORA: "+conjuntoAsignaturas)

          numeroAsignatura = numeroAsignatura+1;
        }


        console.log("-------------------------------")       
        
        console.log("Numero asignaturas nivel 12: "+asign12)

        console.log("-------------------------------")
        
        numeroAsignatura = 0;

        while(numeroAsignatura<asign12){
          var listAux =[];

          var codigo = document.getElementById("codigo_12_"+numeroAsignatura).value;
          var asignatura = document.getElementById("asignatura_12_"+numeroAsignatura).value;
          var T = document.getElementById("T_12_"+numeroAsignatura).value;
          var E = document.getElementById("E_12_"+numeroAsignatura).value;
          var L = document.getElementById("L_12_"+numeroAsignatura).value;
          var tipo = document.getElementById("tipo_12_"+numeroAsignatura).value;
          var requisito = document.getElementById("requisitos_12_"+numeroAsignatura).value;

          console.log(codigo)
          console.log(asignatura)
          console.log(T)
          console.log(E)
          console.log(L)
          console.log(tipo)
          console.log(requisito)
          console.log("-------------------------------")

          listAux.push(codigo)
          listAux.push(asignatura)
          listAux.push(T)
          listAux.push(E)
          listAux.push(L)
          listAux.push(tipo)
          listAux.push(requisito)
          listAux.push("12") /** NIVEL*/

          console.log("ASIGNATURA CREADA: "+listAux)

          conjuntoAsignaturas.push(listAux)

          console.log("TODAS LAS ASIGNATURAS HASTA AHORA: "+conjuntoAsignaturas)

          numeroAsignatura = numeroAsignatura+1;
        }

        totalAsign=asign1+asign2+asign3+asign4+asign5+asign6+asign7+asign8+asign9+asign10+asign11+asign12;
        console.log("Total asignaturas del plan: "+totalAsign)



        /** COMIENZA EL INSERTAR PLAN Y ASIGNATURAS */

        this.$http.get('http://localhost:5000/carreraN?nombrecarrera='+carrera).then(response=>{
              console.log("Get carrera exitoso!")
              console.log(response.body.carrera[0].idcarrera)

              idCarrera = response.body.carrera[0].idcarrera;

              this.$http.post('http://localhost:5000/newPlan',{"idplan":0,"idadmin":this.user.id,"resolu":resolucion,"fechadia":fechaDescompuesta[2],"fechames":fechaDescompuesta[1],"fechaano":fechaDescompuesta[0],"idcarrera":idCarrera}).then(response=>{
                    console.log("PLAN INGRESADO CORRECTAMENTE")
                    estaListo = 0;
                    var aux = 0;
                    
                    while(aux<totalAsign){
                        console.log(conjuntoAsignaturas[aux])

                        this.$http.post('http://localhost:5000/newAsignatura',{"idasignatura":0,"codigoasignatura":conjuntoAsignaturas[aux][0],"nombreasignatura":conjuntoAsignaturas[aux][1],"horasT":conjuntoAsignaturas[aux][2],"horasE":conjuntoAsignaturas[aux][3],"horasL":conjuntoAsignaturas[aux][4],"sct":conjuntoAsignaturas[aux][4],"tipo":conjuntoAsignaturas[aux][5],"requisitos":conjuntoAsignaturas[aux][6],"nivel":conjuntoAsignaturas[aux][7]}).then(response=>{
                              console.log("INSERT ASIGNATURA EXITOSO!")
                              estaListo=estaListo+1;
                              console.log("Esta listo?: "+estaListo)
                              if(estaListo==totalAsign){this.funcionfinal()}
                              
                        },response=>{
                              console.log("Fail insert asginatura")
                        });

                      

                      aux = aux+1;


                    }
                    

              },response=>{
                    console.log("Fail ingresar plan")
              });






        },response=>{
            console.log("Fail get carrera!")
          });


    }

    }
}
</script>

<style >
@import '../fondo.css';

.dinamic {
    position: relative; top: 100px; left: 250px;
    width: 1000px;
    background:#cdd1f8cc;
}

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

.dinamicos {
    position:relative; top:100px; left: 350px; 
    
}

.tablas_dinamicas {
   background-color: #002f6c21;
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
  position: relative; left: 40px;
  border-radius: 5px 10px 5px 10px;
  color: #e6e3e3;
  font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}
</style>

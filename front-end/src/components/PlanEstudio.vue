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
    <button class="botones" v-on:click="saveData">Guardar</button>
    <button class="botones">Atras</button>
    
   
      
    <h4>1. PLAN DE ESTUDIO </h4>
    <table class="bloque1">
    
    <tr>
      <td>Resolución :</td>
      <td  class="texto_input" >
      <input type="text" ref="resolucion"/></td>
    </tr>
    <tr>
      <td>Fecha :</td>
      <td  >
      <input   type="date"  ref="fecha" name="fecha" step="1" min="2018-01-01" max="2030-12-31" value="2018-05-10">
      </td>
    </tr>
    <tr>
      <td>Departamento :</td>
      <td>
        <select>
          <option value="volvo">Mecánica </option>
        </select>
      </td>
    </tr>
     <tr>
      <td>Carrera :</td>
      <td>
        <select id="carrera" >
          <option value="1">Ing. Civil Mecánica</option>
          <option value="2">Ing. Ejecución Mecánica</option>
          <option value="3">Ing. Ejecución Climatización</option>
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
 
    },
    methods: {


    /** Añade a la pagina una tabla para agregar asignaturas
        Entrada : nivel de la asignatura
     */
    agregarAsignatura: function (num){
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
        inputCod.setAttribute("id", "codigo_"+num);
        inputCod.setAttribute("style","width:60px;");
        celda9.appendChild(inputCod);
        hilera2.appendChild(celda9);

        var inputName = document.createElement("input");
        inputName.setAttribute("id", "asignatura_"+num);
        inputName.setAttribute("style","width:210px;");
        celda10.appendChild(inputName);
        hilera2.appendChild(celda10);
      
        var inputT = document.createElement("input");
        inputT.setAttribute("id", "T_"+num);
        inputT.setAttribute("style","width:30px;");
        celda11.appendChild(inputT);
        hilera2.appendChild(celda11);
        
        var inputE = document.createElement("input");
        inputE.setAttribute("id", "E_"+num);
        inputE.setAttribute("style","width:30px;");
        celda12.appendChild(inputE);
        hilera2.appendChild(celda12);

        var inputL = document.createElement("input");
        inputL.setAttribute("id", "L_"+num);
        inputL.setAttribute("style","width:30px;");
        celda13.appendChild(inputL);
        hilera2.appendChild(celda13);

        var inputSCT = document.createElement("input");
        inputSCT.setAttribute("id", "SCT_"+num);
        inputSCT.setAttribute("style","width:50px;");
        celda14.appendChild(inputSCT);
        hilera2.appendChild(celda14);

        // Crear elemento select
        var miSelect=document.createElement("select");
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
        inputReq.setAttribute("id", "requisitos_"+num);
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
  
    /** Guarda el plan de estudio 
        PENDIENTE
     */
    saveData: function(event){
        

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

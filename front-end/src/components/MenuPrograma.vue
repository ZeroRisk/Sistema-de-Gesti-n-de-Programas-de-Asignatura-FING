<template>
    <div>
        <div id='cssmenu' >
                <ul>
                    
                    <li  > 
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
                
                    <li > 
                    <router-link :to="{ name: 'BuscarPorFechaAdmin', params: { user: user , type: type }}"> 
                    <a><span>Buscar por Fecha/Asignatura</span></a> 
                    </router-link> 
                    </li> 

            </ul>

        </div>

            <div class="content-box-top">Bienvenido al portal.<a href="#/"><span class="cerrar">Cerrar sesión</span></a></div>
            <div class="content-box-left"><img src="../assets/usach.png" height="100" width="200"></div>
            <div class="content-box-down">Abajo.</div>
        
        <table  class="tabla">
            
            
            <h4>Seleccionar Programa de asignatura </h4>
            <table class="bloque1">
                <tr>
                <td>Carrera :</td>
                <td>
                    <select id="carrera"  >
                        <option value="1">Ing. Civil Mecánica</option>
                        <option value="2">Ing. Ejecución Mecánica</option>
                        <option value="3">Ing. Ejecución Climatización</option>
                    </select>
                </td>
                <td>
                   <button class="botonesOtros" v-on:click="buscarRes()">Buscar Plan</button> 
                </td>
                </tr>
                <tr>
                <td>Resolución :</td>
                <td>
                    <!-- 
                    con v-for se itera sobre la varible planes y se guardan los valores en plan
                    
                    -->
                    <select  id="resolucion">
                        <option  v-for="plan in planes" :value="plan.idplan_estudio">{{plan.resolucion}}</option>
                    </select>
                </td>
                <td>
                   <button  id="botonRes" class="botonesOtros" v-on:click="obtenerAsignaturas()" disabled="true">Buscar Asignaturas</button> 
                </td>
                </tr>
                <tr>
                <td>Asignatura :</td>
                <td>
                    <!-- 
                    con v-for se itera sobre la varible asignaturas y se guardan los valores en asig
                    
                    -->
                    <select  id="asignatura">
                        <option  v-for="asig in asignaturas" :value="asig.idasignatura">{{asig.nombreAsignatura}}</option>
                    </select>
                </td>
                </tr>
            </table>
               
                    <button id="enviar" class="botones" v-on:click="saveData" disabled="true">Aceptar</button>
              
            
        </table>
    </div>
</template>

<script>
import router from '../index'
export default {
    props: ['user','type'],
     data() {
        return {
             planes :[],
             asignaturas :[],
             idResol:0,
             idAsigna:0,
             idCarrera:0

        }
    },
     mounted: function (){ 
       if(this.type == "Admin"){
 
        this.isAdmin=true
 
      }
  }, 
    methods: {

        /** Funcion que busca un plan dependiendo de la carrera seleccionada
            Guarda el resultado en planes
         */
        buscarRes: function(){
            var combo = document.getElementById('carrera');
            var carrera = combo.options[combo.selectedIndex].value 
            //console.log("carrera seleccionada "+carrera);
            this.$http.get('http://localhost:5000/plancarrera?id_carrera='+carrera)
        .then(response =>{
            this.planes = response.body.plan
            //console.log(this.planes)
            if(this.planes.length==0){
                alert("No existen planes para esta carrera");
                var boton = document.getElementById("botonRes");
                boton.disabled = true;
                this.asignaturas=[];
            }
            else{
                // Se activa el boton para seguir con la seleccion de programa
                var boton = document.getElementById("botonRes");
                boton.disabled = false;
            }
            
            
            }, response =>{
                console.log("falla")
            });    
        },

        /** Funcion que recupera los datos seleccionados y los envia a la pagina programManage 
            donde se carga el programa seleccionado
         */
        saveData: function(){
            var comboRes = document.getElementById('resolucion');
            var resol = comboRes.options[comboRes.selectedIndex].value  
            var comboAsig = document.getElementById('asignatura');
            var asig = comboAsig.options[comboAsig.selectedIndex].value
            var comboCarrera = document.getElementById('carrera');
            var carrera = comboAsig.options[comboAsig.selectedIndex].value
            if(Number(carrera)==1){
                    this.idCarrera="Ing. Civil Mecánica";
            }
            else if (Number(carrera)==2){
                    this.idCarrera="Ing. Ejecución Mecánica";
            }
            else{
                    this.idCarrera="Ing. Ejecución Climatización";
            }
            
            this.idAsigna = asig;
            this.idResol= resol;
            //console.log("datos a enviar res "+this.idResol+ " y asignatura "+this.idAsigna);
            //  Envia datos a la pagina de edicion de programa
            this.$router.push({ name: 'programManage', params: { user: this.user , type: this.type, idRes: this.idResol, idAsig: this.idAsigna , idCarrera: this.idCarrera}})
        },

        /** Funcion que obtiene las asignaturas de la resolucion seleccionada
            Guarda los datos en asignaturas
         */
        obtenerAsignaturas: function(){
            var combo = document.getElementById('resolucion');
            var resol = combo.options[combo.selectedIndex].value 
            //console.log("resol seleccionada "+resol);
            this.$http.get('http://localhost:5000/asignaturaplan?id_plan='+resol)
        .then(response =>{
            this.asignaturas = response.body.asignaturas
            console.log(this.asignaturas)
                if(this.asignaturas.length==0){
                    alert("No existen asignaturas para este plan");
                    var boton = document.getElementById("enviar");
                     boton.disabled = true;
                }
                else
                {
                     var boton = document.getElementById("enviar");
                     boton.disabled = false;
                }
            }, response =>{
                console.log("falla ")
            });
        }
    }
}
</script>

<style>
@import '../fondo.css';

.tabla1 , th, td {
    border: 0px solid #1700ea3b;
    height: 0px;
  
}
.texto_input{
  background-color: #ffffff48;
  
}
.tabla{ 
    position:relative; top:80px; left: 350px; 
    font-size: 18px;
  }

.bloque1 {
  background-color: #002f6c21;
  padding: 10px;
  
}

.botones {
  background: #ea7500e3;
  block-size: 35px;
  font-size: 16px;
  margin-left: 20px;
  position: relative; left: 200px;
  border-radius: 5px 10px 5px 10px;
  color: #e6e3e3;
  font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.botonesOtros {
  background: #ea7500e3;
  block-size: 25px;
  font-size: 16px;
  margin-left: 20px;
  border-radius: 5px 10px 5px 10px;
  color: #fff8f8;
  font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}
</style>

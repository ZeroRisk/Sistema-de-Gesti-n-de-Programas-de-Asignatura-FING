<template>

<div class="main_class">

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
    <li  class='active has-sub'>
      <router-link :to="{ name: 'verPrograma', params: { user: user , type: type}  }">
        <a><span>ver programas asignados</span></a>
        </router-link>
        </li>

   <li>
     <router-link :to="{ name: 'BuscarPorFecha', params: { user: user , type: type }}">
     <a><span>Buscar por Fecha/Asignatura</span></a>
     </router-link>
     </li>
</ul>

</div>

<div class="content-box-top">Bienvenido al portal.<a href="#/"><span class="cerrar">Cerrar sesión</span></a></div>
<div class="content-box-left"><img src="../assets/usach.png" height="100" width="200"></div>
<div class="content-box-down">Abajo.</div>

<div class="centro">
    </h3>Seleccione uno de los programas asignados</h3>
    </h3>para obtener mas detalles</h3>
    <input class="botonesOtros" type="button" id="boton" value="Ver" v-on:click="verPrograma"/>
    <div v-for="program in programs">
      <table class="tabla1" width=1500>
          <td>
            <th>
              <input type="radio" name="radP" value=programa.idprograma v-on:click="actualizaValor(program.idprograma)">
            </th> 
          </td>
          <td> 
              <tr>Nombre :</tr>
              <tr>Departamento :</tr>
              <tr>Fecha creacion  :</tr>
          </td>
          <td>                     
            <tr>{{program.nameprograma}}</tr>
            <tr>{{program.deptoprograma}}</tr>
            <tr>{{program.fechacreacion}}</tr>         
          </td>        
       </table>
    </div>
    
</div>


</div>
</template>

<script>
export default {
    props: ['user','type'],
    data() {
        return {
            isAdmin:true,
            programs:[],
            valor:0
        }
    
    },
    mounted: function (){
      if(this.type != "Admin"){
        this.isAdmin=false
      }
      this.$http.get('http://localhost:5000/getAsignedPrograms?userid='+ this.user.id)
      .then(response =>{
        this.programs = response.body.programs
        console.log("entre a programas")
        console.log(this.programs)
      }, response =>{
        console.log("falle :c ")
      });
    },
    methods: {
       actualizaValor: function(oRad){
        this.valor = oRad;
        console.log("Se cambió valor a :"+this.valor)
      },
      programaSeleccionado: function(idSelected){
        var programRetornado = []
        for(var i =0 ; i < this.programs.length ; i++){
          console.log("iteracion numero " + i)
          console.log(this.programs[i].idprograma)
          if(this.programs[i].idprograma == idSelected){
            console.log("encontre el programa a pasar")
            programRetornado = this.programs[i]
          }
        }
        return programRetornado
      },
      verPrograma: function(){
        if(this.valor==0){
          alert("Debe seleccionar el programa que desee visualizar")
        }
        else{
          var selectedProgram = this.programaSeleccionado(this.valor)
          console.log(selectedProgram.nameprograma)
          this.$router.push({name:'progamAsigned', params:{user:this.user , type:this.typeUser , Programa: selectedProgram } })
        }
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
.centro{ 
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
  block-size: 36px;
  font-size: 20px;
  margin-left: 20px;
  border-radius: 5px 10px 5px 10px;
  position: relative; left:200px;
  color: #fff8f8;
  font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}
</style>
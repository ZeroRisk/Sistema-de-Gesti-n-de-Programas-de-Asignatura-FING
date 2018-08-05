<template>
    <div>
        <div id='cssmenu' >
            <ul>
              <li> 
                <router-link :to="{ name: 'HomeAdmin', params: { user: user , type: type }}"> 
                <a><span>Home</span></a> 
                </router-link> 
                </li> 
            <li> 
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
        

         <div class="res">

            
              <div class="tituloUser">
              <h3>Seleccione Usuario</h3>        
              </div>
              <!-- 
                    con v-for se obtienen los datos de los usuarios
                    
              -->
              <ul v-for="usuario in Usuarios">
                <table class="tabla11" width=900>
                    
                    <td>
                     
                      <tr>
                      <input class="bot" type="button" id="boton" value="Asignar" v-on:click="asignacion"/>
                      </tr>
                    </td>

                  <td>
                    <th>

                      <input type="radio" name="rad" value=usuario.idusuario v-on:click="actualizaValor(usuario.idusuario)" checked>
                    </th>
                  </td> 
                  <td>
                    <tr>Nombre :</tr>
                    <tr>Correo :</tr>
                    <tr>Cargo  :</tr>
                     
                  </td>
                  <td>
                      
                    <tr>{{usuario.nameusuario}}</tr>
                    <tr>{{usuario.correoUsuario}}</tr>
                    <tr>{{usuario.cargousuario}}</tr>
                     
                  </td>
                  
                </table>
              <br>
              <br>
              </ul>
              <div class="tituloProg">
              <h3>Seleccione Programa</h3>        
              </div>
              <!-- 
                    con v-for se itera sobre la varible Programas
                    
              -->
              <ul v-for="programa in Programas">
                <table class="tabla2" width=900>
                  
                  
                    <td>
                      <input  class="bot"  type="button" id="boton" value="Asignar" v-on:click="asignacion"/>
                    </td>

                  <td>
                    <th>
                      <input type="radio" name="radP" value=programa.idprograma v-on:click="actualizaValorP(programa.idprograma)" checked>
                    </th> 
                  </td>
                  <td> 
                    <tr>Nombre :</tr>
                    <tr>Departamento :</tr>
                    <tr>Fecha creacion  :</tr>
                     
                  </td>
                  <td>
                      
                    <tr>{{programa.nameprograma}}</tr>
                    <tr>{{programa.deptoprograma}}</tr>
                    <tr>{{programa.fechacreacion}}</tr>
                     
                  </td>
                  
                </table>
              <br>
              <br>
              </ul>


        </div>


    </div>








</template>

<script>

// Variables globales
var usersAsign = 0;
var programsAsign = 0;
var valor = 0;
var valorP = 0;
export default {
    methods: {
      // Funciones para actualizar el valor del radio
      actualizaValor: function(oRad){
        valor = oRad;
        //console.log("Se cambió valor a :"+valor)
      },
      actualizaValorP: function(pRad){
        valorP = pRad;
        //console.log("Se cambió valor a :"+valorP)
      },

      /** Asigna un programa seleccionado a un usuario
       */
      asignacion: function(){
        //console.log("Se comienza la asignación del user con id :"+valor+", y el programa de id: "+valorP)
        if(valor==0 || valorP==0){
          alert("Debe seleccionar un usuario y un programa para asignar correctamente.");
        }else{
          if (confirm("Esta seguro que desea realizar esta asignación?")){
            
            //console.log("Se confirma la asignacion")
            this.$http.post('http://localhost:5000/programausuario',{
            "nivelpermiso":"Edicion",
            "idus":valor,
            "idpro":valorP}).then(response=>{
            console.log("Exito!")
            }, response=>{
              console.log("No tuvo exito :c")
            });
            

          }else{
            console.log("No se realiza la asignacion")
          }        
        }

      }

      },
    
    /** Obtiene usuarios y programas existentes
     */
    mounted: function(){
      this.$http.get('http://localhost:5000/userAsign')
      .then(response =>{
          
          usersAsign = response.body.Users;
          this.Usuarios = response.body.Users;
          console.log(this.Usuarios)

          //alert("1) "+usersAsign[0].nameusuario+"\n2) "+usersAsign[1].nameusuario)

        }, response =>{
          console.log("falle :c ")
        });
      this.$http.get('http://localhost:5000/programs')
      .then(response =>{
          
          programsAsign = response.body.programs;
          this.Programas = response.body.programs;
          console.log(this.programs)

        }, response =>{
          console.log("falla ")
        });
    },
    data() {

        return {
            
             Usuarios: [],
             Programas: [],
           

        }
    
    }
}
</script>

<style>
@import '../fondo.css';
.tabla11{
  position: absolute;left: 300px;top: 100px;
}

.tabla2{
  position: relative;left: 250px;top: 100px;
  
}
.tituloUser{
  position: absolute;left: 300px;top: 50px;
}

.tituloProg{
   position: relative;left: 300px;top: 100px;
}

.bot {
  background: #ea7500;
  block-size: 25px;
  font-size: 16px;
  
  border-radius: 5px 10px 5px 10px;
  color: #e6e3e3;
  font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}
</style>
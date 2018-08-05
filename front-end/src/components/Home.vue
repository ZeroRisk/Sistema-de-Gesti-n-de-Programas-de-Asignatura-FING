<template>
<div class="main_file">
    <!-- 
    Menu lateral    
  -->
    <div id='cssmenu' >
<ul>

   <li class='active has-sub'> 
       <router-link :to="{ name: 'Home', params: { user: user , type: type }}"> 
           <a><span>Home</span></a> 
      </router-link> 
       </li> 
 
   <li> 
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
<!-- 
      encabezado pagina 
    -->
<div class="content-box-top">Bienvenido al portal.<a href="#/"><span class="cerrar">Cerrar sesión</span></a></div>
<div class="content-box-left"><img src="../assets/usach.png" height="100" width="200"></div>
<div class="content-box-down">Abajo.</div>

<!-- 
      botones permitidos para un usuario 
    -->
<div class="botonesHome">
    <table class="botonBuscar"><td><a href="#/buscar"><img src="../assets/buscarDoc.png"  height="150" width="150"></a></td> <td > Buscar programa </td> </table>
</div>


</div>
</template>

<script>
export default {
    props: ['user','type'],
    data(){
        return{

        }
    },
    mounted: function (){
        console.log("me llegaron los datos")
        console.log(this.user)
        console.log(this.type)

    }
}
</script>

<style>
@import '../fondo.css';

.botonCrear, .botonBuscar {
    border: 1px solid #ea7600;
    color: #002f6c;
    width: 300px;
    height: 150px; 
    background: #ffffffa9; 
}
.botonBuscar{
    position:absolute; top:200px; left: 500px ;
}





</style>

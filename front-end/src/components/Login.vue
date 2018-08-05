<template>
<div class="main_file">
    

<div class="content-box-top">Bienvenido al portal. </div>
    <div class="content-box-login">
        <table>
        <table>
            <td>
                <tr><h4> Bienvenido al portal de Programas de Asignaturas </h4>
                </tr>
                 
            </td>
        </table>
        <br>    
        <br> 
        <center>   
        <table>
            <td>
                <tr>   
                    Usuario :
                </tr>
                <tr>
                    Clave :
                </tr>
            </td> 
            <td>    
                <tr>
                    <input type="text" v-model="mail">
                </tr>
                <tr>
                    <input type="password" v-model="pass">
                </tr>
            </td> 
        </table>
        <button  v-on:click="login">iniciar sesion</button>
        </center>
        </table> 
    </div>
</div>
</template>

<script>
import router from '../index'
export default {
    // Datos globales del componente
    data(){
        return{
            mail:"",
            pass:"",
            user:[{
                id:0,
                username:"",
                cargo:"",
                departamento:"",
                correo:"",
                pass:""
            }],
            typeUser:""
        }
    },
    methods:{
        //Funcion que redirige a la pagina home correspondiente de si
        //es un usuario o un administrador.
        GoTo: function(){
            console.log("inicio sesion")
            if(this.typeUser == "User"){
                console.log("dirigiendo a home usuario")
                this.$router.push({name: 'Home', params: {user:this.user , type:this.typeUser }});
            }
            else if(this.typeUser== "Admin"){   
                console.log("dirigiendo a home administrador")
                this.$router.push({name:'HomeAdmin', params:{user:this.user , type:this.typeUser } })
            }
        },
        //Funcion que verifica si los datos ingresados del usuario existen en la base de datos
        login: function(){
            if(this.mail != "" && this.pass !=""){
            //Funcion que obtiene el usuario como un json segun el usuario y contraseña ingresado
            this.$http.get('http://localhost:5000/Authenticate?Correo='+ this.mail +'&Password='+ this.pass)
            .then(response =>{
                if(response.body.Type == "Admin"){
                    this.typeUser = "Admin"
                    this.user.id = response.body.admin[0]
                    this.user.username = response.body.admin[1]
                    this.user.cargo = response.body.admin[2]
                    this.user.departamento = response.body.admin[3]
                    this.user.correo = response.body.admin[4]
                    this.user.pass = response.body.admin[5]
                }
                else{
                    this.typeUser = "User"
                    this.user.id = response.body.user[0]
                    this.user.username = response.body.user[1]
                    this.user.cargo = response.body.user[2]
                    this.user.departamento = response.body.user[3]
                    this.user.correo = response.body.user[4]
                    this.user.pass = response.body.user[5]
                }
                this.GoTo()
            }, response =>{
                console.log("no hay conexion con la base de datos o el usuario no existe ")
            })
            }
            else{
                alert("complete los campos de usuario y contraseña")
            }
        }
    }
}
</script>

<style>
.main_file{
  
  width: 985px;
  height: 230em;
  background:#e6e3e3;
}

.content-box-top {
margin: 0 0 25px;
overflow: hidden;
padding: 21px;
color: #b1b1b1;
}

.content-box-top {
background-color: #002f6c;
position:absolute; top:0px; left: 0px ; right: 0px;
}

.content-box-login {
background-color: #002f6cbe;
color: #e6e3e3;
height: 250px;
width: 500px;
position:absolute; top:200px; left: 300px ; 
}

</style>

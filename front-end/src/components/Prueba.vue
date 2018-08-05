<template>
<div id="principal">
    <button id="g">Hello</button>
    <button  v-on:click="prueba()"  id="NO">+</button>
</div>
</template>


<script>
function hello() {
alert('Hello');
}

export default {
  methods: {
    prueba: function(){
      var div = document.getElementById("principal");
      var boton = document.createElement("button");
      var textoBoton = document.createTextNode("Dinamico");
      boton.setAttribute("id", "hellobutton");
      boton.appendChild(textoBoton)
      div.appendChild(boton);
      document.getElementById("hellobutton").addEventListener("click", hello);
    }
  }
}

</script>
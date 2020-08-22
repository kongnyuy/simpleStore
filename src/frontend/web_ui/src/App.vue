<template>
  <div id="app">
        <div class="center grid">
      <vs-row>
      <vs-col vs-type="flex" vs-justify="center" vs-align="center" w="12">
        <Home/>
      </vs-col>
    </vs-row>
    </div>
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import Home from './components/Home'

export default {
  name: 'App',
  components: {
    //HelloWorld
    Home
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

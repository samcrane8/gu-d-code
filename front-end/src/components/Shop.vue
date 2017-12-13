<template>
  <v-app style="margin:0px;padding:0px;">
    <v-content>
      <section>
        <v-layout
              column
              align-center
              justify-center
              class="white--text"
        >
          <img src="/static/PBD_LinensPeople-34.jpg" alt="Linen Model" width="100%">
          <h1 class="white--text mb-2 display-1 text-xs-center">Parallax Template</h1>
        </v-layout>
      </section>
      <section>
      </section>
      <section>
        <v-layout class="text-xs-center" justify-space-around row wrap>
          <v-item title="YEAH"> </v-item>
          <v-item/>
          <v-item/>
          <v-item/>
          <v-item/>
          <v-item/>
          <v-item/>
          <v-item/>
          <v-item/>
        </v-layout>
      </section>
    </v-content>
  </v-app>
</template>

<script>
import Item from './Item.vue'

export default {
  components: {
    'v-item': Item
  }
}
</script>

<style> 
body {
  margin-top: 50px;
  padding: 0px;
}
</style>
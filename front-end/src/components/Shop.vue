<template>
  <main class="text-xs-center">
    <!-- <section>
      <v-layout
            column
            align-center
            justify-center
            class="white--text"
      >
        <img src="/static/PBD_LinensPeople-34.jpg" alt="Linen Model" width="100%">
      </v-layout>
    </section> -->
    <section>
      <v-layout wrap class="text-xs-center">
        <v-flex 
          v-for="item in items"
          :key = item.color>
          <v-item :item_info = item> </v-item>
          <v-spacer/>
        </v-flex>
      </v-layout>
    </section>
  </main>
</template>

<style>
  @import url(https://fonts.googleapis.com/css?family=Barlow);
  main {
    font-family: 'Barlow', sans-serif;
  }
</style>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Item from './Item.vue'
import router from '@/router'

Vue.use(VueAxios, axios)

export default {
  components: {
    'v-item': Item
  },
  data () {
    return {
      items: [
        {
          id: 1,
          name: "DUMMY PRODUCT",
          image: "static/PBD_Linens-58.jpg",
          price: "95",
          max_qty: 20,
          color: "white"
        }
      ]
    }
  },
  methods : {
    fetch_items() {
      //now this is going to be run when they mount.
      var url = "http://0.0.0.0:5001/get_products"
      axios.get(url)
          .then((response) => {
            this.items = response.data
          })
          .catch(error => {
            alert('Hmmm something went wrong with our servers when fetching stations!! Sorry!')
        });
    }
  },
  beforeMount(){
    this.fetch_items()
  }
}
</script>

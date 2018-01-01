<template>
  <main>
    <v-layout style="background-color:0px;margin-top:64px; margin-left:50px; margin-right:50px;padding:0px;font-family: 'Barlow', sans-serif;">
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
        <v-layout class="text-xs-center" justify-space-around row wrap>
          <v-flex 
            v-for="item in items"
            :key = item.id
            sm4>
            <v-item :item_info = item> </v-item>
          </v-flex>
        </v-layout>
      </section>
    </v-layout>
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
  beforeMount(){

  },
  data () {
    return {
      items: [
        {
          id: 1,
          title: "TEST NAME",
          image: "static/PBD_Linens-58.jpg",
          price: "95",
          max_qty: 20,
          color: "white"
        },
        {
          id: 2,
          title: "TEST NAME",
          image: "static/PBD_Linens-58.jpg",
          price: "95",
          max_qty: 20,
          color: "white"
        },
        {
          id: 3,
          title: "TEST NAME",
          image: "static/PBD_Linens-58.jpg",
          price: "95",
          max_qty: 20,
          color: "white"
        },
        {
          id: 4,
          title: "TEST NAME",
          image: "static/PBD_Linens-58.jpg",
          price: "95",
          max_qty: 20,
          color: "white"
        },
        {
          id:5,
          title: "TEST NAME",
          image: "static/PBD_Linens-58.jpg",
          price: "95",
          max_qty: 20,
          color: "white"
        },
        {
          id: 6,
          title: "GUY",
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
      var url = "http://gudlinens.com:5001/get_products"
      axios.get(url)
          .then((response) => {
            this.items = response.data
          })
          .catch(error => {
            alert('Hmmm something went wrong with our servers when fetching stations!! Sorry!')
        });
    }
  }
}
</script>

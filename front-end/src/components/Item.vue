<template>
  <v-card flat style="margin: 12px; background-color:white;" class="text-xs-left">
    <v-card-title>
    </v-card-title>
    <v-card-media src="static/PBD_Linens-58.jpg" height="200px"  v-on:click="something">
    </v-card-media>
    <v-layout row>
      <v-flex>
        {{item_info.title}}
      </v-flex>
      <v-spacer/>
      <v-flex class="text-xs-right">
        price: ${{item_info.price}}
      </v-flex>
    </v-layout>
    <v-layout row class="text-xs-center">
      <v-flex>
        <v-btn flat v-on:click="remove_one" :disabled="quantity==0">
          <v-icon color="black">remove</v-icon>
        </v-btn>
        {{quantity}}
        <v-btn flat v-on:click="add_one" :disabled="quantity==item_info.max_qty">
          <v-icon color="black">add</v-icon>
        </v-btn>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
import router from '@/router'

export default {
  props: {
    item_info: {
      type: Object,
      default: {
        title: "default title"
      }
    },
    closeAction: Function,
    containerClass: String
  },
  data() {
    return {
      quantity: 0,
      flipped: false
    }
  } ,
  methods: {
    add_one(event) {
      this.quantity += 1;
      this.flipped = !this.flipped;
    },
    remove_one(event) {
      if (this.quantity > 0){
        this.quantity -= 1;
      }
    },
    goto_item_page(item) {

    },
    something() {
      router.push('about')
    }
  }
}
</script>

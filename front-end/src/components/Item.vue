<template>
  <v-card flat style="margin: 12px; background-color:white;" class="text-xs-center" width="250px">
    <v-layout column class="text-xs-left">
      <v-flex>
        <img :src="item_info.image" height="250px" width="250px">
        </img>
        <v-layout row>
        <span class="text-xs-left">
          {{item_info.name}}
        </span>
        <span class="text-xs-right">
          ${{item_info.price}}
        </span>
      </v-layout>
      </v-flex>
      
      <!-- <v-layout row class="text-xs-center">
        <v-flex>
          <v-btn flat v-on:click="remove_one" :disabled="quantity==0">
            <v-icon color="black">remove</v-icon>
          </v-btn>
          {{quantity}}
          <v-btn flat v-on:click="add_one" :disabled="quantity==item_info.max_qty">
            <v-icon color="black">add</v-icon>
          </v-btn>
        </v-flex>
      </v-layout>-->
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
        name: "default title"
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

<template>
  <v-card flat style="margin: 12px; background-color:white;" class="text-xs-center" width="250px">
    <v-layout column align-center>
      <v-flex>
        <img :src="item_info.image" :height="side" :width="side"  style="width:250px;cursor:pointer" v-on:click="goto_item">
        </img>
        <v-layout row>
          <v-flex class="text-xs-left">
            {{item_info.name}}
          </v-flex>
          <v-flex class="text-xs-right">
            ${{item_info.price}}
          </v-flex>
        </v-layout>
        <v-flex style="color:#747677" class="text-xs-left">
          {{item_info.color}}
        </v-flex>
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
        name: "default title",
        color: "default color"
      }
    },
    closeAction: Function,
    containerClass: String
  },
  data() {
    return {
      quantity: 0,
      flipped: false,
      side: '250px'
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
    goto_item() {
      router.push('product?name='+this.item_info.name+'&color='+this.item_info.color)
    }
  }
}
</script>

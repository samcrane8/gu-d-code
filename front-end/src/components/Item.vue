<template>
  <div class="card-container" v-on:click="add_one">
    <div class="card">
      <div class="side"><img src="https://cdn.shopify.com/s/files/1/0951/7126/products/classic-hardcore-bundle_solid-white_silo_900x.jpg?v=1509636930" v-bind="{width: _width}" alt="Jimmy Eat World"></div>
      quantity = {{this.quantity}}<br>
      <span v-if="flipped">flipped</span>
      <span v-else>not flipped</span>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    Title: String,
    closeAction: Function,
    containerClass: String,
    _width: {
      type: String,
      default: '250px'
    }
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
    }
  }
}
</script>

<style type="text/css">

  body {
    font: 600 14px/24px "Open Sans", "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", Sans-Serif;
    margin: 12px 0;
  }
  .card-container {
    margin: 10px;
    cursor: pointer;
    height: 250px;
    perspective: 600;
    position: relative;
    width: 250px;
  }
  .card {
    height: 100%;
    position: absolute;
    transform-style: preserve-3d;
    transition: all 1s ease-in-out;
    width: 100%;
  }

</style>
<template>
  <main>
  	<section style="margin-left:30px;margin-right:30px;">
	    <v-layout v-if="this.cart.length === 0" row wrap>
	      <v-flex class="text-xs-center">
	        <h1> CART IS EMPTY </h1>
	      </v-flex>
	    </v-layout>
	    <v-layout row wrap v-if="!(this.cart.length === 0)" style="margin-top:80px;">
		    <v-layout column style="margin-top:0px;">
		      <v-layout 
		      style="margin-bottom:25px;margin-top:0px;"
		      v-for="(item,index) in cart"
		      :key = "index"
		      class="text-xs-left"
		      row>
		        <v-flex class="text-xs-right">
							<img v-on:click="goto_item(item)" :src="item.image" :width="size" :height="size"/>
						</v-flex>
						<v-layout column>
							<v-flex style="margin-left:8px;">
								<h5 style="margin:0px;margin-top:-8px;padding-top:0px;" class="text-xs-left">{{item.name}}</h5>
								<p>{{item.color}}</p>
				        <h6>${{item.price}}</h6>
				        <v-flex>
				          <v-btn style="margin:0px;padding-top:0px" flat icon v-on:click="remove_one(item)" :disabled="item.quantity==1">
				            <v-icon small color="black">remove</v-icon>
				          </v-btn>
				          {{item.quantity}}
				          <v-btn style="margin:0px;" flat icon v-on:click="add_one(item)" :disabled="item.quantity==item.max_qty">
				            <v-icon small color="black">add</v-icon>
				          </v-btn>
				        </v-flex>
				      </v-flex>
			      </v-layout>
			      <v-layout>
			      	<v-flex>
			      		<v-btn style="margin:0px;margin-top:-8px;" flat icon v-on:click="remove_item(item)">
				      		<svg style="width:24px;height:24px;" viewBox="0 0 24 24">
	                  <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
	    							<path d="M0 0h24v24H0z" fill="none"/>
	                </svg>
	              </v-btn>
			      	</v-flex>
			      </v-layout>
		    	</v-layout>
		    </v-layout>
		    <v-layout>
		    	<v-layout column>
		    		<v-flex> 
		    			<h6 style="margin-top:0px;" class="text-xs-left"> SUMMARY </h6>
		    			<v-flex>
			    			Subtotal................${{this.subtotal}}
			    		</v-flex>
			    		<v-flex style="margin-top:50px;">
				    			<v-btn outline flat v-on:click="goto_checkout"> TO CHECKOUT </v-btn>
				    	</v-flex>
		    		</v-flex>
		    	</v-layout>
		    </v-layout>
		  </v-layout>
	  </section>
  </main>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from '@/router'

Vue.use(VueAxios, axios)

export default {
	data () {
		return {
			subtotal: 145,
			size:"150px",
			cart: [{
        "color": "...",
        "image": "https://s3.amazonaws.com/gudlinens/PBD_Linens-65.jpg",
        "max_qty": 20,
        "name": "Loading...",
        "price": 95.0,
        "quantity": 5
    	}]
		}
	},
	methods: {
		isCartEmpty() {
			return this.cart.length === 0
		},
  	add_one(item) {
      item.quantity += 1;
      this.edit_cart_quantity(item)
    },
    remove_one(item) {
      if (item.quantity > 0){
        item.quantity -= 1;
      }
      this.edit_cart_quantity(item)
    },
    edit_cart_quantity(item){
	    var body = [{'name': item.name, 'color': item.color, 'quantity': item.quantity}]
    	var url = "http://0.0.0.0:5001/edit_cart_item_quantities"
      axios.post(url,body, {withCredentials:true})
          .then((response) => {
      			this.$emit('cart_change')
	    			this.get_subtotal()
          })
          .catch(error => {
            alert('Hmmm something went wrong with our servers when fetching stations!! Sorry!')
        });
  	},
  	remove_item(item){
  		var body = [{'name': item.name, 'color': item.color}]
    	var url = "http://0.0.0.0:5001/remove_cart_items"
      axios.post(url,body, {withCredentials:true})
          .then((response) => {
      			this.$emit('cart_change')
      			this.get_cart()
          })
          .catch(error => {
            alert('Hmmm something went wrong with our servers when fetching stations!! Sorry!')
        });
  	},
  	get_cart(){
			var url = "http://0.0.0.0:5001/get_cart"
	    axios.get(url, {withCredentials:true})
	      .then((response) => {
	        this.cart = response.data
	    		this.get_subtotal()
	      })
	      .catch(error => {
	        alert('Hmmm something went wrong with our servers when fetching stations!! Sorry!')
	    });
 		},
    goto_item(item_info) {
      router.push('product?name='+item_info.name+'&color='+item_info.color)
    },
    get_subtotal(){
    	this.subtotal=0
    	for (var i = 0, len = this.cart.length; i < len; i++){
    		this.subtotal += this.cart[i].price * this.cart[i].quantity
    	}
  	},
  	goto_checkout(){
  		router.push('/checkout')
  	}
	},
	beforeMount() {
		this.get_cart()
	},
	computed: {
    binding () {
      const binding = {}

      if (this.$vuetify.breakpoint.smAndUp){
      	this.size="150px"
      } else {
      	this.size="100px"
    	}

      return binding
    }
  }
}
</script>
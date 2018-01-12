<template>
  <main>
  	<section style="margin-left:30px;margin-right:30px;">
	    <v-layout v-if="isCartEmpty()" row wrap>
	      <v-flex class="text-xs-center">
	        <h1> CART IS EMPTY </h1>
	      </v-flex>
	    </v-layout>
	    <v-layout row wrap v-if="!isCartEmpty()" style="margin-top:80px;">
		    <v-layout column>
		      <v-layout 
		      style="margin-bottom:25px;"
		      v-for="(item,index) in cart"
		      :key = "index"
		      class="text-xs-left"
		      row>
		        <v-flex class="text-xs-right">
							<img :src="item.image" width="150px" height="150px"/>
						</v-flex>
						<v-layout column style="margin-left:10px;">
							<v-flex>
								<h5>{{item.name}}</h5>
								<p>{{item.color}}</p>
				        <h6>${{item.price}}</h6>
				        <v-flex>
				          <v-btn flat v-on:click="remove_one(item)" :disabled="item.quantity==0">
				            <v-icon color="black">remove</v-icon>
				          </v-btn>
				          {{item.quantity}}
				          <v-btn flat v-on:click="add_one(item)" :disabled="item.quantity==item.max_qty">
				            <v-icon color="black">add</v-icon>
				          </v-btn>
				        </v-flex>
				      </v-flex>
			      </v-layout>
		    	</v-layout>
		    </v-layout>
		    <v-layout class="text-xs-right">
		    	<v-card flat>
		    		<v-card-title> 
		    			<h6 class="text-xs-center"> SUMMARY </h6>
		    		</v-card-title>
		    		<v-card-text>
		    			<v-layout column>
			    			<v-layout row>
				    			<v-flex>
					    			Subtotal...................
					    		</v-flex>
					    		<v-spacer/>
					    		<v-flex>
					    			$145
					    		</v-flex>
					    	</v-layout>
					    	<v-spacer/>
				    		<v-flex>
				    			<v-btn outline flat> TO CHECKOUT </v-btn>
				    		</v-flex>
				    	</v-layout>
		    		</v-card-text>
		    	</v-card>
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
    },
    remove_one(item) {
      if (item.quantity > 0){
        item.quantity -= 1;
      }
    }
	},
	beforeMount() {
		var url = "http://0.0.0.0:5001/get_cart"
    axios.get(url, {withCredentials:true})
      .then((response) => {
        this.cart = response.data
      })
      .catch(error => {
        alert('Hmmm something went wrong with our servers when fetching stations!! Sorry!')
    });
	}
}
</script>
<template>
  <main>
  	<section style="margin-left:30px;margin-right:30px;">
	    <v-layout v-if="isCartEmpty()" row wrap>
	      <v-flex class="text-xs-center">
	        <h1> CART IS EMPTY </h1>
	      </v-flex>
	    </v-layout>
	    <v-layout row wrap>
		    <v-layout v-if="!isCartEmpty()" column>
		      <v-layout 
		      v-for="item in cart"
		      :key = collection
		      class="text-xs-left"
		      row>
		        <h6>{{item}}</h6>
		        <v-spacer/>
		        
		    	</v-layout>
		    </v-layout>
		    <v-layout class="text-xs-right">
		    	<v-card flat>
		    		<v-card-title> 
		    			<h6 class="text-xs-center"> SUMMARY </h6>
		    		</v-card-title>
		    		<v-card-text>
		    			<layout column>
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
				    	</layout>
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
			cart: {}
		}
	},
	methods: {
		isCartEmpty() {
			return Object.keys(this.cart).length === 0
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
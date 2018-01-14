<template>
	<v-layout wrap row style="margin-top: 50px;">
		<v-layout column style="margin:25px;">
			<v-flex class="text-xs-center" style="margin-top:50px;">
				<img :src="product_info.images[0]" width="250px" height="250px"/>
			</v-flex>
		</v-layout>
		<v-layout column style="width:300px;margin-left: 25px;margin-right:25px;">
			<v-flex xs12 class="text-xs-left" mt-5>
				<v-layout row>
					<h3>{{name}}</h3>
					<p>{{color}}</p>
				</v-layout>
				<v-flex>
					<h5>${{product_info.price}}</h5>
				</v-flex>
				<v-tabs left>
		      <v-tabs-bar class="white">
		        <v-tabs-slider class="grey"></v-tabs-slider>
		        <v-tabs-item
		          v-for="i in items"
		          :key="i"
		          :href="'#tab-' + i"
		        >
		          {{ i }}
		        </v-tabs-item>
		      </v-tabs-bar>
		      <v-tabs-items>
		        <v-tabs-content
		          id="tab-Description"
		        >
		          <v-card flat>
		            <v-card-text>{{ product_info.description }}</v-card-text>
		          </v-card>
		        </v-tabs-content>
		        <v-tabs-content
		          id="tab-Details"
		        >
		          <v-card flat>
		            <v-card-text>{{ product_info.details }}</v-card-text>
		          </v-card>
		        </v-tabs-content>
		      </v-tabs-items>
		    </v-tabs>
			</v-flex>
			<v-layout row>
				<!-- <v-flex fluidclass="text-xs-left">
					<h5>PRICE: ${{product_info.price}}</h5>
				</v-flex> -->
				<v-layout row class="text-xs-left" style="margin-right:30px;">
					<v-flex>
	          <v-btn icon style="margin-right:0px;margin-left:2px;" flat v-on:click="remove_one" :disabled="quantity==1">
	            <v-icon color="black">remove</v-icon>
	          </v-btn>
	          {{quantity}}
	          <v-btn icon style="margin-right:0px;margin-left:0px;" flat v-on:click="add_one" :disabled="quantity==this.max_qty">
	            <v-icon color="black">add</v-icon>
	          </v-btn>
	        </v-flex>
	        <v-flex>
						<v-btn style="border-radius:0px" flat outline v-on:click="add_to_cart"> ADD TO CART </v-btn>
					</v-flex>
				</v-layout>
			</v-layout>
		</v-layout>
	</v-layout>
</template>

<style>
</style>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from '@/router'

Vue.use(VueAxios, axios)

export default {
	data() {
		return {
			name: "",
			color: "",
			quantity: 1,
			max_qty: 20,
			items: ['Description', 'Details'],
      product_info: {
      	description: 'Loading...',
      	details: 'Loading...',
      	images: [""],
      	price: "0"
    	}
		}
	},
	methods : {
    fetch_product_info() {
      //now this is going to be run when they mount.
      var url = "http://0.0.0.0:5001/get_product_info"
      var body = {
      	"name": this.name,
      	"color": this.color
    	}
      axios.post(url,body)
          .then((response) => {
            this.product_info = response.data
          })
          .catch(error => {
            alert('Hmmm something went wrong with our servers when fetching stations!! Sorry!')
        });
    },
    add_to_cart() {
    	var body = [{'name': this.name, 'color': this.color, 'quantity': this.quantity}]
    	var url = "http://0.0.0.0:5001/add_to_cart"
      axios.post(url,body, {withCredentials:true})
          .then((response) => {
      			this.$emit('added_to_cart')
          })
          .catch(error => {
            alert('Hmmm something went wrong with our servers when fetching stations!! Sorry!')
        });
  	},
  	add_one(event) {
      this.quantity += 1;
    },
    remove_one(event) {
      if (this.quantity > 0){
        this.quantity -= 1;
      }
    }
  },
	beforeMount() {
		this.name = this.$route.query.name
		this.color = this.$route.query.color
		this.fetch_product_info()
	}
}
</script>
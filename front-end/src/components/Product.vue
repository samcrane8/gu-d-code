<template>
	<v-layout wrap row style="margin-top: 50px;">
		<v-layout column style="margin:25px;">
			<v-flex class="text-xs-center">
				<img :src="product_info.images[0]" width="300px" height="300px"/>
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
				<v-flex fluid class="text-xs-center">
					<v-btn flat outline v-on:click="add_to_bag"> ADD TO CART </v-btn>
				</v-flex>
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
    add_to_bag() {
    	alert('adding to bag!')
  	}
  },
	beforeMount() {
		this.name = this.$route.query.name
		this.color = this.$route.query.color
		this.fetch_product_info()
	}
}
</script>
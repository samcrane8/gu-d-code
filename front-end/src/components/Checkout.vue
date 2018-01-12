<template>
  <v-layout row>
    <v-layout column style="margin-top:80px;">
    	<v-flex class="text-xs-center">
    		YAH
    	</v-flex>
    </v-layout>
    <v-layout>
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
			    			${{this.subtotal}}
			    		</v-flex>
			    	</v-layout>
			    	<v-spacer/>
			    	<v-layout style="margin-top:100px;">
			    		<v-flex>
			    			<v-btn outline flat v-on:click="goto_checkout"> TO CHECKOUT </v-btn>
			    		</v-flex>
			    	</v-layout>
		    	</v-layout>
    		</v-card-text>
    	</v-card>
    </v-layout>
  </v-layout>
</template>

<style>
</style>

<script>
export default {
	data() {
		return {
			subtotal: 0
		}
	}
}
</script>
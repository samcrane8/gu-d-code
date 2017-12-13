<template>
  <v-app>
    <main>
      <v-container fill-height>
        <v-layout row justify-space-around>
          <v-flex v-bind="binding">
            <v-card style="border-radius:0px;">
              <v-card-title fill-width>
                <v-layout column style="padding-bottom:2%;">
                  <h3 class="text-xs-center" style="padding-top:2%;"> 
                      GÜDLINENS
                  </h3>
                  <h6 class="text-xs-center" style="font-size:15px;">
                    Luxury, ethically-sourced linens that don't kill your wallet.
                  </h6>
                </v-layout>
              </v-card-title>
            </v-card>
            <v-card style="border-radius:0px;padding-top:10px;background-color:#fcfcfc">
              <v-card-title fill-width>
                <v-layout column>
                  <h6 class="text-xs-center" v-if="!subscribed">
                    {{message1}}
                  </h6>
                  <h6 class="text-xs-center" v-if="subscribed">
                    <br><br><br>{{message2}}<br><br><br><br>
                  </h6> 
                  <v-text-field
                    label="Email"
                    style="padding-left:7%;padding-right:5%;"
                    v-model="email"
                    v-if="!subscribed"
                  />
                  <v-flex class="text-xs-center">
                    <v-btn v-if="!subscribed" outline style="border-radius:0px;background-color:#f4b061;"type="submit" @click.prevent = "join">JOIN</v-btn>
                  </v-flex>
                </v-layout>
              </v-card-title>
              <v-card-title class="text-xs-center">
                <v-layout row justify-space-around>
                  <!-- <v-btn flat style="border-radius:2px;"type="submit" @click.prevent = "join">
                    <svg style="width:24px;height:24px" viewBox="0 0 24 24">
                      <path fill="#000000" d="M22.46,6C21.69,6.35 20.86,6.58 20,6.69C20.88,6.16 21.56,5.32 21.88,4.31C21.05,4.81 20.13,5.16 19.16,5.36C18.37,4.5 17.26,4 16,4C13.65,4 11.73,5.92 11.73,8.29C11.73,8.63 11.77,8.96 11.84,9.27C8.28,9.09 5.11,7.38 3,4.79C2.63,5.42 2.42,6.16 2.42,6.94C2.42,8.43 3.17,9.75 4.33,10.5C3.62,10.5 2.96,10.3 2.38,10C2.38,10 2.38,10 2.38,10.03C2.38,12.11 3.86,13.85 5.82,14.24C5.46,14.34 5.08,14.39 4.69,14.39C4.42,14.39 4.15,14.36 3.89,14.31C4.43,16 6,17.26 7.89,17.29C6.43,18.45 4.58,19.13 2.56,19.13C2.22,19.13 1.88,19.11 1.54,19.07C3.44,20.29 5.7,21 8.12,21C16,21 20.33,14.46 20.33,8.79C20.33,8.6 20.33,8.42 20.32,8.23C21.16,7.63 21.88,6.87 22.46,6Z" />
                    </svg>
                  </v-btn> -->
                  <v-btn flat style="border-radius:2px;"type="submit" href="https://www.instagram.com/gudlinens/">
                    <svg style="width:24px;height:24px" viewBox="0 0 24 24">
                      <path fill="#000000" d="M7.8,2H16.2C19.4,2 22,4.6 22,7.8V16.2A5.8,5.8 0 0,1 16.2,22H7.8C4.6,22 2,19.4 2,16.2V7.8A5.8,5.8 0 0,1 7.8,2M7.6,4A3.6,3.6 0 0,0 4,7.6V16.4C4,18.39 5.61,20 7.6,20H16.4A3.6,3.6 0 0,0 20,16.4V7.6C20,5.61 18.39,4 16.4,4H7.6M17.25,5.5A1.25,1.25 0 0,1 18.5,6.75A1.25,1.25 0 0,1 17.25,8A1.25,1.25 0 0,1 16,6.75A1.25,1.25 0 0,1 17.25,5.5M12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9Z" />
                    </svg>
                  </v-btn>
                  <v-btn flat style="border-radius:2px;"type="submit" href="http://www.facebook.com">
                    <svg style="width:24px;height:24px" viewBox="0 0 24 24">
                      <path fill="#000000" d="M17,2V2H17V6H15C14.31,6 14,6.81 14,7.5V10H14L17,10V14H14V22H10V14H7V10H10V6A4,4 0 0,1 14,2H17Z" />
                    </svg>
                  </v-btn>
                </v-layout>
              </v-card-title>
            </v-card>
          </v-flex>
          <v-flex/>
        </v-layout>
      </v-container>
    </main>
  </v-app>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from '@/router'
 
Vue.use(VueAxios, axios)

export default {
  data() {
    return {
      auth: {"username": '', "password": ''},
      response: {},
      email: "",
      subscribed: false,
      message1: "Join our mailing list to stay in the loop:",
      message2: "Great! A confirmation email is on the way."
    }
  },
  methods: {
    join: function() {
      var url = "http://gudlinens.com:5000/add_to_newsletter"
      const vm = this;
      var body = { 'email': this.email}
      axios.post(url, body)
        .then((response) => {
          if (response.data.code == 200) {
            this.email = ""
            this.subscribed = true;
          } else if (response.data.code == 50) {
            this.message2="This email is already subscribed."
            this.subscribed = true;
          } else if (response.data.code == 31) {
            this.message1="Not a vaild email. Try again."
            this.email = ""
          }
        })
        .catch(error => {
          this.message2="Something went wrong with the server... we're working on it!"
      });
    }
  },
  computed: {
    binding () {
      const binding = {}

      if (this.$vuetify.breakpoint.mdAndUp) {
        binding.xs6 = true
      }
      return binding
    }
  }
}
</script>

<style>
@import url(https://fonts.googleapis.com/css?family=Barlow);
main {
  background: url("/static/results.jpg") no-repeat fixed left center;
  background-size: cover;
  font-family: 'Barlow', sans-serif;
}

</style>
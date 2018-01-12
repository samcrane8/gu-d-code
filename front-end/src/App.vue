<template>
  <v-app style="background-color:white; margin-top: 0px; font-family: 'Barlow', sans-serif;">
    <v-navigation-drawer temporary v-model="sidebar" absolute>
      <v-list>
        <v-list-tile
          v-for="item in menuItems"
          :key="item.title"
          :to="item.path"
          :color="item.color">
          <v-list-tile-content>{{ item.title }}</v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar fixed flat color="white">
      <span class="hidden-sm-and-up">
        <v-toolbar-side-icon @click.stop="sidebar = !sidebar">
        </v-toolbar-side-icon>
      </span>
      <v-toolbar-title>
        <router-link to="/" tag="span" style="cursor: pointer;">
          <span style="font-size:23.5px;color:black;">GÜDLINENS</span>
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-xs-only">
        <v-btn
          flat
          v-for="item in menuItems"
          :key="item.title"
          :color="item.color"
          :to="item.path">
          <span style="color:black;">{{ item.title }}</span>
        </v-btn>
        <v-btn
          flat
          :color="cart_tile.color"
          :to="cart_tile.path">
          <span style="color:black;">{{ cart_tile.title }}({{cart_size}})</span>
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <main style="background-color:#ffffff; margin-top: 0px; margin-bottom: 50px;">
      <v-container pa-0 fluid>
        <router-view v-on:set_toolbar="set_toolbar"></router-view>
      </v-container>
    </main>
    <span style="background-color:white;">
      <section style="margin-bottom:20px;">
        <v-layout row>
          <v-layout column style="margin-left:50px;">
            <v-flex class="text-xs-left">
              <p> COMPANY </p>
              <span style="cursor:pointer" @click="goto('about')"> About </span><br>
              <span style="cursor:pointer" @click="goto('career')"> Career </span><br>
              <span style="cursor:pointer" @click="goto('sourcing')"> Sourcing </span>
            </v-flex>
          </v-layout>
          <v-flex class="text-xs-left">
            <p> HELP </p>
            <span style="cursor:pointer" @click="goto('support')"> Support </span><br>

          </v-flex>
        </v-layout>
      </section>
      <v-footer class="pa-3" style="background-color:white;">
        <v-spacer></v-spacer>
        <a href="https://www.instagram.com/gudlinens" style="text-decorations:none"><svg style="width:24px;height:24px;margin-right:20px;cursor:pointer;" viewBox="0 0 24 24">
          <path fill="#000000" d="M7.8,2H16.2C19.4,2 22,4.6 22,7.8V16.2A5.8,5.8 0 0,1 16.2,22H7.8C4.6,22 2,19.4 2,16.2V7.8A5.8,5.8 0 0,1 7.8,2M7.6,4A3.6,3.6 0 0,0 4,7.6V16.4C4,18.39 5.61,20 7.6,20H16.4A3.6,3.6 0 0,0 20,16.4V7.6C20,5.61 18.39,4 16.4,4H7.6M17.25,5.5A1.25,1.25 0 0,1 18.5,6.75A1.25,1.25 0 0,1 17.25,8A1.25,1.25 0 0,1 16,6.75A1.25,1.25 0 0,1 17.25,5.5M12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9Z" />
        </svg></a>
        <div>&copy; {{ new Date().getFullYear() }}</div>
      </v-footer>
    </span>
  </v-app>
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
        appTitle: 'HSK',
        sidebar: false,
        toolbar: false,
        cart_size: 0,
        menuItems: [
          { title: 'ABOUT US', path: '/about', icon: 'face', color: "transparent"}
        ],
        cart_tile: { title: 'CART', path: '/cart', icon: 'face', color: "transparent"},
        cart: [
          { name: 'CLASSIC SET', color: 'White', qty: 1}
        ]
      }
    },
    methods: {
      set_toolbar(setting){
        this.toolbar = setting
      },
      goto(loc){
        router.push(loc)
      },
      goto_external(loc){
        window.location.href = loc
      },
      get_cart_size() {
        var url = "http://0.0.0.0:5001/get_products"
        axios.get(url)
          .then((response) => {
            this.cart_size = response.data
          })
          .catch(error => {
            alert('Hmmm something went wrong with our servers when fetching stations!! Sorry!')
        });
      }
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'

  @require '../../node_modules/vuetify/src/stylus/settings/_colors'
  @import url("https://fonts.googleapis.com/css?family=Barlow")
 
  $theme := {
    primary: $red.darken-2
    accent: $red.accent-2
    secondary: $grey.lighten-1
    info: $blue.lighten-1
    warning: $amber.darken-2
    error: $red.accent-4
    success: $green.lighten-2
  }

</style>
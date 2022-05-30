// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import store from './store'
Vue.config.productionTip = false
const axios = require('axios').default

// axios.<method> will now provide autocomplete and parameter typings
/* eslint-disable no-new */
new Vue({

  el: '#app',
  data: {
    jsonapi: []
  },
  mounted: function () {
    axios.get('http://127.0.0.1:8000/api/v2/usdrub/?format=json')
      .then(response => {
        this.jsonapi = response.data
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      })
  }
})

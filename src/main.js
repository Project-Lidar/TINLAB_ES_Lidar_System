import Vue from "vue";
import App from "./App.vue";
import router from "./routes/routes";
import BootstrapVue from "bootstrap-vue";
import PortalVue from 'portal-vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Vue plugins...
Vue.use(BootstrapVue);
Vue.use(PortalVue)

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  router
}).$mount("#app");

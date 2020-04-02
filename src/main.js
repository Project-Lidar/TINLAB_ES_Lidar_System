import Vue from "vue";
import App from "./App.vue";
import router from "./routes/routes";
import Axios from "axios";
import { BootstrapVue, BootstrapVueIcons } from "bootstrap-vue";
import PortalVue from "portal-vue";
import VueMqtt from "vue-mqtt";
import VueGamepad from "vue-gamepad";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

// Vue plugins...
Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);
Vue.use(PortalVue);
Vue.use(VueGamepad);
Vue.use(VueMqtt, "wss://eecfbf0c:59ea275059b9c893@broker.shiftr.io/", {
  clientId: "Web-App",
  username: "f07edbf7",
  password: "1e4e236c716b17ec"
});

Vue.prototype.$http = Axios;

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  router
}).$mount("#app");

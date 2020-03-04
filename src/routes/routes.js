import Vue from "vue";
import Router from "vue-router";

//Component imports
import Home from "../components/Home.vue";
import Control from "../components/Control.vue";
import NavBar from "../components/NavBar.vue";
import NotFound from "../components/404.vue"

Vue.use(Router);

let router = new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      component: NavBar,
      children: [
        {
          path: "home",
          component: Home
        },
        {
          path: "control",
          component: Control
        }
      ]
    },
    { path: '*', component: NotFound }
  ]
});

export default router;

import Vue from "vue";
import Router from "vue-router";

//Component imports
import Home from "../components/Home.vue";
import Control from "../components/Control.vue";
import NavBar from "../components/NavBar.vue";
import Stats from "../components/Stats.vue";
import NotFound from "../components/404.vue";
import Login from "../components/Login";
import Register from "../components/Register";
import Admin from "../components/Admin";
import Dash from "../components/Dashboard";

Vue.use(Router);

let router = new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "userboard",
      redirect: "/home",
      component: NavBar,
      children: [
        {
          path: "home",
          name: "home",
          component: Home,
          meta: {
            requiresAuth: true
          }
        },
        {
          path: "control",
          name: "control",
          component: Control,
          meta: {
            requiresAuth: true
          }
        },
        {
          path: "stats",
          name: "stats",
          component: Stats,
          meta: {
            requiresAuth: true
          }
        }
      ]
    },
    {
      path: "/login",
      name: "login",
      component: Login,
      meta: {
        guest: true
      }
    },
    {
      path: "/admin",
      name: "admin",
      component: Admin,
      redirect: "/dash",
      meta: {
        requiresAuth: true,
        is_admin: true
      },
      children: [
        {
          path: "/register",
          name: "register",
          component: Register,
          meta: {
            requiresAuth: true,
            is_admin: true
          }
        },
        {
          path: "/dash",
          name: "dash",
          component: Dash,
          meta: {
            requiresAuth: true,
            is_admin: true
          }
        }
      ]
    },
    { path: "*", component: NotFound }
  ]
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (localStorage.getItem("jwt") == null) {
      next({
        path: "/login",
        params: { nextUrl: to.fullPath }
      });
    } else {
      let user = JSON.parse(localStorage.getItem("user"));
      if (to.matched.some(record => record.meta.is_admin)) {
        if (user.is_admin == 1) {
          next();
        } else {
          next({ name: "userboard" });
        }
      } else {
        next();
      }
    }
  } else if (to.matched.some(record => record.meta.guest)) {
    if (localStorage.getItem("jwt") == null) {
      next();
    } else {
      next({ name: "userboard" });
    }
  } else {
    next();
  }
});

export default router;

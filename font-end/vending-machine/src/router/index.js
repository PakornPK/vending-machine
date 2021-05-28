import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Login from "../views/Login.vue";
import BuyItems from "../views/BuyItems.vue";
import Admin from "../views/Admin.vue";
import FillProducts from "../views/FillProducts.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/buyitems/:mc",
    name: "BuyItems",
    component: BuyItems,
  },
  {
    path: "/fillproduct/:mc",
    name: "FillProducts",
    component: FillProducts,
  },
  {
    path: "/admin",
    name: "Admin",
    component: Admin,
  },
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "*",
    name: "Home",
    component: Home,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

<template>
  <div>
    <b-nav id="navbar" tabs>
      <img
        align="right"
        id="logo"
        src="../assets/logo.png"
        alt=""
        contain
        height="50px"
        width="50px"
      />
      <b-nav-item to="/dash" exact exact-active-class="active"
        ><b
          ><font size="5"
            ><b-icon icon="columns-gutters" shift-v="-1"></b-icon>
            Dashboard</font
          ></b
        ></b-nav-item
      >
      <b-nav-item to="/register" exact exact-active-class="active"
        ><b
          ><font size="5"
            ><b-icon icon="people" shift-v="-1"></b-icon> Register</font
          ></b
        ></b-nav-item
      >
    </b-nav>
    <b-button
      id="logoutButton"
      squared
      variant="outline-dark"
      size="sm"
      @click="handleLogout"
      >Logout</b-button
    >
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  methods: {
    handleLogout() {
      localStorage.clear();
      this.$router.push("login");
    }
  }
};
</script>

<style scoped>
#logoutButton {
  position: absolute;
  right: 2px;
  top: 2px;
}
#navbar {
  font-family: Agency FB, Helvetica, Arial, sans-serif;
  font-weight: bold;
}
</style>

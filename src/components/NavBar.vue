<template>
  <div>
    <b-nav tabs>
      <img
        align="right"
        id="logo"
        src="../assets/logo.png"
        alt=""
        contain
        height="50px"
        width="50px"
      />
      <b-nav-item to="/home" exact exact-active-class="active"
        ><b
          ><font size="5"
            ><b-icon icon="camera-video" shift-v="-1"></b-icon> Streams</font
          ></b
        ></b-nav-item
      >
      <b-nav-item to="/control" exact exact-active-class="active"
        ><b
          ><font size="5"
            ><b-icon icon="controller" shift-v="-1"></b-icon> Controls</font
          ></b
        ></b-nav-item
      >
      <b-nav-item to="/stats" exact exact-active-class="active"
        ><b
          ><font size="5"
            ><b-icon icon="columns-gutters" shift-v="-1"></b-icon> Stats</font
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
</style>

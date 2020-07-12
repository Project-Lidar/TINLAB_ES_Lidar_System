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
      <b-nav-item to="/map" exact exact-active-class="active"
        ><b
          ><font size="5"
            ><b-icon
              icon="terminal"
              shift-v="1"
              style="width: 25px; height: 25px;"
            ></b-icon>
            Raspberry Pi</font
          ></b
        ></b-nav-item
      >
      <b-nav-item to="/stats" exact exact-active-class="active"
        ><b
          ><font size="5"
            ><b-icon
              icon="columns-gap"
              shift-v="1.5"
              style="width: 23px; height: 23px;"
            ></b-icon>
            Stats</font
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
    <b-button
      id="goBackButton"
      squared
      variant="outline-dark"
      size="sm"
      @click="handleGoBack"
      v-if="show"
      >Go Back</b-button
    >
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data() {
    return {
      show: false,
    };
  },
  methods: {
    handleLogout() {
      localStorage.clear();
      this.$router.push("login");
    },
    handleGoBack() {
      this.$router.push("admin");
    },
  },
  mounted: function() {
    let user = JSON.parse(localStorage.getItem("user"));
    if (user.is_admin == 1) {
      this.show = true;
    } else {
      this.show = false;
    }
  },
};
</script>

<style scoped>
#logoutButton {
  position: absolute;
  right: 2px;
  top: 2px;
}
#goBackButton {
  position: absolute;
  right: 75px;
  top: 2px;
}
#navbar {
  font-family: Agency FB, Helvetica, Arial, sans-serif;
  font-weight: bold;
}
</style>

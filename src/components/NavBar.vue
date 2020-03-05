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
        ><b><font size="5">Home</font></b></b-nav-item
      >
      <b-nav-item disabled to="/control" exact exact-active-class="active"
        ><b><font size="5">Controls</font></b></b-nav-item
      >
    </b-nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {};
</script>

<style scoped></style>

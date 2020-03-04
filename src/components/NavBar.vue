<template>
  <div>
    <b-nav>
      <b-nav-item to="/home" exact exact-active-class="active"
        ><b><font size="5">Home</font></b></b-nav-item
      >
      <b-nav-item to="/control" exact exact-active-class="active"
        ><b><font size="5">Control</font></b></b-nav-item
      >
    </b-nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {};
</script>

<style scoped></style>

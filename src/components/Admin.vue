<template>
  <div class="hello">
    <h1>Welcome to administrator page</h1>
    <h2>{{ msg }}</h2>
    <b-button
      id="logoutButton"
      squared
      variant="outline-dark"
      size="sm"
      @click="handleLogout"
      >Logout</b-button
    >
  </div>
</template>

<script>
export default {
  data() {
    return {
      msg: "The superheroes"
    };
  },
  methods: {
    handleLogout() {
      localStorage.clear();
      this.$router.push("login");
    }
  }
};
</script>
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
#logoutButton {
  position: absolute;
  right: 2px;
  top: 2px;
}
</style>

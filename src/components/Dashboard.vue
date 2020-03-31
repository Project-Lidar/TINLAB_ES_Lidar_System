<template>
  <div>
    <b-button id="goToUserButton" squared variant="dark" @click="goToUser"
      >Go to user page</b-button
    >
  </div>
</template>

<script>
export default {
  methods: {
    goToUser() {
      this.$router.push("/");
    }
  }
};
</script>

<style scoped>
div {
  padding-top: 30px;
  padding-left: 30px;
}
</style>

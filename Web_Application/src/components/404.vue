<template>
  <div>
    <h1>404 Page Not Found</h1>
    <b-button @click="goBack" variant="link">Go to home</b-button>
  </div>
</template>

<script>
export default {
  methods: {
    goBack() {
      this.$router.go(-1);
    }
  }
};
</script>

<style scoped>
div {
  height: 500px;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}
</style>

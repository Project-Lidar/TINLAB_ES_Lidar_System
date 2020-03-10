<template>
  <div>
    <b-row id="container">
      <b-col id="stream">
        <h4 align="left"><b>Camera stream</b></h4>
        <b-embed
          type="iframe"
          aspect="16by9"
          src="http://145.137.65.63:8000/"
        ></b-embed>
      </b-col>

      <b-col id="map">
        <h4 align="left"><b>Thermal camera stream</b></h4>
        <b-embed
          type="iframe"
          aspect="16by9"
          src="https://shiftr.io/BitsNByt3z/Project_Lidar/embed?zoom=1"
        ></b-embed>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
#stream {
  padding-left: 125px;
  padding-right: 75px;
}

#map {
  padding-left: 75px;
  padding-right: 125px;
}

#container {
  padding-top: 25px;
}
</style>

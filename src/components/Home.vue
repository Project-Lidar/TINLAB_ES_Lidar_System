<template>
  <div>
    <b-row id="container">
      <b-col id="stream">
        <h4 align="left"><b>Camera stream</b></h4>
        <b-embed
          type="iframe"
          aspect="16by9"
          src="https://www.youtube.com/embed/8uGS11yuVyo"
        ></b-embed>
      </b-col>
      <b-col id="map">
        <h4 align="left"><b>Lidar map</b></h4>
        <b-embed
          type="iframe"
          aspect="16by9"
          src="https://www.youtube.com/embed/qNdcXUEF7KU"
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

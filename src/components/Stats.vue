<template>
  <div>
    <b-row id="container">
      <b-col id="stream">
        <h4 align="left"><b>Shiftr</b></h4>
        <b-embed
          type="iframe"
          aspect="16by9"
          src="https://shiftr.io/BitsNByt3z/Project_Lidar/embed?zoom=1"
        ></b-embed>
      </b-col>

      <b-col id="map">
        <h4 align="left"><b>Statistics</b></h4>
        <h5 id="BPMTitle" align="left">
          Incoming data from Shiftr: <span>{{ mqtt_data }}</span>
        </h5>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mqtt_data: "null"
    };
  },
  mqtt: {
    sensors(response) {
      this.mqtt_data = response;
    }
  }
};
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

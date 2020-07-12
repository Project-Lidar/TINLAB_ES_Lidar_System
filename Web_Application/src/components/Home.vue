<template>
  <div>
    <b-row id="container">
      <b-col id="stream">
        <h4 align="left"><b>Camera stream</b></h4>
        <b-overlay
          :show="show"
          rounded="sm"
          :variant="variant"
          :opacity="opacity"
          :blur="blur"
        >
          <b-embed
            type="iframe"
            aspect="16by9"
            src="http://145.137.65.63:8000/"
            @load="load"
          ></b-embed>
        </b-overlay>
      </b-col>

      <b-col id="map">
        <h4 align="left"><b>Thermal camera stream</b></h4>
        <b-overlay
          :show="show"
          rounded="sm"
          :variant="variant"
          :opacity="opacity"
          :blur="blur"
        >
          <b-embed type="iframe" aspect="16by9" src="" @load="load"></b-embed>
        </b-overlay>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      show: true,
      opacity: 0.85,
      blur: "2px",
      variant: "transparent",
    };
  },
  methods: {
    load: function() {
      this.show = false;
    },
  },
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

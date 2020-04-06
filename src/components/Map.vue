<template>
  <div>
    <b-card>
      <h4>The robots location: {{ latitude }}, {{ longitude }}</h4>
      <l-map
        ref="myMap"
        style="height: 825px"
        :zoom="zoom"
        :center="center"
        @update:center="centerUpdated"
      >
        <l-tile-layer :url="url"></l-tile-layer>
        <l-marker :lat-lng="markerLatLng"> </l-marker>
      </l-map>
    </b-card>
  </div>
</template>

<script>
import { Icon } from "leaflet";

delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png")
});

export default {
  data() {
    return {
      ipAddress: "",
      dataURL: `http://www.geoplugin.net/json.gp?ip=${this.ipAddress}`,
      latitude: "",
      longitude: "",
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      zoom: 18,
      center: [0, 0],
      markerLatLng: [0, 0]
    };
  },
  mqtt: {
    "location/ip_address"(response) {
      this.ipAddress = response;
    }
  },
  methods: {
    centerUpdated() {
      this.$http
        .get(`http://www.geoplugin.net/json.gp?ip=${this.ipAddress}`)
        .then(response => {
          var lat = response.data.geoplugin_latitude;
          var long = response.data.geoplugin_longitude;
          this.center = [lat, long];
          this.markerLatLng = [lat, long];
          this.latitude = lat;
          this.longitude = long;
        });
    }
  },
  mounted: function() {
    this.centerUpdated();
  }
};
</script>

<style scoped></style>

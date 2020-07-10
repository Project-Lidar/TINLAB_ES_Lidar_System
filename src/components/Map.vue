<template>
  <div>
    <b-card no-body align="center">
      <b-tabs pills card>
        <!-- <b-tab :active="activeTabLidar" title="Lidar">
          <Plotly :data="data" :layout="layout" />
        </b-tab> -->

        <b-tab :active="activeTabLidar" title="Guacamole">
          <iframe
            src="http://192.168.86.30:8080/"
            width="1280"
            height="720"
          ></iframe>
        </b-tab>

        <!-- <b-tab :active="activeTabGps" title="GPS">
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
        </b-tab> -->
      </b-tabs>
    </b-card>
  </div>
</template>

<script>
import { Icon } from "leaflet";
// import { Plotly } from "vue-plotly";

delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
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
      markerLatLng: [0, 0],
      activeTabGps: false,
      activeTabLidar: true,
      show: true,
      measures: [],
      splites: "",
      measuredR: [],
      measuredTheta: [],
      data: [
        {
          r: [1000, 1200, 1700, 750, 2400, 20000],
          theta: [0, 30, 45, 90, 180, 270],
          mode: "lines",
          name: "lidar_simulation",
          line: { color: "red" },
          type: "scatterpolar",
          // x: [1, 2, 3, 4, 5],
          // y: [1, 6, 3, 6, 1],
          // mode: 'markers',
          // type: 'scatter',
          // name: 'bléré',
          // text: ['A-1', 'A-2', 'A-3', 'A-4', 'A-5'],
          // marker: {size: 12}
        },
      ],
      layout: {
        //width: 500,
        height: 600,
        autosize: true,
        xaxis: {
          range: [0.75, 5.25],
        },
        yaxis: { range: [-8, 8] },
        title: "Measures LiDAR",
      },
    };
  },
  components: {
    // Plotly,
  },
  mqtt: {
    "location/ip_address"(response) {
      this.ipAddress = response;
    },
    lidar(response) {
      this.splitStrings(response.toString());
    },
  },
  methods: {
    centerUpdated() {
      this.$http
        .get(`http://www.geoplugin.net/json.gp?ip=${this.ipAddress}`)
        .then((response) => {
          var lat = response.data.geoplugin_latitude;
          var long = response.data.geoplugin_longitude;
          this.center = [lat, long];
          this.markerLatLng = [lat, long];
          this.latitude = lat;
          this.longitude = long;
        });
    },

    setMeasuresPlotly: function(datas) {
      let r = [];
      let theta = [];
      datas.forEach(function(element) {
        theta.push(element[0]);
        r.push(element[1]);
      });

      // this.measuredR.push(parseFloat(datas[3]));
      // console.log("R: " + this.measuredR);
      // this.measuredTheta.push(parseFloat(datas[2]));
      // console.log("Theta: " + this.measuredTheta);
      this.data = [
        {
          r: r,
          theta: theta,
          mode: "markers",
          marker: {
            color: "rgb(0,0,0)",
            size: 5,
          },
          name: "lidar_simulation",
          line: { color: "red" },
          type: "scatterpolar",
        },
      ];
      // console.log(this.data);
    },

    splitStrings: function(data) {
      this.splites = data.split(",");
      // console.log("Splites: " + this.splites[2]);
      this.setMeasuresPlotly(this.splites);
    },
  },
  mounted: function() {
    this.centerUpdated();
  },
};
</script>

<style scoped></style>

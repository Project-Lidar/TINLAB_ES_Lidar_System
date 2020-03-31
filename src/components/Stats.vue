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
        <p>Must be logged into shiftr.io to load the content.</p>
        <p align="left">
          Press assigned gamepad buttons to test input connection with the
          broker.
        </p>
      </b-col>

      <b-col id="map">
        <h4 align="left"><b>Statistics</b></h4>
        <h5 id="BPMTitle" align="left">
          Incoming data from Shiftr: <span>{{ mqtt_data }}</span>
        </h5>
      </b-col>
    </b-row>
    <ul
      v-gamepad:button-a="publishController_A"
      v-gamepad:trigger-right="publishController_A"
      v-gamepad:button-b="publishController_B"
      v-gamepad:trigger-left="publishController_B"
      v-gamepad:button-dpad-left="publishController_Left"
      v-gamepad:button-dpad-right="publishController_Right"
      v-gamepad:left-analog-left.repeat="publishController_Joy_Left"
      v-gamepad:left-analog-right.repeat="publishController_Joy_Right"
    ></ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mqtt_data: "null",
      button: "",
      joy: 0
    };
  },
  mqtt: {
    sensors(response) {
      this.mqtt_data = response;
    },
    "controls/manual/controller/steer"(data, topic) {
      console.log(topic + ": " + String.fromCharCode.apply(null, data));
    },
    "controls/manual/controller/speed"(data, topic) {
      console.log(topic + ": " + String.fromCharCode.apply(null, data));
    }
  },
  methods: {
    publishController_A() {
      this.button = "Acceleration(X/R2) is pressed";
      this.$mqtt.publish("controls/manual/controller/speed", this.button);
    },
    publishController_B() {
      this.button = "Brake(O/L2) is pressed";
      this.$mqtt.publish("controls/manual/controller/speed", this.button);
    },
    publishController_Left() {
      this.button = "D-pad Left is pressed";
      this.$mqtt.publish("controls/manual/controller/steer", this.button);
    },
    publishController_Right() {
      this.button = "D-pad Right is pressed";
      this.$mqtt.publish("controls/manual/controller/steer", this.button);
    },
    publishController_Joy_Left() {
      this.joy--;
      this.$mqtt.publish("controls/manual/controller/steer", String(this.joy));
      this.joy = 0;
    },
    publishController_Joy_Right() {
      this.joy++;
      this.$mqtt.publish("controls/manual/controller/steer", String(this.joy));
      this.joy = 0;
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

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

      <b-col align="left" id="controls">
        <h4><b>Controls</b></h4>

        <b-form-group>
          <b-form-radio
            v-model="selected"
            v-on:change="publish"
            name="some-radios"
            value="M"
            >Autonomous driving</b-form-radio
          >
          <b-form-radio
            v-model="selected"
            v-on:change="publish"
            name="some-radios"
            value="A"
            >Manual driving</b-form-radio
          >
        </b-form-group>
        <h4><b>Manual controls</b></h4>
        <b-button
          squared
          v-on:click="publishController_A"
          v-gamepad:button-a="publishController_A"
          v-gamepad:trigger-right="publishController_A"
          >X</b-button
        >
        <b-button
          squared
          v-on:click="publishController_O"
          v-gamepad:button-b="publishController_O"
          v-gamepad:trigger-left="publishController_O"
          >O</b-button
        >
        <b-button
          squared
          v-on:click="publishController_Left"
          v-gamepad:button-dpad-left="publishController_Left"
          >left</b-button
        >
        <b-button
          squared
          v-on:click="publishController_Right"
          v-gamepad:button-dpad-right="publishController_Right"
          >right</b-button
        >
        <b-button
          squared
          v-on:click="publishController_Joy_Left"
          v-gamepad:left-analog-left.repeat="publishController_Joy_Left"
          >Joy Left</b-button
        >
        <b-button
          squared
          v-on:click="publishController_Joy_Right"
          v-gamepad:left-analog-right.repeat="publishController_Joy_Right"
          >Joy Right</b-button
        >
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selected: "M",
      button: "",
      joy: 0
    };
  },
  methods: {
    publish() {
      this.$mqtt.publish("controls/driving", this.selected);
    },
    publishController_A() {
      this.button = "Acceleration(X/R2) is pressed";
      this.$mqtt.publish("controls/manual/controller", this.button);
    },
    publishController_O() {
      this.button = "Brake(O/L2) is pressed";
      this.$mqtt.publish("controls/manual/controller", this.button);
    },
    publishController_Left() {
      this.button = "D-pad Left is pressed";
      this.$mqtt.publish("controls/manual/controller", this.button);
    },
    publishController_Right() {
      this.button = "D-pad Right is pressed";
      this.$mqtt.publish("controls/manual/controller", this.button);
    },
    publishController_Joy_Left() {
      this.joy--;
      this.$mqtt.publish("controls/manual/controller", String(this.joy));
      this.joy = 0;
    },
    publishController_Joy_Right() {
      this.joy++;
      this.$mqtt.publish("controls/manual/controller", String(this.joy));
      this.joy = 0;
    }
  },
  mqtt: {
    "controls/driving"(data, topic) {
      console.log(topic + ": " + String.fromCharCode.apply(null, data));
    },
    "controls/manual/controller"(data, topic) {
      console.log(topic + ": " + String.fromCharCode.apply(null, data));
    }
  }
};
</script>

<style scoped>
#stream {
  padding-left: 50px;
}

#controls {
  padding-top: 10px;
  padding-left: 75px;
}

#container {
  padding-top: 25px;
}
</style>

<template>
  <div>
    <b-row id="container">
      <b-col id="stream">
        <div>
          <b-card no-body>
            <b-tabs pills card>
              <b-tab :active="activeTabCam" title="Camera">
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
              </b-tab>
              <b-tab :active="activeTabTherm" title="Thermal camera">
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
                  ></b-embed
                ></b-overlay>
              </b-tab>
            </b-tabs>
          </b-card>
        </div>
      </b-col>

      <b-col align="left" id="controls">
        <h4><b>Driving Controls</b></h4>

        <b-form-group>
          <b-form-radio
            v-model="selected"
            v-on:change="
              publish();
              toggler();
            "
            name="some-radios"
            value="M"
            >Autonomous driving</b-form-radio
          >
          <b-form-radio
            v-model="selected"
            v-on:change="
              publish();
              toggler();
            "
            name="some-radios"
            value="A"
            >Manual driving</b-form-radio
          >
        </b-form-group>

        <h4 id="manualControlTitle"><b>Manual controls</b></h4>
        <h5 id="touchControls"><b>Touch/Click Controls</b></h5>

        <b-button
          id="x-button"
          :class="{ active: interval }"
          @mousedown="startA"
          @mouseleave="stop"
          @mouseup="stop"
          @touchstart="startA"
          @touchend="stop"
          @touchcancel="stop"
          squared
          variant="dark"
          size="lg"
          :disabled="manualToggle"
          v-on:click="publishButton_A"
          v-gamepad:button-a="publishController_A"
          v-gamepad:trigger-right="publishController_A"
          ><b-icon icon="x" shift-v="-1.5"></b-icon
        ></b-button>

        <b-button
          id="o-button"
          :class="{ active: interval }"
          @mousedown="startB"
          @mouseleave="stop"
          @mouseup="stop"
          @touchstart="startB"
          @touchend="stop"
          @touchcancel="stop"
          squared
          size="lg"
          :disabled="manualToggle"
          v-on:click="publishButton_B"
          v-gamepad:button-b="publishController_B"
          v-gamepad:trigger-left="publishController_B"
          ><b-icon icon="circle" shift-v="-1.5"></b-icon
        ></b-button>

        <b-button
          id="v-button"
          :class="{ active: interval }"
          @mousedown="startV"
          @mouseleave="stop"
          @mouseup="stop"
          @touchstart="startV"
          @touchend="stop"
          @touchcancel="stop"
          squared
          variant="dark"
          size="lg"
          :disabled="manualToggle"
          v-on:click="publishButton_V"
          v-gamepad:button-x="publishController_V"
          ><b-icon icon="square" shift-v="-0.5"></b-icon
        ></b-button>

        <b-button
          id="left-button"
          :class="{ active: interval }"
          @mousedown="startL"
          @mouseleave="stop"
          @mouseup="stop"
          @touchstart="startL"
          @touchend="stop"
          @touchcancel="stop"
          squared
          size="lg"
          :disabled="manualToggle"
          v-on:click="publishButton_Left"
          v-gamepad:button-dpad-left="publishController_Left"
          ><b-icon icon="arrow-left" shift-v="-1.5"></b-icon
        ></b-button>

        <b-button
          id="right-button"
          :class="{ active: interval }"
          @mousedown="startR"
          @mouseleave="stop"
          @mouseup="stop"
          @touchstart="startR"
          @touchend="stop"
          @touchcancel="stop"
          squared
          variant="dark"
          size="lg"
          :disabled="manualToggle"
          v-on:click="publishButton_Right"
          v-gamepad:button-dpad-right="publishController_Right"
          ><b-icon icon="arrow-right" shift-v="-1.5"></b-icon
        ></b-button>

        <ul
          v-gamepad:left-analog-left.repeat="publishController_Joy_Left"
          v-gamepad:left-analog-right.repeat="publishController_Joy_Right"
          v-gamepad:shoulder-right="tabToggleToTherm"
          v-gamepad:shoulder-left="tabToggleToCam"
        ></ul>

        <p id="ConnectGamepadTitle">
          <b-icon icon="controller" shift-v="-4" font-scale="2.5"></b-icon>:
          <span>{{ connectedGamepad }}</span>
        </p>

        <h5><b>Gamepad Controls</b></h5>

        <p>
          R2 /<b-icon icon="x" shift-v="-1.5" font-scale="1.5"></b-icon>:
          Acceleration
        </p>

        <p>
          L2 / <b-icon icon="circle" shift-v="1.5" font-scale="1"></b-icon> :
          Brake
        </p>

        <p>
          <b-icon icon="square" shift-v="1.5" font-scale="1"></b-icon> : Reverse
        </p>

        <p>
          Left d-pad /
          <b-icon icon="arrow-left" shift-v="-1.7" font-scale="1.7"></b-icon>:
          Steer left
        </p>

        <p>
          Right d-pad /
          <b-icon icon="arrow-right" shift-v="-1.7" font-scale="1.7"></b-icon>:
          Steer right
        </p>
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
      joy: 0,
      connectedGamepad: "Disconnected",
      manualToggle: true,
      interval: false,
      activeTabCam: true,
      activeTabTherm: false,
      show: true,
      opacity: 0.85,
      blur: "2px",
      variant: "transparent",
    };
  },
  methods: {
    publish() {
      this.$mqtt.publish("controls/driving", this.selected);
    },
    publishController_A() {
      this.button = "D";
      this.$mqtt.publish("controls/manual/controller/speed", this.button);
      this.connectedGamepad = "Connected";
    },
    publishController_B() {
      this.button = "B";
      this.$mqtt.publish("controls/manual/controller/speed", this.button);
      this.connectedGamepad = "Connected";
    },
    publishController_V() {
      this.button = "R";
      this.$mqtt.publish("controls/manual/controller/speed", this.button);
      this.connectedGamepad = "Connected";
    },
    publishController_Left() {
      this.button = "L";
      this.$mqtt.publish("controls/manual/controller/steer", this.button);
      this.connectedGamepad = "Connected";
    },
    publishController_Right() {
      this.button = "R";
      this.$mqtt.publish("controls/manual/controller/steer", this.button);
      this.connectedGamepad = "Connected";
    },
    publishController_Joy_Left() {
      this.joy--;
      this.$mqtt.publish("controls/manual/controller/steer", String(this.joy));
      this.joy = 0;
      this.connectedGamepad = "Connected";
    },
    publishController_Joy_Right() {
      this.joy++;
      this.$mqtt.publish("controls/manual/controller/steer", String(this.joy));
      this.joy = 0;
      this.connectedGamepad = "Connected";
    },
    publishButton_A() {
      this.button = "D";
      this.$mqtt.publish("controls/manual/controller/speed", this.button);
    },
    publishButton_B() {
      this.button = "B";
      this.$mqtt.publish("controls/manual/controller/speed", this.button);
    },
    publishButton_V() {
      this.button = "R";
      this.$mqtt.publish("controls/manual/controller/speed", this.button);
    },
    publishButton_Left() {
      this.button = "L";
      this.$mqtt.publish("controls/manual/controller/steer", this.button);
    },
    publishButton_Right() {
      this.button = "R";
      this.$mqtt.publish("controls/manual/controller/steer", this.button);
    },
    toggler() {
      if (this.manualToggle == true) {
        this.manualToggle = false;
      } else if (this.manualToggle == false) {
        this.manualToggle = true;
      }
    },
    tabToggleToTherm() {
      if (this.activeTabCam == true) {
        this.activeTabCam = false;
        this.activeTabTherm = true;
      }
    },
    tabToggleToCam() {
      if (this.activeTabTherm == true) {
        this.activeTabTherm = false;
        this.activeTabCam = true;
      }
    },
    startA() {
      if (!this.interval) {
        this.interval = setInterval(() => this.publishButton_A(), 30);
      }
    },
    startB() {
      if (!this.interval) {
        this.interval = setInterval(() => this.publishButton_B(), 30);
      }
    },
    startV() {
      if (!this.interval) {
        this.interval = setInterval(() => this.publishButton_V(), 30);
      }
    },
    startL() {
      if (!this.interval) {
        this.interval = setInterval(() => this.publishButton_Left(), 30);
      }
    },
    startR() {
      if (!this.interval) {
        this.interval = setInterval(() => this.publishButton_Right(), 30);
      }
    },
    stop() {
      clearInterval(this.interval);
      this.interval = false;
    },
    load: function() {
      this.show = false;
    },
  },
  mqtt: {
    "controls/driving"(data, topic) {
      console.log(topic + ": " + String.fromCharCode.apply(null, data));
    },
    "controls/manual/controller/steer"(data, topic) {
      console.log(topic + ": " + String.fromCharCode.apply(null, data));
    },
    "controls/manual/controller/speed"(data, topic) {
      console.log(topic + ": " + String.fromCharCode.apply(null, data));
    },
  },
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

#manualControlTitle {
  padding-top: 30px;
  padding-bottom: 10px;
}

#touchControls {
  padding-bottom: 25px;
}

#ConnectGamepadTitle {
  padding-top: 20px;
}

#testb {
  user-select: none;
}
</style>

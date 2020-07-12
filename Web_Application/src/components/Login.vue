<template>
  <div>
    <b-container>
      <h1>Project Lidar</h1>

      <img
        id="sidebarLogo"
        src="../assets/logo.png"
        alt=""
        contain
        height="200px"
        width="200px"
      />

      <b-row align-h="center" class="mt-5">
        <b-col cols="7">
          <b-card id="formCard" class="p-3">
            <!-- Login form -->
            <b-form @submit="handleSubmit" v-if="show">
              <b-form-group
                id="input-group-1"
                label-cols-sm="4"
                label-cols-lg="3"
                label="Email:"
                label-for="input-1"
              >
                <b-form-input
                  id="input-1"
                  v-model="form.email"
                  required
                  placeholder="Enter email"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-group-2"
                label-cols-sm="4"
                label-cols-lg="3"
                label="Password:"
                label-for="input-2"
              >
                <b-form-input
                  id="input-2"
                  v-model="form.password"
                  type="password"
                  required
                  placeholder="Enter password"
                ></b-form-input>
              </b-form-group>

              <div align="right">
                <b-button type="submit" variant="primary">Submit</b-button>
              </div>
            </b-form>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        email: "",
        password: "",
      },
      show: true,
    };
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      if (this.form.password.length > 0) {
        this.$http
          .post("http://localhost:3000/api/login", {
            email: this.form.email,
            password: this.form.password,
          })
          .then((response) => {
            let is_admin = response.data.user.is_admin;
            localStorage.setItem("user", JSON.stringify(response.data.user));
            localStorage.setItem("jwt", response.data.token);

            if (localStorage.getItem("jwt") != null) {
              this.$emit("loggedIn");
              if (this.$route.params.nextUrl != null) {
                this.$router.push(this.$route.params.nextUrl);
              } else {
                if (is_admin == 1) {
                  this.$router.push("admin");
                } else {
                  this.$router.push("/");
                }
              }
            }
          })
          .catch(function(error) {
            console.error(error.response);
          });
      }
    },
  },
};
</script>

<style scoped>
#formCard {
  border: none;
}

h1 {
  font-family: Agency FB, Helvetica, Arial, sans-serif;
  font-weight: bold;
  text-align: left;
  padding-top: 20px;
}

#sidebarLogo {
  position: absolute;
  left: 385px;
}
</style>

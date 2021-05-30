<template>
  <v-container fill-height fluid>
    <v-row align="center" justify="center">
      <v-card width="400">
        <v-card-text>
          <v-form @submit.prevent="onSubmit">
            <v-text-field
              label="Username"
              v-model="account.username"
              auto-grow
              outlined
              autofocus
            />
            <v-text-field
              :type="isShowPassword ? 'text' : 'password'"
              label="Password"
              v-model="account.password"
              auto-grow
              outlined
            />
            <v-row class="mb-3 px-5" justify="end">
              <br />
            </v-row>
            <v-row class="justify-end">
              <v-btn type="submit" class="ma-2" color="yellow">login</v-btn>
            </v-row>
          </v-form>
        </v-card-text>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios"
export default {
  name: "Login",
  data() {
    return {
      res: {},
      account: {
        username: "",
        password: ""
      },
    };
  },
  methods: {
    onSubmit() {
      // this.$router.push("/admin");
      axios.post('http://127.0.0.1:5000/api/v1/login',this.account).then(response => {
        this.res = response.data
        if(this.res.result == "Ok" ){
          this.$router.push("/admin");
        }else{ 
          alert(this.res.result)
        }
      })
    },
  },
};
</script>

<style scoped>
.textHead {
  text-align: center;
  margin-bottom: 0;
  padding-bottom: 0;
  font-size: 50px;
  text-transform: uppercase;
}
.textSub {
  text-align: end;
  font-weight: 400;
  padding-top:0;
  padding-right: 50px;
  margin-top: 0;
}
</style>
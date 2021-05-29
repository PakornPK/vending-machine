<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12" md="4" xl="4">
        <Machine
          :src="machine[0].src"
          :location="machine[0].location"
          selector="1"
        />
      </v-col>
      <v-col cols="12" md="4" xl="4">
        <Machine
          :src="machine[1].src"
          :location="machine[1].location"
          selector="2"
        />
      </v-col>
      <v-col cols="12" md="4" xl="4">
        <Machine
          :src="machine[2].src"
          :location="machine[2].location"
          selector="3"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios"
import Machine from "@/components/machines/machine";
export default {
  name: "Home",

  components: {
    Machine,
  },
  methods : {
    getMachines(){
      axios.get("http://127.0.0.1:5000/api/v1/machine").then(response => {
        this.machine = response.data
      })
    },
  },
  mounted() {
    this.getMachines()
  },
  data() {
    return {
      machine: [],
    };
  },
};
</script>

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
import Machine from "@/components/machines/machine";
export default {
  name: "Home",

  components: {
    Machine,
  },
  data() {
    return {
      machine: [
        {
          location: "หน้าโรงงาน",
          src:
            "https://www.scg.com/images/th/05sustainability_development/develop/env2.jpg",
        },
        {
          location: "หน้าโรงเรียน",
          src: "http://teen.mthai.com/app/uploads/2015/12/bbpschool-okkk.jpg",
        },
        {
          location: "หน้าโรงพยบาล",
          src:
            "https://ww2.bangkokhospital.com/assets/theme/bangkok/assets/images/corparate/thumb_xs.jpg",
        },
      ],
    };
  },
};
</script>

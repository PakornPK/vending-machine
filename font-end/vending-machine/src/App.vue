<template>
  <v-app>
    <Header />
    <Contents />
  </v-app>
</template>

<script>
import Header from "@/components/core/Header"
import Contents from "@/components/core/Contents";
export default {
  name: "App",
  components: {
    Header,
    Contents,
  },
  data: () => ({
    //
  }),
};
</script>

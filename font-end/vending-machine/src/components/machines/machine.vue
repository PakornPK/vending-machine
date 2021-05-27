<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card>
          <v-img
            :src="src"
            class="white--text align-end"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            height="200"
            width="max-width"
          >
            <v-card-title v-text="location" />
          </v-img>
          <v-card-actions>
              <v-btn color="yellow" @click="goBuyItems(selector)">
                  ซื้อสินค้า
              </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "machine",
  props: ["location", "src","selector"],
  methods:{ 
      goBuyItems(mc){
          this.$router.push(`/buyitems/${mc}`)
      }
  }
};
</script>

<style>
</style>
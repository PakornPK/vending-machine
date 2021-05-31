<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card hover height="400" class="card-outter">
          <v-img
            :src="src"
            class="white--text align-end"
            max-height="204"
            max-width="250"
          >
          </v-img>

          <v-card-title v-text="name" />
          <v-card-subtitle  v-text="price" />

          <v-card-text>
            <div>
              <p>In Stock : {{stock}}</p>
            </div>
          </v-card-text>

          <v-card-actions class="card-actions">
            <v-btn rounded  color="yellow" @click="buyProduct">
              ซื้อสินค้าชิ้นนี้
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios"
export default {
  name: "product",
  props: ["id","name", "src", "price","stock"],
  methods: {
    buyProduct() {
      axios.post(`http://127.0.0.1:5000/api/v1/buy/${this.$route.params.mc}/${this.id}`,{}).then(response => {
        this.res = response.data
        if(this.res.result == "Ok" ){
          alert("bought")
          location.reload()
        }else{ 
          alert(this.res.result)
        }
      })
    }
  },
  data() {
    return { 
      res: null
    }
  }
};
</script>

<style scoped>
.card-actions {
  position: absolute;
  bottom: 0;
}
.card-outter {
  position: relative;
  padding-bottom: 50px;
}
</style>
<template>
  <v-container>
    <v-row>
      <v-col cols="3">
        <Product
          :src="srcProduct[0].src"
          :name="srcProduct[0].name"
          :price="srcProduct[0].price"
          :stock="srcProduct[0].stock"
        />
      </v-col>
      <v-col cols="3">
        <Product
          :src="srcProduct[1].src"
          :name="srcProduct[1].name"
          :price="srcProduct[1].price"
          :stock="srcProduct[1].stock"
        />
      </v-col>
      <v-col cols="3">
        <Product
          :src="srcProduct[2].src"
          :name="srcProduct[2].name"
          :price="srcProduct[2].price"
          :stock="srcProduct[2].stock"
        />
      </v-col>
      <v-col cols="3">
        <Product
          :src="srcProduct[3].src"
          :name="srcProduct[3].name"
          :price="srcProduct[3].price"
          :stock="srcProduct[3].stock"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3">
        <Product
          :src="srcProduct[4].src"
          :name="srcProduct[4].name"
          :price="srcProduct[4].price"
          :stock="srcProduct[4].stock"
        />
      </v-col>
      <v-col cols="3">
        <Product
          :src="srcProduct[5].src"
          :name="srcProduct[5].name"
          :price="srcProduct[5].price"
          :stock="srcProduct[5].stock"
        />
      </v-col>
      <v-col cols="3">
        <Product
          :src="srcProduct[6].src"
          :name="srcProduct[6].name"
          :price="srcProduct[6].price"
          :stock="srcProduct[6].stock"
        />
      </v-col>
      <v-col cols="3">
        <Product
          :src="srcProduct[7].src"
          :name="srcProduct[7].name"
          :price="srcProduct[7].price"
          :stock="srcProduct[7].stock"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios"
import Product from "@/components/products/product";
export default {
  name: "Home",

  components: {
    Product,
  },
  mounted(){ 
    this.getProducts()
  },
  methods: { 
    getProducts(){
      axios.get("http://127.0.0.1:5000/api/v1/product").then(response => {
        this.srcProduct = response.data
      })
    }
  }, 
  data() {
    return {
      srcProduct: [],
    };
  },
};
</script>

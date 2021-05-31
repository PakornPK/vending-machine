<template>
  <v-container>
    <v-row>
      <v-col cols="3">
        <Product
          id="1"
          src="https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12075425/51021628_P.jpg"
          :name="srcProduct[0].name"
          :price="srcProduct[0].price"
          :stock="srcProduct[0].stock"
        />
      </v-col>
      <v-col cols="3">
        <Product
          id="2"
          src="https://cpfmcdn.bygodigit.net/wp-content/uploads/2018/03/06112105/51009434_P.jpg"
          :name="srcProduct[1].name"
          :price="srcProduct[1].price"
          :stock="srcProduct[1].stock"
        />
      </v-col>
      <v-col cols="3">
        <Product
          id="3"
          src="https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12075341/51011628_P.jpg"
          :name="srcProduct[2].name"
          :price="srcProduct[2].price"
          :stock="srcProduct[2].stock"
        />
      </v-col>
      <v-col cols="3">
        <Product
          id="4"
          src="https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12075429/51021847_P.jpg"
          :name="srcProduct[3].name"
          :price="srcProduct[3].price"
          :stock="srcProduct[3].stock"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3">
        <Product
          id="5"
          src="https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12222505/51010586_P.jpg"
          :name="srcProduct[4].name"
          :price="srcProduct[4].price"
          :stock="srcProduct[4].stock"
        />
      </v-col>
      <v-col cols="3">
        <Product
          id="6"
          src="https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12222438/51008429_P.jpg"
          :name="srcProduct[5].name"
          :price="srcProduct[5].price"
          :stock="srcProduct[5].stock"
        />
      </v-col>
      <v-col cols="3">
        <Product
          id="7"
          src="https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12222756/51033939_P.jpg"
          :name="srcProduct[6].name"
          :price="srcProduct[6].price"
          :stock="srcProduct[6].stock"
        />
      </v-col>
      <v-col cols="3">
        <Product
          id="8"
          src="https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12222141/51037887_P.jpg"
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
      axios.get(`http://127.0.0.1:5000/api/v1/product/${this.$route.params.mc}`).then(response => {
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

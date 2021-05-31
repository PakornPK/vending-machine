<template>
  <v-container>
    <v-row justify="center">
      <v-col>
        <v-card>
          <v-data-table
            :headers="headers"
            :items="products"
            :items-per-page="10"
            class="elevation-1"
          >
            <template v-slot:item="{ item }">
              <tr>
                <td>{{ item.id }}</td>
                <td>{{ item.name }}</td>
                <td>{{ item.unit_price }}</td>
                <td>{{ item.stock }}</td>
                <td>{{ item.reload }}</td>
                <td>
                  <v-btn class="mr-2" color="yellow" @click="fillProduct(item)">
                    เติมสินค้า
                  </v-btn>
                </td>
              </tr>
            </template>
          </v-data-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios"
export default {
  name: "admin",
  mounted() { 
    this.getData()
  },
  methods: { 
    fillProduct(item){
      axios.post(`http://127.0.0.1:5000/api/v1/fill/${this.$route.params.mc}/${item.id}`,{}).then(response => {
        this.res = response.data
        if(this.res.result == "Ok" ){
          this.getData()
        }else{ 
          alert(this.res.result)
        }
      })
    },
    getData(){
      axios.get(`http://127.0.0.1:5000/api/v1/fillproduct/${this.$route.params.mc}`).then(response => {
        this.products = response.data
      })
    }
  },
  data() {
    return {
      res: null,
      headers: [
        {
          text: "รหัสสินค้า",
          align: "start",
          sortable: false,
          value: "id",
        },
        { text: "ชื่อสินค้า", value: "name" },
        { text: "ราคา", value: "price" },
        { text: "จำนวน", value: "qty" },
        { text: "ต้องเติมสินค้า", value: "reload" },
        { text: "เติมสินค้า", value: "fill" },
      ],
      products: [],
    };
  },
};
</script>
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
                <td>{{ item.categorie }}</td>
                <td>{{ item.price }}</td>
                <td>{{ item.qty }}</td>
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
    getData(){
      axios.get("http://127.0.0.1:5000/api/v1/fillproduct").then(response => {
        this.products = response.data
      })
    }
  },
  data() {
    return {
      headers: [
        {
          text: "รหัสสินค้า",
          align: "start",
          sortable: false,
          value: "id",
        },
        { text: "ชื่อสินค้า", value: "name" },
        { text: "ประเภทสินค้า", value: "categorie" },
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
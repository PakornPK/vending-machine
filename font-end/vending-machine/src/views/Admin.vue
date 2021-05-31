<template>
  <v-container>
    <v-row justify="center">
      <v-col>
        <v-card>
          <v-data-table
            :headers="headers"
            :items="machines"
            :items-per-page="10"
            class="elevation-1"
          >
            <template v-slot:item="{ item }">
              <tr>
                <td>{{ item.id }}</td>
                <td>{{ item.location }}</td>
                <td>{{ item.balance }}</td>
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
import axios from "axios";
export default {
  name: "admin",
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      axios.get("http://127.0.0.1:5000/api/v1/machine").then((response) => {
        this.machines = response.data;
      });
    },
    fillProduct(item) {
      this.$router.push(`/fillproduct/${item.id}`)
    },
  },
  data() {
    return {
      headers: [
        {
          text: "ลำดับ",
          align: "start",
          sortable: false,
          value: "id",
        },
        { text: "สถานที่", value: "location" },
        { text: "ยอดขาย", value: "balance" },
        { text: "ต้องเติมสินค้า", value: "reload" },
        { text: "ดูรายละเอียด", value: "info" },
      ],
      machines: [],
    };
  },
};
</script>
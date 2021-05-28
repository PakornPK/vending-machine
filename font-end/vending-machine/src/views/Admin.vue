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
export default {
  name: "admin",
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
      machines: [
        {
          id: 1,
          location: "หน้าโรงงาน",
          balance: 0,
          reload: false,
        },
        {
          id: 2,
          location: "หน้าโรงเรียน",
          balance: 0,
          reload: false,
        },
        {
          id: 3,
          location: "หน้าโรงพยบาล",
          balance: 0,
          reload: false,
        },
      ],
    };
  },
  methods: { 
    fillProduct(item){ 
      this.$router.push(`/fillproduct/${item.id}`)
    }
  }
};
</script>
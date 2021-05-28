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
export default {
  name: "admin",
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
      products: [
        {
          id: 1,
          name: "นกพิราบผักกาดดองเค็มฝาดึง 230 กรัม",
          categorie: "อาหารกระป๋อง",
          price: "฿32.00",
          qty: 10,
          reload: false,
        },
        {
          id: 2,
          name: "ซีเล็คทูน่าสเต็กในน้ำเกลือ 165 กรัม",
          categorie: "อาหารกระป๋อง",
          price: "฿49.00",
          qty: 10,
          reload: false,
        },
        {
          id: 3,
          name: "อะยัมซาร์ดีนในซอสมะเขือเทศ 155 กรัม",
          categorie: "อาหารกระป๋อง",
          price: "฿36.00",
          qty: 10,
          reload: false,
        },
        {
          id: 4,
          name: "ยูเอฟซี เงาะในน้ำเชื่อม 565 กรัม",
          categorie: "อาหารกระป๋อง",
          price: "฿82.00",
          qty: 10,
          reload: false,
        },
        {
          id: 5,
          name: "เอ็ม-150 150 มิลลิลิตร",
          categorie: "เครื่องดื่ม",
          price: "฿10.00",
          qty: 10,
          reload: false,
        },
        {
          id: 6,
          name: "สปอนเซอร์ 250 มิลลิลิตร",
          categorie: "เครื่องดื่ม",
          price: "฿10.00",
          qty: 10,
          reload: false,
        },
        {
          id: 7,
          name: "ลิปตัน เลมอนขวด 445 มิลลิลิตร",
          categorie: "เครื่องดื่ม",
          price: "฿20.00",
          qty: 10,
          reload: false,
        },
        {
          id: 7,
          name: "จับใจ สูตรจับเลี้ยง 500 มิลลิลิตร",
          categorie: "เครื่องดื่ม",
          price: "฿15.00",
          qty: 10,
          reload: false,
        },
      ],
    };
  },
};
</script>
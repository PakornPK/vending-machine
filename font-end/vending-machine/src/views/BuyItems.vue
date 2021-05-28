<template>
  <v-container>
    <v-row>
      <v-col cols="3">
        <Product
          :src="srcProduct[0].src"
          :name="srcProduct[0].name"
          :price="srcProduct[0].price"
        />
      </v-col>
      <v-col cols="3">
        <Product
          :src="srcProduct[1].src"
          :name="srcProduct[1].name"
          :price="srcProduct[1].price"
        />
      </v-col>
      <v-col cols="3">
        <Product
          :src="srcProduct[2].src"
          :name="srcProduct[2].name"
          :price="srcProduct[2].price"
        />
      </v-col>
      <v-col cols="3">
        <Product
          :src="srcProduct[3].src"
          :name="srcProduct[3].name"
          :price="srcProduct[3].price"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3">
        <Product
          :src="srcProduct[4].src"
          :name="srcProduct[4].name"
          :price="srcProduct[4].price"
        />
      </v-col>
      <v-col cols="3">
        <Product
          :src="srcProduct[5].src"
          :name="srcProduct[5].name"
          :price="srcProduct[5].price"
        />
      </v-col>
      <v-col cols="3">
        <Product
          :src="srcProduct[6].src"
          :name="srcProduct[6].name"
          :price="srcProduct[6].price"
        />
      </v-col>
      <v-col cols="3">
        <Product
          :src="srcProduct[7].src"
          :name="srcProduct[7].name"
          :price="srcProduct[7].price"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Product from "@/components/products/product";
export default {
  name: "Home",

  components: {
    Product,
  },
  mounted(){ 
    this.welcome()
  },
  methods: { 
    welcome(){
      alert("Test")
    },
  }, 
  data() {
    return {
      srcProduct: [
        {
          src:
            "https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12075425/51021628_P.jpg",
          name: "นกพิราบผักกาดดองเค็มฝาดึง 230 กรัม",
          price: "฿32.00",
        },
        {
          src:
            "https://cpfmcdn.bygodigit.net/wp-content/uploads/2018/03/06112105/51009434_P.jpg",
          name: "ซีเล็คทูน่าสเต็กในน้ำเกลือ 165 กรัม",
          price: "฿49.00",
        },
        {
          src:
            "https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12075341/51011628_P.jpg",
          name: "อะยัมซาร์ดีนในซอสมะเขือเทศ 155 กรัม",
          price: "฿36.00",
        },
        {
          src:
            "https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12075429/51021847_P.jpg",
          name: "ยูเอฟซี เงาะในน้ำเชื่อม 565 กรัม",
          price: "฿82.00",
        },
        {
          src:
            "https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12222505/51010586_P.jpg",
          name: "เอ็ม-150 150 มิลลิลิตร",
          price: "฿10.00",
        },
        {
          src:
            "https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12222438/51008429_P.jpg",
          name: "สปอนเซอร์ 250 มิลลิลิตร",
          price: "฿10.00",
        },
        {
          src:
            "https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12222756/51033939_P.jpg",
          name: "ลิปตัน เลมอนขวด 445 มิลลิลิตร",
          price: "฿20.00",
        },
        {
          src:
            "https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12222141/51037887_P.jpg",
          name: "จับใจ สูตรจับเลี้ยง 500 มิลลิลิตร",
          price: "฿15.00",
        },
      ],
    };
  },
};
</script>

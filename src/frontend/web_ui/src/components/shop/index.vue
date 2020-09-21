<template>
  <div class="app-shelfs">
    <PageTitle title="Articles in the shop" />
    <vs-row>
      <vs-col
        style="background-color: brown;"
        vs-type="flex"
        vs-justify="center"
        vs-align="center"
        w="1"
      >50%</vs-col>
      <vs-col class="shoparts" w="11">
        <!-- articles will display here -->
        <vs-card
          class="art-tpl"
          vs-type="flex"
          vs-justify="flexstart"
          vs-align="flexstart"
          :key="idx"
          v-for="idx in 10"
        >
          <template #title>
            <h3>Pot with a plant</h3>
          </template>
          <template #img>
            <img src="/foto5.png" alt />
          </template>
          <template #text>
            <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit.</p>
          </template>
          <template #interactions>
            <vs-button danger icon>
              <i class="bx bx-heart"></i>
            </vs-button>
            <vs-button class="btn-chat" shadow primary>
              <i class="bx bx-chat"></i>
              <span class="span">54</span>
            </vs-button>
          </template>
        </vs-card>


      </vs-col>
      
    </vs-row>
            <!-- pagination -->
        <div id="pager" class="center">
          <vs-pagination v-model="page" :length="20" />
        </div>
  </div>
</template>

    <script>
import PageTitle from "../widgets/PageTitle";
export default {
  name: "ShopInventory",
  components: {
    PageTitle,
  },
  data: () => ({
    page: 1,
  }),
};
</script>


<style>
.app-shelfs {
  width: 100%;
  height: 100%;
  /* background-color: pink; */
}

.art-tpl {
  margin: 0.5em;
  width: 16em;
  float: left;
}

.shoparts {
  display: flex;
  flex-direction: row;
  align-content: flex-start;
  justify-content: flex-start;
  align-items: flex-start;
  /* background-color: aliceblue; */
}

#pager{
  margin: 1em 0 0 0;
}
</style>
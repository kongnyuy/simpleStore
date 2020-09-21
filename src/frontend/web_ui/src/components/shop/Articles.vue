<template>
  <div class="app-articles">
    <PageTitle title="Buy your article" />
    <section class="trending">
      <!-- Buy template -->
      <vs-tooltip bottom shadow not-hover v-model="buyDialogShow">
        <!-- <vs-button danger @click="buyDialogShow=!buyDialogShow">Click Delete User</vs-button> -->
        <vs-card-group class="slider">
          <vs-card v-for="card in 6" :key="card" @click="handleClick(card)">
            <template #title>
              <h3>Pot with a plant</h3>
            </template>
            <template #img>
              <!-- <img :src="`/static/media/images/foto${card}.png`" alt /> -->
              <img :src="`/foto${card % 2 == 0 ? 1 : 5}.png`" alt />
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
        </vs-card-group>
        <template #tooltip>
          <div class="content-tooltip">
            <h4 class="center">Confirm</h4>
            <p>
              You are about to buy the article
              <b>{{currentSelectedArticle.label}}</b>
            </p>
            <footer>
              <vs-button @click="buyArticle" danger block>Buy</vs-button>
              <vs-button @click="buyDialogShow=false" transparent dark block>Cancel</vs-button>
            </footer>
          </div>
        </template>
      </vs-tooltip>
    </section>
    <section class="arts-controllers"></section>
    
    <!-- all articles display section -->

    <section class="all-arts">      
       <vs-button @click="openLoading">Open Loading</vs-button>
      <box-icon name="rocket"></box-icon>
    </section>
  </div>
</template>

<script>
import PageTitle from "../widgets/PageTitle";

export default {
  name: "Articles",
  components: {
    PageTitle,
  },

  mounted: () => {
    console.log('vue mounted view')
    //this.openLoading()
  },
  data: () => ({
    buyDialogShow: false,
    currentSelectedArticle: {
      id: -1,
      label: "article label",
    },
  }),
  methods: {
    handleClick(c = -1) {
      if (c < 0) return;
      if (!this.$data.buyDialogShow) {
        this.$data.buyDialogShow = !this.$data.buyDialogShow;
      }
      console.log(`selected item is : ${c}`);
      this.$data.currentSelectedArticle.id = c;
    },

    buyArticle() {
      let art = this.$date.currentSelectedArticle;
      if (art < 0) return;
      console.log(`you are about to buy : ${art}`);
      setTimeout(() => {
        this.$data.buyDialogShow = false;
      }, 1500);
    },

    openLoading() {
          const loading = this.$vs.loading()
          setTimeout(() => {
            loading.close()
          }, 3000)
        }
  },
};
</script>


<style>
.app-articles {
  width: 100%;
  height: 100%;
  /* background-color: pink; */
}

.slider > * {
  overflow-x: auto;
}

.trending {
  min-height: 8em;
  width: 100%;
  /* background-color: brown; */
}

.arts-controllers {
}

.all-arts {
  width: 100%;
}
</style> 
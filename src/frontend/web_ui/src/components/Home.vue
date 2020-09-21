<template>
  <div class="hidden">
    <vs-navbar shadow square center-collapsed v-model="active">
      <template #left>
        <vs-button @click="activeSidebar = !activeSidebar" flat icon>
          <i class="bx bx-menu"></i>
        </vs-button>
      </template>
      <vs-navbar-item
        @click="$router.push('articles')"
        :active="active == 'articles'"
        id="articles"
      >Articles</vs-navbar-item>
      <vs-navbar-item
        @click="$router.push('inventory')"
        :active="active == 'inventory'"
        id="inventory"
      >Inventory</vs-navbar-item>
      <vs-navbar-item
        @click="$router.push('shelfs')"
        :active="active == 'store_shelfs'"
        id="store_shelfs"
      >Store shelfs</vs-navbar-item>
      <!-- <vs-navbar-item :active="active == 'license'" id="license">license</vs-navbar-item> -->
      <template #right>
        <vs-button warn gradient @click="refreshData()">refresh</vs-button>
        <vs-button @click="showLoginDialog = !showLoginDailog" flat>Login</vs-button>
        <vs-button circle icon floating>
          <i class="bx bx-plus"></i>
        </vs-button>
      </template>
    </vs-navbar>
    <vs-sidebar absolute v-model="active" :open.sync="activeSidebar">
      <template #logo>
        <!-- ...img logo -->
      </template>
      <vs-sidebar-item id="home">
        <template #icon>
          <i class="bx bx-home"></i>
        </template>
        Home
      </vs-sidebar-item>
      <vs-sidebar-item id="articles" @click="$router.push('articles')">
        <template #icon>
          <i class="bx bxs-shapes"></i>
        </template>
        Articles
      </vs-sidebar-item>
      <vs-sidebar-item id="store_shelfs" @click="$router.push('shelfs')">
        <template #icon>
          <i class="bx bxs-shopping-bags"></i>
        </template>
        Store shelfs
      </vs-sidebar-item>
      <vs-sidebar-group>
        <template #header>
          <vs-sidebar-item arrow>
            <template #icon>
              <i class="bx bx-group"></i>
            </template>
            Shop administration
          </vs-sidebar-item>
        </template>

        <vs-sidebar-item id="inventory" @click="$router.push('inventory')">
          <template #icon>
            <i class="bx bxs-buildings"></i>
          </template>
          Inventory
        </vs-sidebar-item>
        <vs-sidebar-item id="store_shelfs" @click="$router.push('shelfs')">
          <template #icon>
            <i class="bx bxs-store-alt"></i>
          </template>
          Articles in store(shelfs)
        </vs-sidebar-item>
      </vs-sidebar-group>
      <template #footer>
        <vs-row justify="space-between" v-show="userLoggedIn">
          <vs-avatar>
            <img src="/avatars/avatar-5.png" alt />
          </vs-avatar>

          <vs-avatar badge-color="danger" badge-position="top-right">
            <i class="bx bx-bell"></i>

            <template #badge>28</template>
          </vs-avatar>
        </vs-row>
      </template>
    </vs-sidebar>
    <div class id="tv">
      <router-view id="vrouter"></router-view>
    </div>

    <vs-dialog v-model="showLoginDialog">
      <template #header>
        <h4 class="not-margin">
          Welcome to
          <b>Vuesax</b>
        </h4>
      </template>

      <div class="con-form">
        <vs-input v-model="email" placeholder="Email">
          <template #icon>@</template>
        </vs-input>
        <vs-input type="password" v-model="password" placeholder="Password">
          <template #icon>
            <i class="bx bxs-lock"></i>
          </template>
        </vs-input>
        <div class="flex">
          <vs-checkbox v-model="remember">Remember me</vs-checkbox>
          <a href="#">Forgot Password?</a>
        </div>
      </div>

      <template #footer>
        <div class="footer-dialog">
          <vs-button block>Sign In</vs-button>

          <div class="new">
            New Here?
            <a href="#">Create New Account</a>
          </div>
        </div>
      </template>
    </vs-dialog>
  </div>
</template>

<script>
//import Header from "./widgets/Header";
//import Sidebar from "./widgets/Sidebar";

export default {
  name: "Home",
  components: {
    //Header,
    //Sidebar,
  },
  mounted() {
    //this.$vs.setColor("primary", "#000");
    //this.refreshData()
  },

  created(){
    this.refreshData()
  },
  props: {},
  data: () => ({
    tabs: [
      {
        label: "label",
        url: "/destination_link",
      },
      {
        label: "Articles",
        url: "/articles",
      },
      {
        label: "Inventory",
        url: "/store/inventory",
      },
    ],
    showLoginDialog: false,
    active: "home",
    activeSidebar: false,
    email: "",
    password: "",
    remember: false,
    userLoggedIn: false,
  }),
  methods: {
    openLoading() {
      const loading = this.$vs.loading();
      setTimeout(() => {
        loading.close();
      }, 3000);
    },

    refreshData(){
      console.log('loading data')
      this.openLoading();
    }
  },
};
</script>



 <style lang="stylus">
 getColor(vsColor, alpha = 1) {
   unquote('rgba(var(--vs-' + vsColor + '), ' + alpha + ')');
 }

 getVar(var) {
   unquote('var(--vs-' + var + ')');
 }

 .not-margin {
   margin: 0px;
   font-weight: normal;
   padding: 10px;
 }

 .con-form {
   width: 100%;

   .flex {
     display: flex;
     align-items: center;
     justify-content: space-between;

     a {
       font-size: 0.8rem;
       opacity: 0.7;

       &:hover {
         opacity: 1;
       }
     }
   }

   .vs-checkbox-label {
     font-size: 0.8rem;
   }

   .vs-input-content {
     margin: 10px 0px;
     width: calc(100%);

     .vs-input {
       width: 100%;
     }
   }
 }

 .footer-dialog {
   display: flex;
   align-items: center;
   justify-content: center;
   flex-direction: column;
   width: calc(100%);

   .new {
     margin: 0px;
     margin-top: 20px;
     padding: 0px;
     font-size: 0.7rem;

     a {
       color: getColor('primary') !important;
       margin-left: 6px;

       &:hover {
         text-decoration: underline;
       }
     }
   }

   .vs-button {
     margin: 0px;
   }
 }

 .app-head-area {
   /* background-color: red; */
 }

 #tv {
   width: 100%;
   min-height: 90vh;
   height: auto;
   /* background-color: pink; */
   margin: 4em 0 0 0;
 }

 #vrouter {
   width: inherit;
   height: inherit;
   min-min-height: 90vh;
   /* background-color: blue; */
 }
</style>
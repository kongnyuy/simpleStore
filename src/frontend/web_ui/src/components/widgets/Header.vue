
<template>
  <!-- <div class="center examplex"> -->
  <vs-navbar center-collapsed v-model="active">
    <template #left>
      <img src="/logo2.png" alt />
    </template>
    <vs-navbar-item :active="active == 'guide'" id="guide">Guide</vs-navbar-item>
    <vs-navbar-item :active="active == 'docs'" id="docs">Documents</vs-navbar-item>
    <vs-navbar-item :active="active == 'components'" id="components">Components</vs-navbar-item>
    <vs-navbar-item :active="active == 'license'" id="license">license</vs-navbar-item>
    <vs-navbar-item
      :active="active == tab.label"
      id="tab.label"
      v-for="tab in tabs"
      :key="tab.label"
    >
      <router-link to="/foo">{{tab.label}}</router-link>
    </vs-navbar-item>
    <template #right>
      <div v-show="showAdminPanel == 'false'">
        <vs-button flat>Login</vs-button>
        <vs-button>Get Started</vs-button>
      </div>
    </template>
  </vs-navbar>
  <!-- <div class="square">
      <div class="child">child 1</div>
      <div class="child">child 2</div>
      <div class="child">child 3</div>
  </div>-->
  <!-- </div> -->
</template>
<script>
export default {
  name: "Header",
  props: ["tabs", "showAdminPanel"],
  data: () => ({
    active: "home",
  }),
};
</script>

        
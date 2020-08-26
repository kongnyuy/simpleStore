<template>
  <h1 class="pageTitle">{{title}}</h1>
</template>

<script>
export default {
    name: "PageTitle",
    props: ['title']
}
</script>

<style>
.pageTitle{
    font-size: 30px;
    font-weight: 800;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    margin: 1em 0;
    color: var(--app-dark-text);
}

</style>
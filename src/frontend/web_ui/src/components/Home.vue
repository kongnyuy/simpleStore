<template>
    <div class="app-home">
        <div class="center grid">
            <h2>bobo</h2>
            <Header :tabs="tabs" showAdminPanel="false"/>
        </div>
    </div>
</template>

<script>
import Header from './widgets/Header'

export default {
    name: 'Home',
    components: {
        Header
    },
    props: {

    },
    data: () =>({
        tabs: [
            {
                label: 'label',
                url: '/destination_link'
            },
            {
                label: 'Articles',
                url: '/articles'
            },
            {
                label: 'Inventory',
                url: '/store/inventory'
            }
        ]
    }) 
}
</script>

<style>

</style>
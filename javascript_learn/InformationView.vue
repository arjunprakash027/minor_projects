<template>
    <div>
        <p>Message is: {{ message }}</p>
        <input v-model="message" placeholder="edit me" />

        <button @click="getPosts">Show Posts</button>

        <p> {{ stock.price }} </p>


        <!-- <p>{{ data }}</p> -->
    </div>
</template>

<script>
export default {
    setup () {

        return {}
    },
    data() {
        return {
            message: '',
            stock: {}
        }
    },
    methods: {
        async getPosts() {
            await fetch(`https://arjunro.herokuapp.com/get_stock/${this.message}`)
                .then(response => response.json())
                .then(data => this.stock = data)
        }
    }
    
}
</script>

<style lang="scss" scoped>

</style>
<template>
<div class="container justify-content-center align-items-center">
    <h3 style="text-align: center;">History Actions</h3>
    <table class="table table-striped">
    <thead>
        <tr>
        <th scope="col">Date</th>
        <th scope="col">Uploaded File</th>
        <th scope="col">Action</th>
        </tr>
    </thead>

    <tbody>
        <tr v-for="(item, i) in history_data" :key="i">
        <td>{{  item.datetime }}</td>
        <td>{{   item.fileName }}</td>
        <td>{{   item.action }}</td>
        </tr>
    </tbody>

    </table>
</div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "History",
        data() {
            return {
                history_data: [],
            }
        },

        created() {
            this.getData()
        },

        methods: {
            getData() {
                axios.get('')
                    .then(function (response) {
                        console.log(response.data);
                        this.history_data = response.data;
                    })
                    .catch(function (error) {
                        if (error.response) {
                            // The request was made and the server responded with a status code
                            // that falls out of the range of 2xx
                            console.log(error.response.data);
                            console.log(error.response.status);
                            console.log(error.response.headers);
                        } else if (error.request) {
                            // The request was made but no response was received
                            // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                            // http.ClientRequest in node.js
                            console.log(error.request);
                        } else {
                            // Something happened in setting up the request that triggered an Error
                            console.log('Error', error.message);
                        }
                        console.log(error.config);
                    });
            }
        }
    }
</script>

<style scoped>
    .container {
        margin-top: 2vw;
        margin-bottom: 2vw;
    }
    .table {
        width: 80%;
        height: auto;
        margin-top: 2vw;
        margin-bottom: 2vw;
        margin-left: auto;
        margin-right: auto;
    }
</style>
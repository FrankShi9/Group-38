<template>
    <input class="search" placeholder="searching word..." v-model="select_word" style="width: 230px;">
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <button class="btn-primary" @click="highLight">Search</button>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <button class="btn-primary" @click="clearSelection">Clear</button>
    <div >
        <p id="context" style="border:1px solid black;width:500px;padding:5px;">
            I consider that a man's brain originally is like a little empty attic, and you have to stock it with such furniture as you choose. A fool takes in all the lumber of every sort that he comes across, so that the knowledge which might be useful to him gets crowded out, or at best is jumbled up with a lot of other things, so that he has a difficulty in laying his hands upon it.
            I consider that a man's brain originally is like a little empty attic, and you have to stock it with such furniture as you choose. A fool takes in all the lumber of every sort that he comes across, so that the knowledge which might be useful to him gets crowded out, or at best is jumbled up with a lot of other things, so that he has a difficulty in laying his hands upon it.
            I consider that a man's brain originally is like a little empty attic, and you have to stock it with such furniture as you choose. A fool takes in all the lumber of every sort that he comes across, so that the knowledge which might be useful to him gets crowded out, or at best is jumbled up with a lot of other things, so that he has a difficulty in laying his hands upon it.
        </p>
    </div>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "",
        data(){
            return{
                select_word:''
            }
        },
        methods:{
            highLight(){
                this.clearSelection()
                const searchText=this.select_word
                const newText="("+searchText+")"
                const regExp=new RegExp(newText,"g")
                console.log(regExp)
                var html=$('#context').html().toString()
                var newHtml=html.replace(regExp,'<span id="searched" style="background-color: yellow;font-weight: 800;">$1</span>')
                $("#context").html(newHtml)
            },
            clearSelection(){
                console.log($("#context").find("#searched"))
                $("#context").find("#searched").each(function(){
                    $(this).replaceWith($(this).html())
                })
            }
        }
    }
</script>

<style scoped>

</style>
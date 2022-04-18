<template>
	<div class="container">
		<div>
			<h2>Upload File</h2>
			<hr/>
			<label>
				<input type="file" @change="handleFileUpload( $event )" placeholder="choose a csv file" accept=".csv">
                <button v-on:click="submitFile()">Submit</button>
			</label>
			<br>
		</div>
	</div>
    <div class="home">
        <model :showModelTwo="this.showModelTwo"></model>
    </div>
</template>

<script>
	import axios from 'axios';
	import Model from '../components/Model'
	export default {
	    components:{Model},
		data(){
			return {
				file: '',
                fileValue: "",
                showModelTwo: false
			}
		},
		
		methods: {
			handleFileUpload( event ){
                // a single file
				this.file = event.target.files[0];
			},
			submitFile(){
				let formData = new FormData();
				let funcNum = this.$route.query.funcNum
                this.showModelTwo=true
				formData.append('file', this.file);
				// issue a POST request
				axios.post( '', formData, {
						headers: {
                            'Content-Type': 'multipart/form-data'
						}
					}
				).then(response => {
                    if (parseInt(funcNum)==1){
                        console.log(response.data)
                        const arg=JSON.stringify(response.data)
                        console.log(arg)
                        localStorage.setItem('key',arg)
                        //window.location.href='/SDChart?arg='+window.encodeURIComponent(arg);
                        window.location.href='/SDChart'
                    }
                    if (parseInt(funcNum)==2){
                        console.log(response.data)
                        const arg=JSON.stringify(response.data)
                        console.log(arg)
                        localStorage.setItem('key',arg)
                        //window.location.href='/RFMChart?arg='+window.encodeURIComponent(arg)
                        window.location.href='/RFMChart'
                    }
                    if (parseFloat(funcNum)==3.1){
                        console.log(response.data)
                        //this.iconBase64=response.data
                        //localStorage.setItem('key',this.iconBase64)
                        const arg=JSON.stringify(response.data)
                        console.log(arg)
                        localStorage.setItem('key',arg)
                        window.location.href='/TSChart?funcNum=3.1'
                    }
                    if (parseFloat(funcNum)==3.2){
                        const arg=JSON.stringify(response.data)
                        localStorage.setItem('key',arg)
                        window.location.href='/TSChart?funcNum=3.2'
                    }
                })
				.catch(reason => {
                    if (parseInt(funcNum)==1){
                        const data={'a': -1.44, 'b': 9.72, 'c': 16, 'd': 24, 'e': 142,'f': 300,'g':{'p':100,'q':200}}
                        const arg=JSON.stringify(data)
                        localStorage.setItem("key",arg)
                        //window.location.href='/SDChart?arg='+window.encodeURIComponent(arg);
                        window.location.href='/SDChart'
                    }else if (parseInt(funcNum)==2){
                        const data={'a': 144, 'b': 972, 'c': 160, 'd': 240, 'e': 142,'f': 300,'g':400,'r':{'r':100,'f':100,'m':100}}
                        const arg=JSON.stringify(data)
                        localStorage.setItem('key',arg)
                        window.location.href='/RFMChart'}
                    // }else if (parseInt(funcNum)==3){
                    //     window.location.href='/TSChart'
                    // }
                    console.log(reason)
				});
			},
		}
	}
</script>
<style>
    .home {
        width: 100%;
        height: 1000px;
    }
</style>
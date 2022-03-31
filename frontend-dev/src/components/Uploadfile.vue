<template>
	<div class="container">
		<div>
			<h2>Upload File</h2>
			<hr/>
			<label>File
				<input type="file" @change="handleFileUpload( $event )" accept=".csv">
			</label>
			<br>
			<button v-on:click="submitFile()">Submit</button>
		</div>
	</div>
</template>

<script>
	import axios from 'axios';
	
	export default {
		data(){
			return {
				file: ''
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

				formData.append('file', this.file);

				// axios.request({
                //     method:'post',
                //     url: 'https://jsonplaceholder.typicode.com/users',
                //     data: {
                //         //funcNum: funcNum,
                //         file: formData
                //     },
                //     headers:{
                //         'Content-Type': 'multipart/form-data'
                //         //'Content-Type': 'application/json'
                //     }
                // }).then(response => {
                //     console.log(response.data)
                //     console.log('SUCCESS!')
                // })
                //     .catch(function(){
                //         console.log('FAILURE!');
                //     });
				// issue a POST request
				axios.post( '',
					formData,
					{
						headers: {
                            'Content-Type': 'multipart/form-data'
						}
					}
				).then(response => {
				    console.log(funcNum)
                    if (parseInt(funcNum)==1){
                        const a=response.data.a
                        const b=response.data.b
                        const c=response.data.c
                        const d=response.data.d
                        const e=response.data.e
                        const f=response.data.f
                        window.location.href='/SDChart?a='+a+'&b='+b+'&c='+c+'&d='+d+'&e='+e+'&f='+f;
                    }
                    if (parseInt(funcNum)==2){
                        console.log(response.data)
                        const arg=JSON.stringify(response.data)
                        window.location.href='/RFMChart?arg='+window.encodeURIComponent(arg)
                    }
                    if (parseInt(funcNum)==3){
                        window.location.href='/TSChart'
                    }
                })
				.catch(reason => {
                    console.log('Failure')
				});
			}
		}
	}
</script>
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
				
				formData.append('file', this.file);
				// issue a POST request
				axios.post( '',
					formData,
					{
						headers: {
								'Content-Type': 'multipart/form-data'
						}
					}
				).then(function(){
					console.log('SUCCESS!');
				})
				.catch(function(){
					console.log('FAILURE!');
				});
			}
		}
	}
</script>
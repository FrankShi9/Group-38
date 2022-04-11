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
        <div>
            <input type="file" :value="fileValue" id="upImageFile" placeholder="choose a png" @change="ImageToBase64">
            <img :src="iconBase64" alt="" width="200"/>
            <button>上传</button>
        </div>
	</div>
</template>

<script>
	import axios from 'axios';
	
	export default {
		data(){
			return {
				file: '',
                fileValue: "",
                iconBase64: ""
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
				// issue a POST request
				axios.post( '', formData, {
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
                        console.log(response.data)
                        //localStorage.setItem('key',this.iconBase64)
                        this.iconBase64=response.data
                        localStorage.setItem('key',this.iconBase64)
                        window.location.href='/TSChart'
                    }
                })
				.catch(reason => {
                    // if (parseInt(funcNum)==3){
                    //     localStorage.setItem('key',this.iconBase64)
                    //     window.location.href='/TSChart'
                    // }
                    localStorage.setItem('key',this.iconBase64)
                    window.location.href='/TSChart'
                    console.log(reason)
				});
			},
            ImageToBase64() {
                let files = document.getElementById('upImageFile').files[0];
                var reader = new FileReader()
                reader.readAsDataURL(files)
                reader.onload = () => {
                    console.log('file 转 base64结果：' + reader.result)
                    this.iconBase64 = reader.result
                }
                reader.onerror = function (error) {
                    console.log('Error: ', error)
                }
            }
		}
	}
</script>
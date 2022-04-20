<template>
  <div class="container" >
    <div class="row justify-content-center align-items-center">
      <div class="col-md-12">
    <div class="jumbotron">
      <h1 class="display-4">Hi, here is Area-38!</h1>
      <p class="lead">We aim to provide useful insights into business data and empower your business decisions</p>
      <hr class="my-4">
      <a class="btn btn-primary btn-lg" href="../aboutus/" role="button">Learn more about us</a>
    </div>
      </div>
    </div>
    <br />

    <div class="row justify-content-center align-items-center">
        <div class="col-md-4">
            <div class="card text-center">
                <img src="../assets/demand_supply.jpg" class="card-img-top" @click="onSubmitOne" alt="">
                <div class="card-body">
                    <h5 class="card-title">Demand and Supply</h5>
                    <p class="card-text">Improve your pricing strategy</p>
                    <button type="button" class="btn btn-primary" @click="onSubmitOne">Try it!</button>
                </div>
            </div>
        </div>


        <div class="col-md-4">
            <div class="card text-center">
                <img src="../assets/customer_logo.jpg" class="card-img-top" @click="onSubmitTwo" alt="">
                <div class="card-body">
                    <h5 class="card-title">RFM Prediction</h5>
                    <p class="card-text">Locate your target customer</p>
                    <button type="button" class="btn btn-primary" @click="onSubmitTwo">Try it!</button>
                </div>
            </div>
        </div>


        <div class="col-md-4">
            <div class="card text-center">
                <img src="../assets/lstm.jpg" class="card-img-top" @click="onSubmitThree" alt="">
                <div class="card-body">
                    <h5 class="card-title">Time-Series Prediction</h5>
                    <p class="card-text">Predict your future profit</p>
                    <button type="button" class="btn btn-primary" @click="onSubmitThree">Try it!</button>
                </div>
            </div>
        </div>
      </div>
      
      <div class="home">
        <model :showModelThree="this.showModelThree" @cancel="this.showModelThree=false"></model>
      </div>
  </div>
</template>

<script>
import axios from "axios";
import $ from "jquery";
import Model from "../components/Model";
import cookies from "vue-cookies";
export default {
  name: "ChooseFunc",
  components: { Model },
  data() {
    return {
      file: "",
      funcNum: 0,
      status: false,
      showModelThree: false,
    };
  },
  methods: {
    onSubmitOne() {
      this.funcNum = 1;
      window.location.href = "/uploadfile?funcNum=" + this.funcNum;
    },
    onSubmitTwo() {
      this.funcNum = 2;
      window.location.href = "/uploadfile?funcNum=" + this.funcNum;
    },
    onSubmitThree() {
      this.funcNum = 3;
      if (!this.status) {
        alert("You need to login, help you redirect to login page");
        window.location.href = "/login";
      } else {
        this.showModelThree = true;
      }
    },
    handleFileUpload(event) {
      // a single file
      this.file = event.target.files[0];
    },
  },
  created() {
      //cookies.set("is_login",true)
    this.status = cookies.get("is_login");

    // if (document.cookie) {
    //     var cookie = {};
    //     var line = document.cookie.split("; ");
    //     cookie[line[0].split("=")[0]] = line[0].split("=")[1];
    //     cookie[line[1].split("=")[0]] = line[1].split("=")[1];
    //     console.log(cookie);
    //     //this.user = "欢迎:" + cookie["username"] + "(id:" + cookie["id"] + ")";
    // }
  },
};
</script>

<style scoped>
.container {
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto;
}

.jumbotron {
  margin-top: 3vw;
  margin-bottom: 2vw;
}

.col-md-4 img {
  width: 100%;
  height: 18vw;
}

.home {
  width: 100%;
  height: auto;
}
</style>
<template xmlns="http://www.w3.org/1999/html">
    <input class="search" placeholder="searching word..." v-model="select_word" style="width: 230px;">
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <button class="btn-primary" @click="highLight" style="border-radius: 8px">Search</button>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <button class="btn-primary" @click="clearSelection" style="border-radius: 8px">Clear</button>
    <div style="text-align: center;font-size: 40px;margin:auto;left:50%">User Manual</div>
    <div style="width:1000px;padding:5px;margin: auto; left: 50%; top: 20%" class="context">
        <p style="margin:0cm;text-align:center;font-size:14px;font-family:等线;margin-left:18.0pt;"><strong><span style="font-size: 21px; font-family: Tahoma, Geneva, sans-serif;">User Manual</span></strong></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong><span style="font-size: 16px;">1.&nbsp;</span></strong><strong><span style="font-size: 16px;">User Oriented View</span></strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Ⅰ</strong><strong>. Common Users&nbsp;</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;"><span style="font-family: Tahoma, Geneva, sans-serif;">When common users choose the &lsquo;Home&rsquo; column which is displayed on the top left of our website, you can see our dashboard of the Area-38 website. On the left our website, there is an accordion menu which involves Home, User Guidance, Login, History, Logout and About us columns. The followings are their descriptions of the above features.</span></p>
<p style="margin:0cm;text-align:left;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Home</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">The &lsquo;Home&rsquo; column mainly displays our dashboard of the Area-38 website. In the center of the home page, there are three major functionalities which are Demand Curve, RFM Prediction and Time-Series Prediction. You can find their individual instructions in the following part of the user manual.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>User Guidance</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">For User Guidance, you can find our user manual when you turn to this page. The User Guidance column is displayed on the left of our website. Additionally, you can use search box to get specific information that you are looking for.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Login</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">If it is your first time to use our website, it is welcome for you to register an account on our website. Therefore, you can have some privileges such as downloading your PDF report, choosing time-series prediction functionality to view your future profit to obtain more benefit from our website.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>History</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">For the &lsquo;History&rsquo; page, it mainly uses for users to review their historical actions including corresponding files and actions on specific dates.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Logout</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">You can logout your account at any time column which is displayed on the left of our website.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>About us</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">This is an area where users can obtain a brief recognition of our project description, target users, and team members.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">&nbsp;</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;"><span style="font-family: Tahoma, Geneva, sans-serif;">Additionally, In the center of the home page, there are three major functionalities which are Demand Curve, RFM Prediction and Time-Series Prediction. The followings are the descriptions of these three functionalities.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Demand Curve</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">The Demand Curve Functionality mainly offers capabilities for users who intend to seek for a price-demand equilibrium in the stability of commodity market price fluctuation. With the implementation of this function, users can obtain a real-time interactive demand curve which can provide them with an optimized pricing strategy for a higher profit or customized goal.&nbsp;</span></p>
<p style="margin:0cm;text-align:justify;text-indent:0cm;font-size:14px;font-family:等线;margin-left:74.95pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>&nbsp;</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>RFM Prediction</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">The RFM Prediction Functionality provides timely assistance for users who are curious about their target customers group. With the implementation of algorithms such as Recency, Frequency, Monetary Value (RFM) analysis in this functional module, users can locate their optimal/potential customer groups (ranked by quality). Additionally, users can choose to download their PDF report to gain a further understanding in their target customers groups.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>&nbsp;</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Time-Series Prediction</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">The Time-Series Prediction Functionality offers users an opportunity to have a quick glance on their future profit. With algorithms such as AI model (LSTM) and traditional statistical model (holt-winters) in this functional module, users can obtain a line chart which shows future short-term finer (user input 20 days) prediction (LSTM) as well as the long-term (user input 20000 days) tendency of prediction target (holt-winters). Additionally, users can choose to download their PDF report to gain a further understanding in the trend of their future profits.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:36.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>&nbsp;</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Ⅱ</strong><strong>. &nbsp;Administrator&nbsp;</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;"><span style="font-family: Tahoma, Geneva, sans-serif;">After the administrator uses his specific email address and password to login onto our website, there two main features which involves &lsquo;show all users&rsquo; and &lsquo;update models&rsquo; will be shown on our website. This page is only permitted to be viewed by administrators. In this page, the administrator can click the &lsquo;show all users&rsquo; button to check the Database for all users&rsquo; email addresses and passwords who are already registered in our website. Additionally, the administrator can also update current LSTM time-series prediction pre-trained models by simply clicking the &lsquo;Update models&rsquo; button to upload the latest version.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>&nbsp;</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong><span style="font-size: 16px;">2. Installation/Set Up Instructions</span></strong></span></p>
<ol style="list-style-type: decimal;margin-left:8px;">
    <li style="font-family: Tahoma, Geneva, sans-serif;">Open your web browser</li>
    <li style="font-family: Tahoma, Geneva, sans-serif;">Enter the domain name: <a href="http://www.group-38.com">www.group-38.com</a></li>
    <li style="font-family: Tahoma, Geneva, sans-serif;">Press Enter button to access our website</li>
</ol>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>&nbsp;</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong><span style="font-size: 16px;">3. How to Use Instructions</span></strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Ⅰ</strong><strong>. Common Users&nbsp;</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Register</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">If it is your first time to use our website, it is welcome for you to register an account on our website. For registration, just simply input your username, email address and password according to our stipulation. After a successful registration, you will be redirected to the login interface.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Login</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">When it comes to login interface, please input your registered email address and password to gain a successful login onto our website.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Skip (without login)</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">If you don&rsquo;t prefer to login or register, you can click the &lsquo;Skip&rsquo; button to experience two free functionalities: Demand Curve and RFM Prediction.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Demand Curve Functionality</strong></span></p>
<p style="margin:0cm;text-align:left;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">If you take interest in maximizing your profit between demand curve for your stores, you can follow the following steps to acquire your own customized pricing strategy by using our Demand Curve Functionality.</span></p>
<p style="margin:0cm;text-align:left;font-size:14px;font-family:等线;margin-left:42.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">1. Click the &lsquo;Try it!&rsquo; button under the Functional Module of Demand Curve</span></p>
<p style="margin:0cm;text-align:left;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">2. When it turns to the page which requires you to upload your dataset file, please strictly follow the corresponding format of our own demo dataset that can assist you to accomplish a successful analysis.</span></p>
<p style="margin:0cm;text-align:left;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">3. After choosing your target file, please click the &lsquo;Submit&rsquo; button and then wait for your file to finish processing. Otherwise, you can click the &lsquo;Reset&rsquo; button to rechoose your dataset files.</span></p>
<p style="margin:0cm;text-align:left;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">4. When the Price-Demand Curve is shown on your screen, you can pull the slide bar on the left side of the chart which corresponds to price going up or down a certain amount. Therefore, you seek for your optimal profit under the your target prices. Additionally, prices and predicted revenue are listed below the Demand and Price Curve. In addition, the Box-plot visualizes the statistical distribution of the input raw data such as range, interquartile range, mean and variance to a great extent.</span></p>
<p style="margin:0cm;text-align:left;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">5. If you only intend to download the Demand Curve Graph, please click the download button at the top right-hand corner of the graphics. This is free for every user even though they don&rsquo;t register or login onto our website.</span></p>
<p style="margin:0cm;text-align:left;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">6. If you are willing to download the PDF report, please click the &lsquo;Download Results&rsquo; button to get your customized result. Remember please login first before downloading, since this is a privilege for our registered users.</span></p>
<p style="margin:0cm;text-align:left;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">7. Additionally, you can click the &lsquo;Return back to main menu&rsquo; button to return to our home page.</span></p>
<p style="margin:0cm;text-align:left;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>RFM Prediction Functionality</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">For RFM Prediction functionality, please follow the following steps to locate your target customers and acquire your own customer persona analysis.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:42.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">1. Click the &lsquo;Try it!&rsquo; button under the Functional Module of RFM Prediction</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">2. When it turns to the page which requires you to upload your dataset file, please strictly follow the corresponding format of our own demo dataset that can assist you to accomplish a successful analysis.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">3. After choosing your target file, please click the &lsquo;Submit&rsquo; button and then wait for your file to finish processing. Otherwise, you can click the &lsquo;Reset&rsquo; button to rechoose your dataset files.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">4. When the Target Customer Group Analysis Graph is shown on your screen, you can simply zoom in and out of with your mouse scroll. Additionally, when you place the mouse over the corresponding block of customer group, it will automatically display the name and the total amount of this specific customer group. Moreover, statistics of Recency, Frequency and Monetary Value of each customer group are listed on the right-hand side of the graph. In addition, the Box-plot below visualizes the statistical distribution of the input raw data such as range, interquartile range, mean and variance to a great extent.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">5. If you only intend to download the Target Customer Group Analysis image, please click the download button at the top right-hand corner of the graphics. This is free for every user even though they don&rsquo;t register or login onto our website.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">6. If you are willing to download the PDF report, please click the &lsquo;Download Results&rsquo; button to get your customized result. Remember please login first before downloading, since this is a privilege for our registered users.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">7. Additionally, you can click the &lsquo;Return back to main menu&rsquo; button to return to our home page.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Time Series Prediction Functionality</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">If you have already registered and logged into our website, you can follow the following steps to view your future profit prediction of your target metric by using our Time Series Prediction Functionality.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:42.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">1. Click the &lsquo;Try it!&rsquo; button under the Functional Module of Time Series Prediction.&nbsp;</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">2. Then, you can choose whether to use AI model (LSTM) or traditional statistical model for your future profit prediction.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">3. After choosing the model that you prefer, you are required to upload your historic dataset file, please ensure the format of your data follows that of time series dataset where the first column of your dataset must be &ldquo;Time&rdquo;.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">4. After choosing your target file, please click the &lsquo;Submit&rsquo; button and then wait for your file which is automatically starting to process. Otherwise, you can click the &lsquo;Reset&rsquo; button to rechoose your dataset files.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">5. Whichever model you chose earlier, the website will first plot your original dataset. Then, you can input how many days in the future you want to predict and see the result right after to foster a deeper insight into the tendency (holt-winters) and finer local detail (LSTM) of your future profit. Moreover, users can change the start and end of x-axis to zoom in or out the whole line graph. In addition, the Box-plot below visualizes the statistical distribution of the input raw data such as range, interquartile range, mean and variance to a great extent.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">6. If you only intend to download the Time Series Prediction Graph, please click the download button at the top right-hand corner of the graphics. This is free for every user even though they don&rsquo;t register or login onto our website.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">7. If you are willing to download the result of the whole part, please click the &lsquo;Download Results&rsquo; button to get your time series prediction result.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:52.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">8. Additionally, you can click the &lsquo;Return back to main menu&rsquo; button to return to our home page.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:63.0pt;text-indent:-21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">&nbsp;</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Ⅱ</strong><strong>. &nbsp;Administrator&nbsp;</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Login</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">Click the &lsquo;login&rsquo; button on the left of our website. Then, enter admin dedicated email address and password and then the website will jump into the exclusive admin page which cannot be accessed by common users.&nbsp;</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Show all users</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">Click the &lsquo;show all users&rsquo; button to check the Database for all users&rsquo; email addresses and passwords who are already registered in our website.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;"><strong>Update models</strong></span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:21.0pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">Click the &lsquo;Update models&rsquo; button to upload the latest version of current LSTM time-series prediction pre-trained models.</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;margin-left:31.5pt;text-indent:-10.5pt;"><span style="font-family: Tahoma, Geneva, sans-serif;">&nbsp;</span></p>
<p style="margin:0cm;text-align:justify;font-size:14px;font-family:等线;"><span style="font-family: Tahoma, Geneva, sans-serif;">&nbsp;</span></p>
    </div>
</template>

<script>
    import $ from 'jquery'
    import axios from "axios";
    export default {
        name: "",
        data() {
            return {
                select_word: ''
            }
        },
        methods: {
            highLight() {
                this.clearSelection()
                const searchText = this.select_word
                const newText = "(" + searchText + ")"
                const regExp = new RegExp(newText, "g")
                var html = $('.context').html().toString()
                var newHtml = html.replace(regExp, '<span class="searched" style="background-color: yellow;font-weight: 800;">$1</span>')
                $(".context").html(newHtml)
            },
            clearSelection() {
                $(".context").find(".searched").each(function () {
                    $(this).replaceWith($(this).html())
                })
            }
        }
    }
</script>

<style scoped>
    .sub {
        font-weight: bold;
        font-size: 20px;
        font-family: sans-serif;
    }
    .sub-sub{
        font-weight: bold;
        font-size: 17px;
        font-family: sans-serif;
    }
    /* .sub-sub-sub{

    } */

</style>
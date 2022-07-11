# Area 38: An AI-based Business Intelligence Website 
> This repo contains our project codes and related coursework for COMP208: Group Software Project, 2022 Spring.

:rocket:Our website is deployed and available online. You can take a visit by clicking [here](http://group-38.com/).

:bulb: If you are interested in more details (demos/technical specifications), you can take a look at our [docs]().

:hammer: This project is under [GPL-3.0 License](). Contributions of any kind are welcomed!



---



## Application Overview

Our project "Area 38" is a *lightweight and AI-based Business Intelligence Analysis Website* which provides commercial entities, especially individual merchants, a handy platform where they can obtain their own business metrics forecast based on their historical sales data. 

Specifically, we expect to provide users with Demand curve fitting for optimised pricing strategies, RFM customer segmentation and AI/statistical time-series prediction to help them achieve a higher profit or customised goals. 



### System Architecture

<img src="C:\Users\Luyixing\AppData\Roaming\Typora\typora-user-images\image-20220711113326530.png" alt="image-20220711113326530" style="zoom: 25%;" />

The system consists of seven components: Demand/RFM/LSTM(AI)/Holt-Winters (Statistical); each includes related upload/download as well as user account related systems. Guest users could not access LSTM, Holt-Winters and admin functions. A registered user could access all except admin functions. The system employs Request POST, cookies, browser buffer, DBMS and local file storage for data communication/persistence and file I/O.



### UI/UX Design

<img src="C:\Users\Luyixing\AppData\Roaming\Typora\typora-user-images\image-20220711134438245.png" alt="image-20220711134438245" style="zoom:50%;" />



### Development Tools

- Frontend
  - Framework: Vue.js
  - Data Visualization: Apache Echarts
- Backend
  - Framework: Django
  - ML/Statistical models: TensorFlow, scikit-learn etc.



## Get Started

- Create and activate conda env
```
conda create -n proj38 python=3.7
conda activate proj38
```

- Install dependencies

`pip install -r requirements.txt `

- Start DB

```
cd Area_38
python manage.py makemigrations
python manage.py migrate
```

- Start server
```
python manage.py runserver
```

- Type the URL in your browser
```
http://localhost:8000/home
```

> Note
> You can query the database by using `sqlite3 db.sqlite3` in the command line
> or downloading [DB browser for SQLite](https://sqlitebrowser.org/).



## Issues

If you have any question/suggestion, you are welcomed to open an issue. We will try our best to help you with it.



## Contributors

:heart: Thanks to contributions of lovely group members and valuable feedback from our lecturers!

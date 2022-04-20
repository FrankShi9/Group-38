from __future__ import print_function

from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Area_38_app')

import os
import json
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import datetime


temp_user_email = "temp"
if models.UserInfo.objects.filter(email=temp_user_email).first() is None:
    models.UserInfo.objects.create(email=temp_user_email, password='temp').save()

def login(request):
    # if GET, simply render templates
    if request.method == "GET":
        return render(request, "index.html")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_obj = models.UserInfo.objects.filter(email=email, password=password).first()

        if user_obj is not None:

            if 'admin' in email:
                response = redirect('/Admin')
                response.set_cookie("admin", True, max_age=60 * 60 * 24)
                return response
            else:
                response = redirect('/home')
                response.set_cookie("is_login", "true", max_age=60 * 60 * 24)
                response.set_cookie("email", email, max_age=60 * 60 * 24)
                return response

        else:
            return HttpResponse('Login failed')


# front-end bug inside
def register(request):
    # if GET, simply render templates
    if request.method == "GET":
        print('we get!')
        return render(request, "index.html")

    if request.method == "POST":
        print('we post!')
        userName = request.POST.get("userName")
        email = request.POST.get("email")  # front-end bug here
        password = request.POST.get("password")
        print('userName:', userName)
        print('email:', email)
        print('passwd:', password)
        user_obj = models.UserInfo.objects.filter(email=email).first()
        # user_obj = UserInfo(email=email, password=password)
        if user_obj is not None:
            print('register failed, user already exists')
            return HttpResponse('register failed, user already exists')

        else:
            user_obj = models.UserInfo.objects.create(email=email, password=password)
            user_obj.save()
            # logger.info(email)
            # logger.info(password)

            return redirect('/login')


def forget(request):
    # if GET, simply render templates
    if request.method == "GET":
        return render(request, "index.html")


# later when we have user icon, call this function
def logout(request):
    # response = redirect('/login')
    # response.delete_cookie("is_login")
    # response.delete_cookie("email")
    # return response
    if request.method == "GET":
        return render(request, "index.html")


def SDChart(request):
    # if GET, simply render templates
    if request.method == "GET":
        return render(request, "index.html")


def RFMChart(request):
    # if GET, simply render templates
    if request.method == "GET":
        return render(request, "index.html")


def TSChart(request):
    # if GET, simply render templates
    if request.method == "GET":
        return render(request, "index.html")

    if request.method == "POST":
        funcNum = request.POST.get('funcNum')
        if funcNum == '3.1':
            import tensorflow as tf
            import numpy as np
            import pandas as pd
            from sklearn.preprocessing import MinMaxScaler
            import matplotlib.pyplot as plt

            status = request.COOKIES.get('is_login')
            if status == "true":
                print("xts lstm already login")
            user_email = request.COOKIES.get("email")
            uploadfilepath = "./" + user_email + "/upload/"

            scaler = MinMaxScaler(feature_range=(0, 1))
            from tensorflow import keras
            print(tf.__version__)

            # print(type(future))
            future = 20
            model = keras.models.load_model('Area_38_app/m3')
            dataframe = pd.read_csv(open(uploadfilepath + 'gold_price_data.csv'), header=0, parse_dates=[0], index_col=0,
                                    usecols=[0, 1], squeeze=True)
            look_back = 1

            def input_file(df):
                df = df.sort_index(axis=0, ascending=True)  # 将数据按照时间顺序排列
                dataset = df.values  # 保留所有数据值（即非时间戳列的数据）
                line_number = df.shape[0]  # 检测有几行数据，即有几条数据
                # scaler = MinMaxScaler(feature_range=(0, 1))
                dataset = scaler.fit_transform(dataset.reshape(-1, 1))
                return dataset

            def interact(future, back, dataset, model):
                predict = []  # 用来装一个一个的预测结果
                source = []  # 用来装每一次预测的预测数据源
                for i in range(future):
                    t = dataset[-back:]
                    source.append(t)
                    source0 = np.array(source)
                    temp = model.predict(source0)
                    source = []  # 清空，用于下次填充
                    dataset = np.row_stack((dataset, temp[0]))
                    predict.append(temp[0])
                predict = np.array(predict)
                predict = scaler.inverse_transform(predict)
                return predict, dataset

            ds = input_file(dataframe)  # 归一化后的原始输入数据集

            future = request.POST.get('future')
            future = int(future)
            pp, ddss = interact(future, look_back, ds, model)  # pp为用户提供范围内预测的值，ddss 为不断添加预测值更新得到的数据集
            origin = scaler.inverse_transform(ds)  # 原始输入数据集

            dif = origin[-1] - pp[0][0]
            for i in range(future):
                pp[i][0] = pp[i][0] + dif  # 将每个数据加上差值，从而使图像能够连接起来

            # 新建空数组，填入用户自定义future预测的结果，用于接上原图
            futurePredictPlot = np.empty_like(ddss)
            futurePredictPlot[:] = np.nan
            futurePredictPlot = np.reshape(futurePredictPlot, (ddss.shape[0], 1))
            futurePredictPlot[-future: len(ddss), :] = pp

            ''' 画图 '''
            fig1 = plt.figure(figsize=(20, 15))
            plt.plot(origin, color='red', label='Reality')
            plt.plot(futurePredictPlot, color='green', label='Future')
            plt.ylabel('price')
            plt.xlabel('date')
            # plt.show(block=True)
            # save fig
            downloadpath = './{}/report/'.format(user_email)
            if not os.path.exists(downloadpath):
                os.makedirs(downloadpath)
            position = os.path.join(downloadpath, 'gold_price_data_3_1.png')
            plt.savefig(position)
            plt.clf()
            ''' enchart response '''
            # x_test = list(round(i,2) for i in X_test.reshape(-1).tolist())
            y_test = list(round(i, 2) for i in origin.reshape(-1).tolist())
            y_pred = list(round(i, 2) for i in futurePredictPlot.reshape(-1).tolist())
            y_pred = y_pred[-future:]
            # print(y_pred)

            data = {
                'y1': y_test,
                'y2': y_pred,
                # 'value': dataframe.get(['Value']).to_string(index=False).split('\n'),
                #'value': list(i for i in dataframe.values.reshape(-1).tolist()),
            }
            print(data)
            return HttpResponse(json.dumps(data))

        elif funcNum == '3.2':
            from statsmodels.tsa.holtwinters import ExponentialSmoothing
            import pandas as pd
            import matplotlib.pyplot as plt

            status = request.COOKIES.get('is_login')
            if status == "true":
                print("xts hw already login")
            user_email = request.COOKIES.get("email")
            uploadfilepath = "./" + user_email + "/upload/"

            data = pd.read_csv(uploadfilepath + "gold_price_data.csv")
            data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
            rNum = data.shape[0]
            trainNum = rNum
            predictNum = request.POST.get('future')
            predictNum = int(predictNum)


            train_hw = data["Value"][:trainNum]
            #test_hw = data["Value"][trainNum:]

            future = ExponentialSmoothing(train_hw, trend='mul').fit()
            forecast_hw = future.forecast(predictNum)

            ''' plt '''
            plt.figure(figsize=(16, 4))
            plt.plot(train_hw, label='Train')
            plt.plot(forecast_hw, label='Forecast')
            plt.legend(loc='best')

            # save fig
            downloadpath = './{}/report/'.format(user_email)
            if not os.path.exists(downloadpath):
                os.makedirs(downloadpath)
            position = os.path.join(downloadpath, 'gold_price_data_3_2.png')
            plt.savefig(position)
            plt.clf()

            train = train_hw.to_numpy()
            y_1 = list(round(i, 2) for i in train.reshape(-1).tolist())
            forecast = forecast_hw.to_numpy()
            y_2 = list(round(i, 2) for i in forecast.reshape(-1).tolist())
            data = {
                'y1': y_1,
                'y2': y_2,
            }
            return HttpResponse(json.dumps(data))


funcNum = 0


def home(request):
    # if GET, simply render templates
    if request.method == "GET":
        return render(request, "index.html")


def uploadfile(request):
    # if GET, simply render templates
    global funcNum

    if request.method == "GET":
        funcNum = request.GET.get('funcNum')
        print(funcNum)
        return render(request, "index.html")

    if request.method == "POST":
        file = request.FILES.get('file')
        # print(request.POST.get('funcNum'))
        # file = request.POST.get('file')
        if not file:
            print("no file")
            return HttpResponse("file not found")

        status = request.COOKIES.get('is_login')
        user_email = temp_user_email
        print(request.COOKIES)
        if status == "true":
            print("already login")
            user_email = request.COOKIES.get("email")
            uploadfilepath = "./" + user_email + "/upload"
        else:
            print("didn't login")
            uploadfilepath = "./" + user_email + "/upload"
            #return HttpResponse("login required")
            #uploadfilepath = "./upload"

        # store in database
        funcNum = request.GET.get('funcNum')
        print(funcNum)
        userfile_obj = models.UserFile.objects.create(userEmail=models.UserInfo.objects.get(email=user_email),
                                                      fileName=file.name, uploadDate=datetime.datetime.now())
        userfile_obj.save()
        userlog_obj = models.UserLog.objects.create(userEmail=models.UserInfo.objects.get(email=user_email),
                                                    fileName=file.name,
                                                    actionDescription=str(funcNum),
                                                    actionDate=datetime.datetime.now())
        userlog_obj.save()

        if not os.path.exists(uploadfilepath):
            os.makedirs(uploadfilepath)
        position = os.path.join(uploadfilepath, file.name)
        storage = open(position, 'wb')
        for chunk in file.chunks():
            storage.write(chunk)
        storage.close()

        #print(funcNum, type(funcNum))
        # use if else to redirect 3 dif functions

        if funcNum == str(1):
            return redirect('/demand')
        elif funcNum == str(2):
            return redirect('/rfm')
        elif funcNum == str(3.1):
            return redirect('/xts')
        elif funcNum == str(3.2):
            return redirect('/hw')


def history_api(request):
    if request.method == "GET" and request.COOKIES.get('is_login') == 'true':
        user_email = request.COOKIES.get('email')
        log_objs = models.UserLog.objects.filter(userEmail=user_email).order_by('-actionDate')
        data = []
        for i in log_objs:
            temp = {'fileName': i.fileName, 'action': i.actionDescription, 'datetime': str(i.actionDate)}
            data.append(temp)
        print(json.dumps(data))
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponse('need login')


def history(request):
    if request.method == "GET" and request.COOKIES.get('is_login') == 'true':
        return render(request, 'index.html')


def demand(request):
    import pandas as pd
    import numpy as np

    status = request.COOKIES.get('is_login')
    if status == "true":
        print("demand already login")
        user_email = request.COOKIES.get("email")
        uploadfilepath = "./" + user_email + "/upload/"
    else:
        #uploadfilepath = "./upload/"
        print("demand not login")
        user_email = temp_user_email
        uploadfilepath = "./" + user_email + "/upload/"


    demand = pd.read_csv(uploadfilepath+'demand.csv')
    # print(demand.head(10))

    # curve-fit() function from scipy
    from scipy.optimize import curve_fit
    from matplotlib import pyplot as plt

    x = demand['Quantity']

    # y is another array which stores 3.45 times
    # the sine of (values in x) * 1.334.
    # The random.normal() draws random sample
    # from normal (Gaussian) distribution to make
    # them scatter across the base line
    y = demand['Price']

    # Objective function with coefficients as parameters
    def obj2(X, alpha, beta):
        return np.exp(alpha * np.log(X) + beta)

    # curve_fit() function takes the test-function
    # x-data and y-data as argument and returns
    # the coefficients a and b in param and
    # the estimated covariance of param in param_cov
    param, param_cov = curve_fit(obj2, x, y)
    ans = np.exp(param[0] * np.log(x) + param[1])

    print(param)
    print(min(demand['Quantity']), max(demand['Quantity']))
    print(min(demand['Price']), max(demand['Price']))

    plt.xlabel('Demand')
    plt.ylabel('Price')
    plt.plot(x, y, 'o', color='red', label="data")
    plt.plot(x, ans, '--', color='blue', label="fitted curve")
    plt.legend()

    # save fig
    downloadpath = './{}/report/'.format(user_email)
    if not os.path.exists(downloadpath):
        os.makedirs(downloadpath)
    position = os.path.join(downloadpath, 'demand_1.png')
    plt.savefig(position)
    plt.clf()

    raw = {
        'q': (demand['Quantity'].to_string(index=False).split('\n')),
        'p': (demand['Price'].to_string(index=False).split('\n')),
    }

    data = {'a': (param[0]),
            'b': (param[1]),
            'c': (min(demand['Quantity'])),
            'd': (max(demand['Quantity'])),
            'e': (min(demand['Price'])),
            'f': (max(demand['Price'])),
            'g': raw
            }
    # return JsonResponse(data)
    # return HttpResponse(data)
    return HttpResponse(json.dumps(data))


# keep the print() for report
def rfm(request):
    import pandas as pd
    from datetime import timedelta
    import matplotlib.pyplot as plt
    import seaborn as sns
    import squarify

    # Load Dataset
    status = request.COOKIES.get('is_login')
    if status == "true":
        print("rfm already login")
        user_email = request.COOKIES.get("email")
        uploadfilepath = "./" + user_email + "/upload/"
    else:
        #uploadfilepath = "./upload/"
        user_email = temp_user_email
        uploadfilepath = "./" + user_email + "/upload/"


    data = pd.read_csv(uploadfilepath+'rfm.csv', encoding='ISO-8859-1')

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    # Convert 'InvoiceDate' column from object to datetime
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

    # print('------------------------------------------------------')
    # print('Basic analysis: ')
    # print('------------------------------------------------------')
    # print('There are ', data.shape[0], ' rows, ', data.shape[1], ' columns')
    #
    # print('There are ', data[data.CustomerID.isnull()].shape[0], ' orders without a valid consumer id')
    #
    # print('Start time: ', data['InvoiceDate'].min(), '\nEnd time: ', data['InvoiceDate'].max())
    # print('------------------------------------------------------')

    # Preprocess: drop-na
    data.dropna()

    # New Aggregate column: 'TotalSales'
    data['TotalSales'] = data['Quantity'] * data['UnitPrice']

    # New Aggregate column: 'SnapshotDate'
    SnapshotDate = data['InvoiceDate'].max() + timedelta(days=1)
    # print('SnapshotDate: ', SnapshotDate)
    # print('------------------------------------------------------')

    # Group by column: 'CustomerID'
    grouped = data.groupby(['CustomerID']).agg({
        'InvoiceDate': lambda x: (SnapshotDate - x.max()).days,
        'InvoiceNo': 'count',
        'TotalSales': 'sum'
    })

    # Rename for RFM analysis
    grouped.rename(columns={'InvoiceDate': 'Recency (R)',
                            'InvoiceNo': 'Frequency (F)',
                            'TotalSales': 'MonetaryValue (M)'
                            }, inplace=True)

    # Check data head
    # print(grouped.head())
    # print('------------------------------------------------------')
    # print(grouped.shape[0], ' rows, ', grouped.shape[1], ' columns')
    # print('------------------------------------------------------')

    # # basic stat fig
    # plt.figure(figsize=(12, 10))
    # plt.subplot(3, 1, 1)
    # sns.distplot(grouped['Recency (R)'])
    # plt.subplot(3, 1, 2)
    # sns.distplot(grouped['Frequency (F)'])
    # plt.subplot(3, 1, 3)
    # sns.distplot(grouped['MonetaryValue (M)'])
    # plt.show(block=True)

    # Label R and F
    r_label = range(4, 0, -1)
    f_labels = range(1, 5)

    # Assign labels to 4 percentile groups
    r_group = pd.qcut(grouped['Recency (R)'], q=4, labels=r_label)
    f_group = pd.qcut(grouped['Frequency (F)'], q=4, labels=f_labels)

    # New columns R, F
    grouped = grouped.assign(R=r_group.values, F=f_group.values)
    # print('------------------------------------------------------')
    # print(grouped.head())
    # print('------------------------------------------------------')
    ## Label M
    m_label = range(1, 5)

    # Assign labels
    m_group = pd.qcut(grouped['MonetaryValue (M)'], q=4, labels=m_label)

    # New column M
    grouped = grouped.assign(M=m_group.values)

    # Get RFM segments
    def rfm(x):
        return str(x['R']) + str(x['F']) + str(x['M'])

    grouped['RFM'] = grouped.apply(rfm, axis=1)

    rfm_data = grouped
    # print(rfm_data.head())
    # print('------------------------------------------------------')

    # How many unique segments
    rfm_cnt = rfm_data.groupby('RFM')
    rfm_data['RFM'].nunique()
    # print(rfm_cnt.sum())
    # print('------------------------------------------------------')

    # Get RFM score
    rfm_data['RFM_Score'] = rfm_data[['R', 'F', 'M']].sum(axis=1)

    # print(rfm_data['RFM_Score'].head())
    # print('------------------------------------------------------')

    # RFM_level function
    def rfm_level(df):
        if df['RFM_Score'] >= 9:
            return 'Do not lose them'
        elif (df['RFM_Score'] >= 8) and (df['RFM_Score'] < 9):
            return 'Champions'
        elif (df['RFM_Score'] >= 7) and (df['RFM_Score'] < 8):
            return 'Loyal'
        elif (df['RFM_Score'] >= 6) and (df['RFM_Score'] < 7):
            return 'Potential'
        elif (df['RFM_Score'] >= 5) and (df['RFM_Score'] < 6):
            return 'Promising'
        elif (df['RFM_Score'] >= 4) and (df['RFM_Score'] < 5):
            return 'Pay attention'
        else:
            return 'Activate them'

    # RFM level
    rfm_data['RFM_level'] = rfm_data.apply(rfm_level, axis=1)
    # print(rfm_data.head())
    # print('------------------------------------------------------')

    # Calculate average values for each RFM_Level, and return a size for each segment
    rfm_level_agg = rfm_data.groupby('RFM_level').agg({
        'Recency (R)': 'mean',
        'Frequency (F)': 'mean',
        'MonetaryValue (M)': ['mean', 'count']
    }).round(1)

    #print(rfm_level_agg)
    # print('------------------------------------------------------')

    rfm_level_agg.columns = rfm_level_agg.columns.droplevel()
    rfm_level_agg.columns = ['RecencyMean', 'FrequencyMean', 'MonetaryMean', 'Count']

    # Plot
    fig = plt.gcf()
    ax = fig.add_subplot()
    fig.set_size_inches(16, 9)
    # print(rfm_level_agg['Count'])
    ## print('------------------------------------------------------')
    squarify.plot(sizes=rfm_level_agg['Count'], label=[
        'Do not lose them',
        'Champions',
        'Loyal',
        'Pay Attention',
        'Potential',
        'Promising',
        'Activate them'], alpha=.5)
    plt.title("Your predicted target customer group", fontsize=19, fontweight='bold')
    # plt.show(block=True)

    # save fig
    downloadpath = './{}/report/'.format(user_email)
    if not os.path.exists(downloadpath):
        os.makedirs(downloadpath)
    position = os.path.join(downloadpath, 'rfm_2.png')
    plt.savefig(position)
    plt.clf()
    ## plot lim does not need
    ## return Json to WC
    #data = dict(rfm_level_agg['Count'])

    #print(rfm_data)
    raw = {
        'r': list(i.replace('CustomerID', '') for i in rfm_data['Recency (R)'].to_string(index=False).split('\n')),
        'f': list(i.replace('CustomerID', '') for i in rfm_data['Frequency (F)'].to_string(index=False).split('\n')),
        'm': list(i.replace('CustomerID', '') for i in rfm_data['MonetaryValue (M)'].to_string(index=False).split('\n'))
    }
    print(raw)
    data = {
        'Activate them': int(rfm_level_agg['Count'][0]),
        'Champions': int(rfm_level_agg['Count'][1]),
        'Do not lose them': int(rfm_level_agg['Count'][2]),
        'Loyal': int(rfm_level_agg['Count'][3]),
        'Pay attention': int(rfm_level_agg['Count'][4]),
        'Potential': int(rfm_level_agg['Count'][5]),
        'Promising': int(rfm_level_agg['Count'][6]),
        'r': raw
    }
    return HttpResponse(json.dumps(data))


def xts(request):
    # import tensorflow as tf
    # import numpy as np
    import pandas as pd
    # from sklearn.preprocessing import MinMaxScaler

    status = request.COOKIES.get('is_login')
    if status == "true":
        print("xts lstm already login")
    user_email = request.COOKIES.get("email")
    uploadfilepath = "./" + user_email + "/upload/"

    datas = pd.read_csv(open(uploadfilepath + 'gold_price_data.csv'))

    # scaler = MinMaxScaler(feature_range=(0, 1))
    # from tensorflow import keras
    # print(tf.__version__)
    #
    # # print(type(future))
    # future = 20
    # model = keras.models.load_model('Area_38_app/m3')
    # dataframe = pd.read_csv(open(uploadfilepath + 'gold_price_data.csv'), header=0, parse_dates=[0], index_col=0,
    #                         usecols=[0, 1], squeeze=True)
    # look_back = 1
    #
    # def input_file(df):
    #     df = df.sort_index(axis=0, ascending=True)  # 将数据按照时间顺序排列
    #     dataset = df.values  # 保留所有数据值（即非时间戳列的数据）
    #     line_number = df.shape[0]  # 检测有几行数据，即有几条数据
    #     # scaler = MinMaxScaler(feature_range=(0, 1))
    #     dataset = scaler.fit_transform(dataset.reshape(-1, 1))
    #     return dataset
    #
    # def interact(future, back, dataset, model):
    #     predict = []  # 用来装一个一个的预测结果
    #     source = []  # 用来装每一次预测的预测数据源
    #     for i in range(future):
    #         t = dataset[-back:]
    #         source.append(t)
    #         source0 = np.array(source)
    #         temp = model.predict(source0)
    #         source = []  # 清空，用于下次填充
    #         dataset = np.row_stack((dataset, temp[0]))
    #         predict.append(temp[0])
    #     predict = np.array(predict)
    #     predict = scaler.inverse_transform(predict)
    #     return predict, dataset
    # ds = input_file(dataframe)  # 归一化后的原始输入数据集

    if request.method == "GET":
        data = {
            'y1': datas['Value'].to_string(index=False).split('\n'),
            'start': datas['Date'].to_string(index=False).split('\n')[0],
        }
        #print(data)
        return HttpResponse(json.dumps(data))

    # if request.method == "POST":
    #     future = request.POST.get('future')
    #     pp, ddss = interact(future, look_back, ds, model)  # pp为用户提供范围内预测的值，ddss 为不断添加预测值更新得到的数据集
    #     origin = scaler.inverse_transform(ds)  # 原始输入数据集
    #
    #     dif = origin[-1] - pp[-1][0]
    #     for i in range(future):
    #         pp[i][0] = pp[i][0] + dif  # 将每个数据加上差值，从而使图像能够连接起来
    #
    #     # 新建空数组，填入用户自定义future预测的结果，用于接上原图
    #     futurePredictPlot = np.empty_like(ddss)
    #     futurePredictPlot[:] = np.nan
    #     futurePredictPlot = np.reshape(futurePredictPlot, (ddss.shape[0], 1))
    #     futurePredictPlot[-future: len(ddss), :] = pp
    #
    #     ''' 画图 '''
    #     # fig1 = plt.figure(figsize=(20, 15))
    #     # plt.plot(origin, color='red', label='Reality')
    #     # plt.plot(futurePredictPlot, color='green', label='Future')
    #     # plt.ylabel('price')
    #     # plt.xlabel('date')
    #     # plt.show(block=True)
    #     ''' image response '''
    #     # import base64
    #     # with open('foo.png', "rb") as image_file:
    #     #     image_data = base64.b64encode(image_file.read()).decode('utf-8')
    #     # return HttpResponse(image_data)
    #
    #     ''' enchart response '''
    #     #x_test = list(round(i,2) for i in X_test.reshape(-1).tolist())
    #     y_test = list(round(i,2) for i in origin.reshape(-1).tolist())
    #     y_pred = list(round(i,2) for i in futurePredictPlot.reshape(-1).tolist())
    #     y_pred = y_pred[-future:]
    #     #print(y_pred)
    #
    #     data = {
    #         'y1': y_test,
    #         'y2': y_pred,
    #         #'value': dataframe.get(['Value']).to_string(index=False).split('\n'),
    #         'value': dataframe.values,
    #         #'start': datas['Date'].to_string(index=False).split('\n'),
    #     }
    #     #print('1:', data.get('x1'))
    #     #print('2', data.get('y2'))
    #     print(data)
    #     return HttpResponse(json.dumps(data))


# All pdf down button redirect to this one
def pdf_download(request):
    user_email = request.COOKIES.get('email')
    if request.COOKIES.get('is_login') == 'true':
        user_email = request.COOKIES.get('email')
    print(user_email)
    if user_email is None:
        return HttpResponse('Cannot download PDF report, please login')
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # get action
    action = models.UserLog.objects.filter(userEmail=user_email).order_by('id').last()
    funcNum = action.actionDescription
    filepath = "./{}/report/".format(user_email)
    fileName = str(action.fileName)
    fileName = fileName.split('.')[0]
    description = ''
    if funcNum == str(1):
        fileName = fileName + '_1.png'
        description = 'Demand Curve'
    elif funcNum ==str(2):
        fileName = fileName + '_2.png'
        description = 'Recency, Frequency, Monetary Value Analysis'
    elif funcNum ==str(3.1):
        fileName = fileName + '_3_1.png'
        description = 'LSTM Model Prediction'
    elif funcNum ==str(3.2):
        fileName = fileName + '_3_2.png'
        description = 'Holter Winters Model Prediction'
    position = os.path.join(filepath, fileName)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.

    p.drawString(100, 100, description)
    p.drawImage(position, 50, 300, width=500, height=500)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='report.pdf')


def AboutUs(request):
    if request.method == "GET":
        return render(request, "index.html")


def Guidance(request):
    if request.method == "GET":
        return render(request, "index.html")


def Admin(request):
    if request.method == "GET":
        return render(request, "index.html")

    if request.method == "POST":
        funcNum = request.COOKIES.get('funcNum')
        print(funcNum)
        if funcNum == str(1):
            email = models.UserInfo.objects.values_list('email', flat=True)
            password = models.UserInfo.objects.values_list('password', flat=True)
            data = {
                'email': list(email),
                'password': list(password),
            }
            #print('1:', data.get('email'))
            #print('2', data.get('password'))
            return HttpResponse(json.dumps(data))

        elif funcNum == str(2):
            file = request.FILES.get('file')
            # print(request.POST.get('funcNum'))
            # file = request.POST.get('file')
            print(file)

            if not file:
                print("no file")
                return HttpResponse("file not found")

            uploadfilepath = "./Area_38_app/m3/"

            if not os.path.exists(uploadfilepath):
                os.makedirs(uploadfilepath)

            position = os.path.join(uploadfilepath, file.name)
            storage = open(position, 'wb')
            for chunk in file.chunks():
                storage.write(chunk)
            storage.close()
            return HttpResponse('Model update success')


def holt_winters(request):
    import matplotlib.pyplot as plt
    import pandas as pd

    status = request.COOKIES.get('is_login')
    if status == "true":
        print("xts hw already login")
    user_email = request.COOKIES.get("email")
    uploadfilepath = "./" + user_email + "/upload/"

    data = pd.read_csv(uploadfilepath+"gold_price_data.csv")
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

    if request.method == "GET":
        datas = {
            'y1': data['Value'].to_string(index=False).split('\n'),
            'start': data['Date'].to_string(index=False).split('\n')[0],
        }
        #print(data)
        return HttpResponse(json.dumps(datas))



**MySQL数据库读取ETF日数据**
---
现在所维护的ETF数据库使用的是MySQL, 可以通过MATLAB和PYTHON两种方式进行访问进行数据获取，使用的脚本在文件夹Read From MySQL，得到的格式在MATLAB下为Dataset，在PYTHON下为Dataframe，可在脚本里面设定field name来得到指定的数据，如PX_OPEN为开盘价，PX_LAST为收盘价。
运行脚本读取全部时间内（10年）的单个参数数据需要的时间很长，3-4分钟，请耐心等待。
更新频率为每周五下午。

参数 | 名称
---  |  ---
PX_CLOSE_1D  | 前一收盘价
PX_OPEN | 开盘价
PX_HIGH | 最高价
PX_LOW | 最低价
PX_LAST | 收盘价
PX_OFFICIAL_CLOSE | SETTLE价
PX_VOLUME | 成交量
TURNOVER | 总成交额
FUT_AGGTE_VOL | 成交笔数
EQY_WEIGHTED_AVG_PX | 均价
PX_SCALING_FACTOR | 复权因子
OPEN_INT | 持仓量

###操作方式
**MySQL**
**服务器用户名和密码：**
user name: dataaccess
password: 4rQ8SmbvJprb
ip: 120.27.155.55

**连接：**
windows 下建议使用MySQL workbench。

**MATLAB**
> - **Step 1.** 按照此[链接][1]的教程进行MATLAB与MYSQL服务器进行连接。
> - **Step 2.** 在Database Explorer 中可直接进行MYSQL数据表的查看，要获得所需数据并导出到table形式的Dataset, 只需运行**import_data_to_matlab_security_test.m**即可得到。
> - **Step 3.** 获取的数据存在变量W中，W(:,1)为日期，W(:,2)为表头ticker下的price。
> **注意：为了避免重复从MySQL服务器读取数据，从而花费大量时间，建议把已经读取出来的数据存储在本地，可使用**
> ```save W name```

 
**PYTHON**
__prequirement:__
> - python MySQL library. windows 下最方便的安装方法是[anaconda][2], 安装完anaconda之后请升级python-mysql连接包。
> ```
> conda install -c anaconda mysql-connector-python=2.0.3
> ```

__使用方法：__
> - **1.** 直接在python环境下运行脚本retrieving_data_table.py， 取得的数据会存在pandas.DataFrame对象下。
> - **2.** 为了避免重复从MySQL服务器读取数据，从而花费大量时间，建议把已经读取出来的数据存储在本地，可使用pd.to_csv(name)保存dataframe为csv格式文件。


**更新频率**
可根据策略的运行频率来进行确定，目前默认为每周五下午更新。


[1]: http://www.mathworks.com/help/database/ug/mysql-jdbc-windows.html
[2]: http://repo.continuum.io/archive/Anaconda2-4.1.1-Windows-x86_64.exe

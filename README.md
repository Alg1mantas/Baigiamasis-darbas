Here is a simple Flask wheather app. User needs to provide city e.g. : Vilnius, Kaunas etc. It displays: City, Country, Temperature and  Wind speed in given city.
If city name is wrong you will receive N/A.
If you make more than 5 requests per minute, it will also gives you back N/A.
wheather_info.html backround color will change depending on wheather condition in given city. 

When user provides City. App will send request to https://weatherapi-com ...

Required versions:

Package            Version
------------------ ---------
certifi            2022.6.15
charset-normalizer 2.1.0
click              8.1.3
colorama           0.4.5
Flask              2.1.2
idna               3.3
itsdangerous       2.1.2
Jinja2             3.1.2
MarkupSafe         2.1.1
pip                21.2.4
requests           2.28.1
setuptools         58.1.0
urllib3            1.26.10
Werkzeug           2.1.2
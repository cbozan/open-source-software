# Servisi sanal bir sunucu üzerinde ayağa kaldırmak ve kullanmak

- İşletim sisteminiz üzerinde sanallaştırma sunucusu kurmak
- Sanallaştırma sunucusu üzerinde bir işletim sistemi kurmak
- İşletim sisteminde, daha önce oluşturduğunuz servisi ayağa kaldırmak
- Servise kendi makinenizden erişim sağlamak.

&nbsp;
## Sanallaştırma sunucusu
> Oracle VM Virtualbox

![t-1](https://user-images.githubusercontent.com/71611710/201194612-cd62ee04-2b5b-434e-8fec-b62764d7b594.png)

&nbsp;
## Sanal işletim sistemi
> ubuntu-20.04.5-live-server-amd64

![t-2](https://user-images.githubusercontent.com/71611710/201195057-305adeca-5d8e-4661-8f26-a9500fcc6f19.png)

&nbsp;
## Sanal sunucu üzerinde servisi çalıştırmak
> git clone

![t-3 1](https://user-images.githubusercontent.com/71611710/201196267-cacfa571-06ca-419e-8803-f986fce8806c.png)

&nbsp;
> python3 restAPIService.py

![t-3 2](https://user-images.githubusercontent.com/71611710/201196601-893bf0ef-30df-4774-9eef-8731895e96d5.png)

&nbsp;
## Servise ana makineden erişim
> ssh -p 22 cbozan@192.168.1.39

![t-4](https://user-images.githubusercontent.com/71611710/201196946-3cc244d6-8f86-4348-9252-46888d1fd225.png)

&nbsp;
> curl http://127.0.0.1:5000/trends

![t-4 1](https://user-images.githubusercontent.com/71611710/201197050-50baef87-e0ff-4cf2-afb1-f211ddc8ca50.png)

&nbsp;
> GET /trends HTTP/1.1 200

![t-4 2](https://user-images.githubusercontent.com/71611710/201197307-194cac72-c03e-482e-a0bc-958e616359de.png)

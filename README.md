
Este es un proyecto que utiliza python flask, sqlite3 y highcharts para poder visualizar y configurar sensores en arduinos.

## Instrucciones ejecutarlo en  debian

```
 apt install python3 python3-pip python3-flask python3-flask-flatpages sqlite3 git 
 python3-flaskext.wtf python3-apscheduler python3-flask-migrate python3-fpython3-flask-restful python3-flask-sqlalchemy python3-sqlalchemy python3-sqlalchemy-ext python3-flask-babel
 apt install python3-spidev python3-rpi.gpio  # Estos paquetes se deben instalar en la raspi
 git clone https://github.com/neozerosv/invernaderof
 cd invernadero-pi
 # Si se quiere usar la version en desarrollo ejecutar 
 git checkout develop
 source .initflask 
 flask init-db
 flask run
```
Para ejecutarlo en un ambiente virtual y que se pueda ver en la red local
```
 python3-flaskext.wtf python3-apscheduler python3-flask-migrate python3-fpython3-flask-restful python3-flask-sqlalchemy python3-sqlalchemy python3-sqlalchemy-ext python3-flask-babel
 apt install python3 python-sqlite sqlite3 git python3-venv
 apt install python3-spidev python3-rpi.gpio  # Estos paquetes se deben instalar en la raspi
 git clone https://github.com/neozerosv/invernaderof
 cd invernadero-pi
 # Si se quiere usar la version en desarrollo ejecutar
 git checkout develop
 python3 -m venv venv/
 source venv/bin/activate
 pip3 install flask
 source .initflask
 flask init-db
 flask run --host=0.0.0.0
```
Luego deberán abrir la direccion http://127.0.0.1:5000/auth/login el usuario y clave por defecto son: admin:admin


El sistema deberá tener:
- [ ] Administración de usuarios y grupos
- [ ] Administración de lugares (invernaderos) 
- [ ] Administración sensores en cada invernadero
- [ ] Administración de actuadores determinando sus valores de configuracion
- [ ] Agregar de alertas via email u otras cosas
- [ ] Graficas de los valores historicos de los sensores
- [ ] Graficas de los sensores actuales de cada lugar (invernadero)
- [ ] Integracion con las lecturas de los luagares
- [ ] Agrupar los sensores por lugares
- [ ] Actualizar las gráficas dinamicamente
- [ ] Verificar la devolucion de valores nulos
- [ ] Agregar un modulo de traduccion de interfaz
- [ ] Hacer widgets de arrastrar para graficas de sensores

![Captura de grafica](https://github.com/neozerosv/invernadero-pi/raw/develop/images/invernadero-pi-grafica-bruto.png)

Este software utiliza la plantilla base que explican en https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world y basado en el trabajo previo en https://github.com/neozerosv/invernadero-pi




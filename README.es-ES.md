

# Descargador de PDF con Scrapy 

Un Spider de Scrapy para descargar archivos PDF desde una página web. 

# Instalación

1. Crea un virtualenv -  [Cómo crear un virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
2. Activa el virtualenv - `source path/to/bin/activate`
3. Ejecuta `pip install -r requirements.txt`

Nota: Omita esta sección si está ejecutando con docker

# Ejecutar

`scrapy runspider pdf_downloader.py` 

`scrapy runspider download_humblebundle.py` 


# Ejecutar con docker

`docker-compose run download`

# Descargar PDF/EPUB de Humble Bundle

`docker-compose run download_humblebundle`

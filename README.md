# Scrapy PDF Downloader 

A Scrapy Spider for downloading PDF files from a webpage. 

# Installation

1. Create a virtualenv -  [How to create virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
2. Activate the virtualenv - `source path/to/bin/activate`
3. Run `pip install -r requirements.txt`

Note: Skip this section if you running using docker

# Run

`scrapy runspider pdf_downloader.py` 

`scrapy runspider download_humblebundle.py` 


# Run using docker

`docker-compose run download`

# Download Humble Bundle PDF/EPUB

`docker-compose run download_humblebundle`
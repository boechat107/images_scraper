# Image scraper

It is very simple [Scrapy](http://scrapy.org/) based scraper used to download dynamic
generated images on websites.
The scraper downloads the html page, parses the image url and then downloads the image.

## Usage example

[This](http://webas.sefaz.pi.gov.br/SintegraConsultaPublica) web page has a dynamic 
generated captcha image and the following spider can easily grab the images:

```sh
scrapy crawl sintegraPi
```

The `sintegraPi` spider is executed just once and puts an image in the current folder
(it can be adjusted at `settings.py`).
If you want to execute the scraper to N times, just pass the number as an argument:

```sh
scrapy crawl sintegraPi -a runtimes=20
```

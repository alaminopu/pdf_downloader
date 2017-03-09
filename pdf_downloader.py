import urlparse
import scrapy

from scrapy.http import Request

class PdfDownloader(scrapy.Spider):
	name = 'pdf_downloader'
	# domain URL
	allowed_domains = ['example.com']
	# links to the specific pages
	start_urls = ['http://example.com/slides/']


	def parse(self, response):
		# selector of pdf file.
		selector = 'table tr td a[href$=".pdf"]::attr(href)'
		for href in response.css(selector).extract():
			yield Request(
				url=response.urljoin(href),
				callback=self.save_pdf
			)


	def save_pdf(self, response):
		""" Save pdf files """
		path = response.url.split('/')[-1]
		self.logger.info('Saving PDF %s', path);
		with open(path, 'wb') as file:
			file.write(response.body);
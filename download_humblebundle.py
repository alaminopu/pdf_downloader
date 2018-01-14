import os
import scrapy

from scrapy.http import Request


class DownloadHumblebundle(scrapy.Spider):
	name = 'download_humblebundle'
	# domain URL
	allowed_domains = ['www.humblebundle.com']
	# links to the specific pages
	start_urls = ['https://www.humblebundle.com/downloads?key={}'.format(os.environ.get('KEY'))]

	def start_requests(self):
		for url in self.start_urls:
			yield Request(url, self.parse)

	def parse(self, response):
		# selector of pdf file.
		selector = '.download a::attr(href)'
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
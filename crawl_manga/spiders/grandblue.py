import scrapy
from crawl_manga.items import CrawlMangaItem


class GrandblueSpider(scrapy.Spider):
    name = 'grandblue'
    start_urls = ['https://truyentranhlh.net/truyen-tranh/grand-blue/chap-1-4426']

    def parse(self, response):
        raw_image_urls = response.css("#chapter-content > img::attr(data-src)").getall()
        yield CrawlMangaItem(image_urls=raw_image_urls, chapter=response.request.url.split("/")[-1])
        next_page = response.css(
            '#app > main > div.container > center:nth-child(5) > a.rd_sd-button_item2.rd_top-right::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

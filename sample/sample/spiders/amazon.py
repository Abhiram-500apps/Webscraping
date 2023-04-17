import scrapy


class AmazonJobsSpider(scrapy.Spider):
    name = 'amazon_jobs'
    start_urls = ['https://www.amazon.jobs/en/search?base_query=Information+Systems+Engineer']

    def parse(self, response):
        job_data=response.xpath("//div[@class='job-tile-lists col-12 mt-3 mt-md-0']/div/a").xpath('@href').getall()
        # print(response.text)
        print(job_data)

        for job_link in job_data:
            yield scrapy.Request(url=job_link, callback=self.parse_job)
            
    def parse_job(self, response):
        print(response.text)
        job_dict = {}
        title = response.xpath("//div[@class='job']/div/div/h3/text()").get()
        job_dict['title'] = title
        yield job_dict
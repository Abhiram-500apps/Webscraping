import scrapy


class AmazonJobsSpider(scrapy.Spider):
    name = 'amazon_jobs'
    start_urls = ['https://www.amazon.jobs/en/jobs/2348059/business-intelligence-engineer-datacenter-security']

    def parse(self, response):
        job_links_data=response.xpath("//div[@class='job-tile-lists col-12 mt-3 mt-md-0']/div/a").xpath('@href').getall()
        print(job_links_data)

        for job_link in job_links_data:
            yield scrapy.Request(url=job_link, callback=self.parse_job)
            
    def parse_job(self, response):
        print(response.text)
        job_dict = {}
        title = response.xpath("//div[@class='styles__TitleOpeningContainer-sc-15yd6lj-13 vQfBh']/h1/text()").get()
        job_dict['title'] = title
        yield job_dict
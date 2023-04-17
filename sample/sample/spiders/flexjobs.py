import scrapy


class FlexjobsSpider(scrapy.Spider):
    name = "flexjobs"
    allowed_domains = ["www.flexjobs.com"]
    start_urls = ["https://www.flexjobs.com/search?search=python&location="]

    def parse(self, response):
        job_data=response.xpath("//ul[@class='p-0 ']//a").xpath('@href').getall()
        # print(response.text)
        print(job_data)
        count = 0
        for i in job_data:
            job_data[count] = f"https://www.flexjobs.com/{i}"
            count=count+1
            print(job_data)
        for job_link in job_data:
            yield scrapy.Request(url=job_link, callback=self.parse_job)

    def parse_job(self, response):
        print(response.text)
        job_dict = {}
        title = response.xpath("//h1/text()").get()
        Description=response.xpath("//div[@class='job-description']/text()").get()
        Dateposted=response.xpath("//table[@class='job-details']/tbody/tr/th[text()='Date Posted:']").get()
        job_dict['description'] = title
        job_dict['title'] = Description
        job_dict['date posted'] = Dateposted
        yield job_dict



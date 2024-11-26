# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

"""

1. saving based on terminal command:
    store return value of parse method with arranged text extension 
    ('json', 'jsonlines', 'jsonl', 'jl', 'csv', 'xml', 'marshal', 'pickle')
    
    parse mathod will return every data requires to save

    scrapy crawl (crawler_name) -o (file_path.extention)


2. saving based on pipe:
    1) use parse method to analyze data
    2) define element in items.py
    3) store analyzed crawler data to items format object
    4) submit object to pipe BY yield key word.
    5) pipe recieve itetm object, store in various formations
    6) open pipe in settings file


"""

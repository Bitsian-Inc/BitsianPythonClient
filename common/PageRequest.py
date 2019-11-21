class PageRequest(object):
    def __init__(self, page):
        self.totalPage = page['totalPage']
        self.page = page['page']
        self.pageSize = page['pageSize']

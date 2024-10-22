class AppMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        response['X-APP-NAME'] = 'Rush'
        response['X-APP-API-VERSION'] = '0.1'

        return response

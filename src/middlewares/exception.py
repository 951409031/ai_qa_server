from ai_qa_server.models import Response


class HandleException:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    @staticmethod
    def process_exception(request, exception):
        if len(exception.args) > 1:
            return Response(code=exception.args[1], msg=exception.args[0])

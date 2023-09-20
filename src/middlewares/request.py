from copy import deepcopy
from utils.util import to_json
from ai_qa_server.models import Response, Request
from utils.authentication import check_cookie, check_ip, check_paramenter


class FormatRequest:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        params = request.GET.dict()
        body = deepcopy(request.body)
        params.update(request.POST.dict())
        if body and isinstance(to_json(body), dict):
            params.update(to_json(body))
        params = Request(params)
        
        if params._test_num == 1 or not check_cookie():
            return Response(code=101, msg="invalid token")
        if params._test_num == 2 or not check_ip():
            return Response(code=102, msg="unauthorized IP")
        if params._test_num == 3 or not check_paramenter():
            return Response(code=201, msg="invalid check_paramenter")
        
        view_kwargs.update({"params": params})
        

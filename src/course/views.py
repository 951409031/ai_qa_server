from ai_qa_server.models import Response


def complete_question(request, params):
    if params._test_num == 4:
        return Response(question=f"{params.question}-心理学问题")
    if params._test_num == 5:
        return Response(question=f"{params.question}-金融学问题")
    return Response()

def assess_subject(request, params):
    if params._test_num == 4:
        return Response(score=0)
    if params._test_num == 5:
        return Response(score=0.5)
    if params._test_num == 6:
        return Response(score=1)
    return Response()

def answer_doc(request, params):
    if params._test_num == 4:
        raise Exception("cannot find any proper document to answer this question, which means, the returned score is 0", 301)
    if params._test_num == 5:
        raise Exception("the concatenation of documents is too long, this will happen if you set k to a large value and set mode to be “sum“", 302)
    if params._test_num == 6:
        return Response(score=0.8)
    if params._test_num == 7:
        return Response(score=1)
    return Response()

def answer_free(request, params):
    if params._test_num == 4:
        return Response(answer=f"{params.question}-心理学答案")
    if params._test_num == 5:
        return Response(answer=f"{params.question}-金融学答案")
    return Response()
from django.shortcuts import render
from fake_news_detector import model
from fake_news_detector import Learning_Agent
from django.shortcuts import redirect
from django.urls import reverse



def get_results(request):
    if request.method == "POST" and "predict" in request.POST:
        text = request.POST.get('text')

        model_object = model.Model(text)
        result = model_object.prediction()

        label = result[0]
        prob = result[1] * 100
        precision = result[2] * 100
        if label is not None and prob is not None:
            data = {
                'result': label,
                'probability': prob,
                'precision': precision
            }
        else:
            data = {
                'result': "____",
            }
        return render(request, "index.html", data)
        # if "predict1" in request.GET:
        #     prediction = request.GET.get('predict1')
        #     return redirect('feedback_view')

    return render(request, "index.html")


def redirect_view(request):
  if "predict1" in request.POST:
    prediction = request.POST.get('predict1')
    return redirect('feedback_view')




def feedback(request):
    text = None
    selected_value = None
    if request.method == "POST" and 'submit_button' in request.POST:
        text = request.POST.get('text')
        selected_value = request.POST.get('label')
    if text is not None and selected_value is not None:
        write_csv = Learning_Agent.NewsCSVWriter(selected_value, text)
        write_csv.write_to_csv()
        return redirect('feedback_view')
    return render(request, "feedback.html")

def feedback_view(request):
    return render(request, "feedback.html")




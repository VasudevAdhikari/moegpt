import os
from chatbot.models import Chat, Module
from django.shortcuts import render, redirect
from google import genai
from moegpt.settings import GENERATIVE_AI_KEY
from django.contrib.auth.decorators import login_required
from google.api_core.exceptions import FailedPrecondition, InternalServerError
import random

client = genai.Client(api_key=GENERATIVE_AI_KEY)

def get_explicity_response():
    explicit_responses = [
        "It seems that your question contains explicit content. Please consider rephrasing it.",
        "Your question appears to touch on sensitive topics. We encourage you to ask in a more general manner.",
        "We cannot provide answers to questions that involve explicit or inappropriate content. Please ask something else.",
        "Your inquiry seems to involve explicit material. Let's keep the conversation respectful and appropriate.",
        "This question may be considered explicit. Please ask a different question that adheres to our guidelines.",
        "We prioritize a safe environment for all users. Your question contains explicit elements that we cannot address.",
        "It looks like your question includes content that is not suitable for discussion. Please rephrase your question.",
        "Your question has been flagged as potentially explicit. We recommend asking about a different topic.",
        "We cannot assist with questions that involve explicit content. Please feel free to ask something else.",
        "Your question seems to contain explicit language. Let's focus on more appropriate topics."
    ]
    
    answer = random.choice(explicit_responses)
    answer = f'<p><strong>Sorry! <br>{answer}</strong></p>'
    return answer

def get_answer(msg):
    try:
        msg += """
        Above is the question. Generate the answer in the follwing format. The following is the format only.
        give the answer with <p> tag and use html tags for your answers (bold, italic, code etc)
        html response. 
        If the output is a code, then color each an every character according to the semantics and syntax. You can use inline css for separate coloring for each character. If you are coding in python, make sure to give correct indentation. You can use <pre><code> </code></pre> tag which will preserve indentations.
        Use big or small fonts where necessary. (Use bigger fonts for titles or important things)
        if there is a table, write in <table> tag
        if there is code, write in <code> tag with a border and round border radius
        instead of writing texts between ** **, use <b> tag
        Start from the <p> tag. Not from the html beginning
        """

        bot_response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=msg,
        )
        return bot_response.text
    
    except FailedPrecondition as e:
        return False
    
    except (ValueError, InternalServerError) as e:
        get_explicity_response()

    
def invalid_location(request):
    return render(request, 'invalid_location.html')


def get_title(msg):
    try:
        msg += ".Give me a very very short title for the given question. Not more than 50 characters. Embed the title within <strong>tag"
        answer = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=msg,
        )
        return answer.text
    except FailedPrecondition as e:
        return False
    except (ValueError, InternalServerError) as e:
        return get_explicity_response()

@login_required
def askquestion(request):
    print('got into askquestion function')
    if request.method == 'POST':
        question = request.POST.get('usermsg')
        first = request.POST.get('first')
        print(first)
        module = None

        answer = "Sorry, no answers for this question"
        if first == 'true':
            title = get_title(question)
            answer += str(title)
            if title==False:
                print('successfully found error')
                return redirect('/invalid_location/')
            Module.objects.all().update(is_current=False)
            module = Module.objects.create (
                user = request.user,
                module_title = title,
                is_current = True
            )
        else:
            module = Module.objects.get(user=request.user, is_current=True)

        answer = get_answer(question)
        if not answer:
            answer = "Sorry, <br>Cannot answer that question!"
        if answer==False:
            return redirect('/invalid_location/')
        chat = Chat.objects.create (
            question=question, 
            answer=answer, 
            module=module
        )

        chats = Chat.objects.filter(module=module)
        for chat in chats:
            print(chat.question, chat.answer)

        modules = Module.objects.filter(user=request.user).order_by('-module_time')
        
        return render(request, 'index.html', {'chats': chats, 'module': module, 'modules': modules})

@login_required
def show_chatbot(request):
    modules = Module.objects.filter(user=request.user).order_by('-module_time')
    return render(request, 'index.html', {'modules': modules})

@login_required
def show_history(request, module_id):
    Module.objects.all().update(is_current=False)
    module = Module.objects.get(module_id=module_id)
    module.is_current = True
    module.save()
    current_module = Module.objects.get(is_current=True)
    modules = Module.objects.all()
    chats = Chat.objects.filter(module=current_module)
    return render(request, 'index.html', {'chats': chats, 'module': current_module, 'modules': modules})

@login_required
def determine_interface(request):
    if request.user:
        return redirect('/chatbot/')
    return redirect('login')


@login_required
def delete_history(request, delete_module_id, current_module_id):
    Module.objects.filter(module_id=delete_module_id).delete()
    modules = Module.objects.all()
    message = "Related chat history deleted successfully"
    if not (current_module_id == 0):
        module = Module.objects.get(module_id=current_module_id)
        current_module = Module.objects.get(is_current=True)
        chats = Chat.objects.filter(module=current_module)
        return render(request, 'index.html', {'chats': chats, 'module': current_module, 'modules': modules, 'message': message})
    return render(request, 'index.html', {'modules': modules, 'message': message})

@login_required
def show_profile(request):
    chat_count = Chat.objects.filter(module__user_id=request.user.id).count()
    module_count = Module.objects.filter(user_id=request.user.id).count()
    return render(request, 'profile.html', {'user': request.user, 'chat_count': chat_count, 'module_count': module_count})

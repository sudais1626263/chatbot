import re
import longresponses as long
def message_probability(user_message,recognize_words,single_response=False,required_words=[]):
    message_certainity=0
    has_required_words=True
    for word in user_message:
        if word in recognize_words:
            message_certainity+=1
    percentage=float(message_certainity)/float(len(recognize_words))
    for word in user_message:
        if word not in user_message:
            has_required_words=False
            break
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0
def check_all_messages(message):
    high_prob_list={}
    def response(bot_response,list_of_words,single_response=False,required_words=[]):
        nonlocal high_prob_list
        high_prob_list[bot_response]=message_probability(message,list_of_words,single_response,required_words)
    response('hello',['hello','hi','howdy','hi'],single_response=True)
    response('i am doing fine! and you?',['how','are','you','doing'],required_words=['how'])
    response('thank you',['i','love','you'],required_words=['love','you'])
    response(long.r_eating,['what','you','eat'],required_words=['you','eat'])
    best_match=max(high_prob_list,key=high_prob_list.get)
    #print(high_prob_list)
    
    return long.unknown() if high_prob_list[best_match]<1 else best_match
def get_response(user_input):
   
    split_message=re.split(r'\s +[/|.?]\s*',user_input.lower())
    responses=check_all_messages(split_message)
    return responses
while True:
    print('bot: '+ get_response(input('you:')))
    


from flask import Flask, jsonify, make_response, request
from IR_model import ir_model
from feedback import update
from keywords_extraction import keywords_extracted_tfidf
import string
import numpy as np
"""
@author: Tianyu
"""
app = Flask(__name__)




l1=[['comp9444','9444','neural networks and deep learning'],'Monday 6-9pm, Weeks 1-9,11-13 ','Central Lecture Block 7',' http://www.cse.unsw.edu.au/~cs9444','Alan Blair\nHere is their website\nhttps://www.cse.unsw.edu.au/~blair/','Term 3','Postgraduate','Topics chosen from: perceptrons, feedforward neural networks, backpropagation, Hopfield and Kohonen networks, restricted Boltzmann machine and autoencoders, deep convolutional networks for image processing; geometric and complexity analysis of trained neural networks; recurrent networks, language processing, semantic analysis, long short term memory; designing successful applications of neural networks; recent developments in neural networks and deep learning.']
l2=[['comp9414','9414','artificial intelligence'],'Wed 10:00 - 13:00 (Weeks:11), Fri 10:00 - 13:00 (Weeks:1-8,10)','Sir John Clancy Auditorium (K-C24-G17)',' http://www.cse.unsw.edu.au/~cs9414','Alan Blair\nHere is their website\nhttps://www.cse.unsw.edu.au/~blair/','Summer Term, Term 1, Term 2','Postgraduate','Overview of Artificial Intelligence. Topics include: the representation of knowledge, search techniques, problem solving, machine learning, expert systems, natural language understanding, computer vision and an Artificial Intelligence programming language (Prolog or LISP). Students may be required to submit simple Art ificial Intelligence programs, or essays on an aspect of A.I, for assessment, in areas such as robotics, computer vision, natural language processing, and machine learning.']
l3=[['comp1531','1531','software engineering fundamentals'],'Tue 16:00 - 18:00 (Weeks:1-10), Wed 14:00 - 16:00 (Weeks:1-10)','Keith Burrows Theatre (K-J14-G5)',' http://www.cse.unsw.edu.au/~cs1531','Dr A Natarajan\nHere is their website\nhttps://bit.ly/2UrFBUJ','Term 1, Term 3','Undergraduate','This course provides an introduction to software engineering principles: basic software lifecycle concepts, modern development methodologies, conceptual modeling and how these activities relate to programming. It also introduces the basic notions of team-based project management via conducting a project to design, build and deploy a simple web-based application. It is typically taken in the semester after completing COMP1511, but could be delayed and taken later. It provides essential background for the teamwork and project management required in many later courses.']
obj_1=[l1,l2,l3]

def int():
    intent_1 = {}
    for i in obj_1:
        for j in i[0]:
            j=j.lower()
            intent_1[j]='obj'
        for k in range(1,len(i)):
            m=i[k].lower()
            intent_1[m]='obj'
    intent_1['time'] = 'int'
    intent_1['where'] = 'int'
    intent_1['web'] = 'int'
    intent_1['when']='int'
    intent_1['location']='int'
    intent_1['place']='int'
    intent_1['teach']='int'
    intent_1['lecturer']='int'
    intent_1['term']='int'
    intent_1['level']='int'
    intent_1['overview']='int'
    # intent_1['website']='int'
    return intent_1


@app.route('/webhook', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook
    This is meant to be used in conjunction with the translate Dialogflow agent
    """

    # Get request parameters
    req = request.get_json(force=True)
    query = req.get('queryResult').get('queryText')
    para=req.get('queryResult').get('parameters')

    intent= req.get('queryResult').get('intent').get('displayName')

    print(intent)





    if intent == 'Default Fallback Intent':

        ans1=ir_model(query)
        ans1 = {'fulfillmentText': ans1}
        return make_response(jsonify(ans1))



    if intent == 'feedback':
        ans3 = update(query)
        ans3 = {'fulfillmentText': ans3}
        return make_response(jsonify(ans3))

    if intent == 'restart':
        ans7=keywords_extracted_tfidf()
        ans10='Restart successfully'
        ans10 = {'fulfillmentText': ans10}
        return make_response(jsonify(ans10))


    if intent == 'Default Welcome Intent':
        ans4 = 'Hi! I am Fire Balloon, your personal study assistant! May I have your name?'
        save3=[None,None]
        save3 = np.array(save3)
        np.save('save2.npy', save3)

        ans4 = {'fulfillmentText': ans4}
        return make_response(jsonify(ans4))

    if intent == 'place' or intent =='timetable' or intent =='course_web_site' or intent =='what_about' or intent=='lecturer' or intent=='term' or intent == 'study_level' or intent == 'overview':
        query=query.translate(str.maketrans('','',string.punctuation))
        check=query.split()
        for i in range(0 ,len(check)):
            if 'comp' in check[i]:
                if check[i] != 'comp9444' and  check[i] !='comp9414' and check[i] !='comp1531':
                    ans5='Sorry, we do not have information about this course'
                    ans5={'fulfillmentText': ans5}
                    return make_response(jsonify(ans5))
                else:
                    break
        ans2 = context(query)
        ans2 = {'fulfillmentText': ans2}
        return make_response(jsonify(ans2))




def context(query):
    query=query.lower()
    intent_1 = int()
    
    try:
        save1 = np.load('save2.npy')
    except FileNotFoundError:
        save1 = np.load('9900_backend/save2_default.npy')
    
    
    save1 = list(save1)
    for key in intent_1:
        if  key in query:
            if intent_1[key] == 'int':
                save1[0] = key
            else:
                save1[1] = key
    save1 = np.array(save1)
    np.save('save2.npy', save1)
    if save1[0] is None:
        return 'What would you like to know about it?'
    if save1[1] is None:
        return 'Which course would you like to know about?'


    for i in obj_1:
        for j in i[0]:
            if j == save1[1]:
                if save1[0] == 'time' or save1[0] =='when':
                    return i[1]
                elif save1[0] == 'where' or save1[0] =='place' or save1[0] =='location':
                    return i[2]
                elif save1[0] == 'web':
                    return i[3]
                elif save1[0] == 'lecturer' or save1[0] == 'teach':
                    return i[4]
                elif save1[0]== 'term':
                    return i[5]
                elif save1[0]== 'level':
                    return i[6]
                elif save1[0]== 'overview':
                    return i[7]
        for k in i[1:]:
            if k.lower() == save1[1]:
                p=i[0]

                return p[0]


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

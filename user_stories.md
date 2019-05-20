# capstone-project-fire-balloon

## User stories
1 story point = 1 hour
Priority range 1 to 5 from highest to lowest.
Epic stories are in bold, followed by their respective user stories.
User stories are formatted as follows: <br>
   As a: <br>
   I want: <br>
   So that: <br>
   Story points: <br>
   Priority: <br>
   Acceptance criteria: <br>

**As a user I want to be able to have questions about a course's outline answered so that I can prepare for the course.**
1. As a: user<br>
   I want: to be able to type messages to the system<br>
   So that: I can request information<br>
   Story points: 10<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - User is able to type in a text box
   - When an on-screen button or the enter key is pressed, the text in the text box is sent to the server
2. As a: user<br>
   I want: the system to understand my questions<br>
   So that: the system can provide a relevant answer<br>
   Story points: 20<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - System is able to recognise keywords in question
3. As a: user<br>
   I want: the system to respond to my questions with relevant information<br>
   So that: I can know information relevant to the course<br>
   Story points: 30<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - System is able to extract relevant information from a database using keywords
   - e.g. who is the lecturer for COMP9900?
   - e.g. tell me the lecturer for COMP9900.
4. As a: user<br>
   I want: the system's answers to be formed into sentences<br>
   So that: it is more natural to converse with the system<br>
   Story points: 20<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - System is able to display answers to the user in fully formed sentences
5. As a: user<br>
   I want: the system to recognise my speech<br>
   So that: I can ask my questions out loud<br>
   Story points: 10<br>
   Priority: 2<br>
   Acceptance criteria: <br>
   - When an on-screen button is clicked, the system goes into speech detection mode
   - In speech detection mode, the user cannot enter messages using the keyboard
   - In speech detection mode, the user's speech is converted into text displayed in the text box to enter messages.
   - When the on-screen button is clicked again, the system exits speech detection mode

A large part of this epic will be researching and learning how to use Dialogflow. This large user stories cannot be broken up into smaller stories because the high number of story points comes from a lack in skills and not the complexity of the story.

**As a user I want the system to be able to respond conversationally so that it is not a simple question and answer bot.**
1. As a: user<br>
   I want: the sytem to suggest new questions based on my recent questions<br>
   So that: I save time asking questions<br>
   Story points: 30<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - The system suggests related questions for the user to ask after it has given an answer
   - e.g. after answering the question "Who is my lecturer?" the system will suggest the question "What is their email address?"
2. As a: user<br>
   I want: the system to ask close ended questions for more information if it cannot answer my question with the given information<br>
   So that: the system can answer my question<br>
   Story points: 30<br>
   Priority: 3<br>
   Acceptance criteria: <br>
   - System can ask close ended questions for clarification
   - e.g. user: tell me about COMP9900<br>
     system: would you like to know about the course outline or course content?
3. As a: user<br>
   I want: the system to ask open ended questions for more information if it cannot answer my question with the given information<br>
   So that: the system can answer my question<br>
   Story points: 30<br>
   Priority: 3<br>
   Acceptance criteria: <br>
   - System can ask open ended questions for clarification
   - e.g. user: tell me about COMP9900<br>
     system: what would you like to know?
4. As a: user<br>
   I want: the system to be able to handle unexpected phrases<br>
   So that: the system can continue the flow of conversation<br>
   Story points: 10<br>
   Priority: 2<br>
   Acceptance criteria: <br>
   - System responds even if unexpected input is given
      - e.g. "daskljfklsadflsa"
5. As a: user<br>
   I want: the system to be able to handle unrelated questions<br>
   So that: the system can continue the flow of conversation<br>
   Story points: 10<br>
   Priority: 2<br>
   Acceptance criteria: <br>
   - System responds even if question unrelated to course outline or content is asked
      - e.g. "What is the weather like?"

**As a user I want the system to answer questions based on the context of the conversation so I can converse with it like I would with a human.**
1. As a: user<br>
   I want: the system to remember information that I have previously given<br>
   So that: I do not have to repeat the information<br>
   Story points: 20<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - System stores keywords from previous questions and answers

2. As a: user<br>
   I want: the system to use information that I have previously given to answer my questions<br>
   So that: I do not have to repeat the information<br>
   Story points: 70<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - System uses old information given by the user to generate responses

**As a user I want to be able to have questions about a course's content answered so that I can study using the system.**
This is an extension to the epic user story "as a user I want to be able to have questions about a course's outline answered so that I can prepare for the course". This epic involves adding the contents of courses into the database that the system uses to generate responses to the user's questions.
1. As a: user<br>
   I want: i want to be able to have questions about a course's content answered<br>
   So that: I can study using the system<br>
   Story points: 30<br>
   Priority: 5<br>
   Acceptance criteria: <br>
   - System can answer questions about a course's content

**As a developer I want it to be easy for users to access the system so that more users will use the system**
1. As a: developer<br>
   I want: users to be able to access the system through Facebook Messenger<br>
   So that: Facebook Messenger will be able to access the system<br>
   Story points: 10<br>
   Priority: 3<br>
   Acceptance criteria: <br>
   - Users can send messages to the system through Facebook Messenger
   - Users can receive messages from the system through Facebook Messenger
2. As a: developer<br>
   I want: users to be able to access the system through Trello<br>
   So that: Trello will be able to access the system<br>
   Story points: 10<br>
   Priority: 4<br>
   Acceptance criteria: <br>
   - Users can send messages to the system through Facebook Messenger
   - Users can receive messages from the system through Facebook Messenger

## Chosen epics
For our project demo, we have chosen to implement the following epics:
- As a user I want to be able to have questions about a course's outline answered so that I can prepare for the course.
- As a user I want the system to be able to respond conversationally so that it is not a simple question and answer bot.
- As a user I want the system to answer questions based on the context of the conversation so I can converse with it like I would with a human.

These 3 epics were chosen because they contain user stories with the highest priorities. The user stories from the other epics will be attempted if time allows, in order of priority.

The sum of the story points from the 3 chosen epics is 290. UNSW expects a course's workload to be 25 hours per term per UOC. COMP[39]900 is worth 6 OUC so each member's work load should roughly equal 150 hours for the whole 10 weeks (15 hours per week). To calculate time actually spent working on completing user stories, we have removed 3 hours a week due to scheduling 3 hours of meetings per week. We also have scheduled to finish the project 1 week early in order to spend the last week debugging and writing the report. This results in each member spending a total of 12 * 6 = 72 hours working on completing user stories. For the whole team of four, 72 * 4 = 288 hours will be spent working on completing user stories.

To summarise, we expect to be able to complete the user stories on time as we expect to spend 288 hours completing 290 hours of user stories. The 2 hours we are missing out is negligible and can be made up during the final week if necessary. We have planned to stop working on user stories 1 week before the deadline to give us time to debug our software and write our report.

## Sprints
Our team's sprint lengths will be 2 weeks each due to the large size of a lot of the user stories. As previously stated, the large user stories cannot be broken up into smaller ones because the large size of the user stories is not due to the actually complexity of the story, but instead due to the time it would take us to learn the technology. There are 7 weeks remaining, but as stated above we plan to finish in 6 weeks to give us 1 week to debug and write the final report. This gives us 3 sprints to complete the project and we can go into the last week if necessary.

Our MVP will consist of all of the priority 1 user stories. This will take 200 story points. Going by the 12 hours a week that has been calculated above, it will take just over 4 weeks to complete (192 hours as a team over 4 weeks) but we will be aiming to complete the MVP by the end of the 4th week (2nd sprint).

The rest of the stories will be completed at a rate of approximately 48 story points per week in order of priority (12 hours per person) so 96 per sprint. This will allow us to finish by the end of the 3rd sprint (290 story points in total).
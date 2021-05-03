# n2p-gpt3-bot

n2p bot (Notes to points) is a GPT3 based bot that converts roughly jotted down notes to grammatically correct agenda points for a meeting report or minutes of the meeting.
The structure for the notes should be (without new line in between):
* Topic of dicussion
* Discussion-
* Issues- 
* Action-
* To-do-

Here are some examples:
1. Sales report:
  ```
  >>> from n2pbot import convert, append_interaction_to_chat_log
  >>> chat_log = None
  >>> notes = 'Sales report- Harry presented the report. Discussion- growth reported at 15%. CEO credits growth to supply chain efficiency. Action- Target for next quarter 20%. To-do- update progress in next meet'
  >>> points = convert(notes, chat_log)
  >>> points
'As per the next meet agenda on the sales report, Harry presented the report. He reported the sales growth of 15%. The CEO credited the growth to supply chain efficiency. The target for the next quarter was set at 20%. Progress of the target was to be updated in the next meet.'
```
3. Project N2P:
  ```
  >>> notes ='Project N2P- Jack presented the progress, project ready to go for production. Discussion- Suggestions requested on SMS API. Mark suggests Twilio because of its smooth integration. Action- Suggestion approved. To-do- Update progress by Monday'
  >>> points
  "As per the next meeting agenda on the N2P project, Jack presented the progress of the project. He stated that the project is ready for production. He requested suggestions on the SMS API. Mark suggested Twilio as the SMS API because of its smooth integration. The suggestion was approved. Updating on the progress of the project was added to the next meet's agenda."
  ```
  
  ### Scope: 
  * Extended features such as scanning handwritten notes to genrate report points using CNNs for character recognition
  

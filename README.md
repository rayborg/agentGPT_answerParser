# agentGPT_answerParser
The output of the chat produced by the AgentGPT Beta version website doesn't seem to give one final output but instead gives a series of responses. When you use the Export function as a PDF it does not save the output responses, only the queries. So one has to manually go in and copy the ones desired which is tedious. So, I made this quick python script to extract them for you. Just save the Chat in the website then click on it and do a "Select all" then drop it in a text file on the computer and save it as plain text and run the following script on it.

## Instructions
1. After running a Goal on the AgentGPT website Beta version https://agentgpt.reworkd.ai/
2. Save the chat
3. Click on the saved chat and select all then paste it into notepad and save as a plain text file UTF-8 formatted
5. Name that text file agentGPToutput.txt
6. Run the python script and you get the result in a file called compiled.txt

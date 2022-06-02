# summarize-article

My dad, David Everman, is a former physician. He spends a considerable amount of time reviewing the latest medical literature so that he can stay up to date and maintain his continuing education. Since he reads so many complex articles per day, he asked me if I could pass an article through GPT-3 and generate a relevant summary. 

I built a python script that does a few things:
1.	Converts a PDF to HTML, then to txt
2.	Iterates over the txt file and parses it into blocks
3.	Passes each block to the GPT-3 davincii-2 API
4.	Aggregates each response into a summary
5.	Writes the summary to a .txt file

You can find an example article and summary on my website at www.beneverman.com/openai

The issue I am currently dealing with is time complexity, something I have never explored before. My next goal is to optimize the script for time. 

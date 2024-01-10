# Universal-Language-Translator: Multilingual Dataset Conversion Tool
- Here Orders Export is a dataset that is in Chinese, This code helps to convert this complete dataset all cells from Chinese to English.
- Implemented the task using translator and googletrans libraries which are absolutely free and had unlimited API calls.

Observations
-------------
1. Translator library is not giving appropriate results, it is not converting all cells into English, but taking very less time.
2. googletrans library is giving appropriate results, converting all the cells language to English but it is taking very large time to give outputs.

Solution
--------
To overcome this problem, I have tried to parallelise the process of translating the cells. In this parallelization randomly different processes takes different cells, and all processes tries to translate the text in the cell parallelly saving a lot of time. 
I have implemented this using ThreadPool in python.

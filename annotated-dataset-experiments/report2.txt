qualitative findings
"label" is what the law students reported, 
zero shot performance decent


run over absent period with catch err
switch token to petra's

## Overview
In this experiment, I assess the few-shot performance without fine-tuning of the currently best model from openai available via API on the labeled dataset.

### Set-up
**Model**: I use the "text-davinci-003" model. OpenAI's GPT-3 series features a set of models, of which "davinci" is the largest one. They offer fine-tuned version of it for task executions, the third edition of which "text-davinci-003" is. I leave all hyperparameters at default except Temperature, which I set to 0. Thereby the model becomes deterministic, making the outcome more accurate, and the result becomes reproducible.

**Prompt**: After a lot of explorative experiments, I opt for the following prompt, in order to achieve a reasonable precision-recall ratio:
"""
Might the following post have been sponsored? 
 Post: 'All my teenage girl dreams come true tonight! Thank you so much @sherrihill for having me perform at New York Fashion week! 🖤#SherriHillNYFW'
 Potentially Sponsored (True/False): True
 
 Post: 'Life imitating #art 🎨🎨\nlive your #fantasy ✨✨\nStrolling in #beverlyhills #losangeles \n#Illustration by @donna_adi 🎨🎨\nHappy to be back In #usa #la'
 Potentially Sponsored (True/False): False
 
 Post:{txt}
 Potentially Sponsored (True/False): 
"""

**Samples**: I use two samples as training data and evaluate performance on the entire remainder of the 1000+ samples. 

**Evaluation**: I evaluate against the labels as ground truth and compute all default metrics in the sklearn classification report.

## Results
**Quantitative**: The precision is 83.3% for the false predictions and and 86.7% for the true predictions, resulting in an overall accuracy of 84.1% due to the greater weight of the false labels. The whole classification report and the confusion matrix is in the appendix of this document. It is important to note that again in the confusion matrices True and False are flipped, i.e. a non-Ad post (is_ad=False) that is correctly predicted as such is reflected in the left upper number.
Due to repeating server crashes, I end up having it executed only on 1046 of the 1210 samples, but given that the omitted samples are random I don't expect this to significantly impact the performance metrics.

**Qualitative Findings**:
1. The labels are not a perfect ground truth. For example there are 9 instances where the post has disclosures, qualitatively judged clearly is an advertisment but has "False" has label. There is good reason to assume that these 9 are not the only posts labelled as False despite being ads and potentially there are some posts where this is true the other way round too. The important implication for model performance is that the true model performance is likely higher than reported (assuming that the model is more likely to have a mismatch with the labels, if the label is wrong than an accidental match with the labels because it did the same mistake as the labeler).

2. Balancing false positives and negatives is trial and error. As the models are not classification models per se, nudging it to tend to more positive or negative predictions is quite a bit of grammatical playing. Interestingly, a loose phrasing of the task leads to more TP and TN _at the same time_.

3. The "text_davinci_002" model is a really bad choice, no matter the task.

## Discussion
Broadly see the last report for interpretation. 84% without any training seems like a quite reasonable baseline, especially in the light of the labels being not perfectly accurate themselves.

## Future Experiments
1. Fine-tune the model.
2. Just use the Encoder (embedding) and try a) random forrest b) a NN
3. Scale
4. Consider images
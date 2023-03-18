## Overview
In this experiment, I performed few-short learning classification of the labelled dataset with GPT-4 and created explanations.

### Set-up
**Model**: I create a prompt as defined in the texts folder where I give GPT-4 the author of the post and its caption and ask for a true/false label. I also allow for uncertain/true and uncertain/false, but instruct it to choose the stronger labels whenever possible.

**Prompt**: see folder

**Samples**: I use 527 samples, all labelled ones that don't have a caption. 

**Evaluation**: I evaluate classifications against the labels. Then I qualitatively assess the mismatches

## Results
**Quantitative**: I chose a prompt that calibrates GPT-4 in a way that it tends to assign a positive label more often relative to the law students. This yields to a quite high recall of 0.93 on the positive instances, but at the cost of a low precision.

**Qualitative Findings**:
1. A substantial part of the mismatches lie in different definitions of what constitutes "True". I instructed GPT-4 to classify any promotional activity as True, even if non-commercial. It seems like the definition for the law students was less sharp, for example self-promotion of books/fashion of influencers and company accounts are sometimes classified as True, sometimes as False by the law students. For example the fashion brand weworewhat belongs to a single influencer model who sells women fashion. They have 8 posts where they advertise their own products, 4 of which are labelled as True, 4 as False. Following my instructions GPT-4 classified all of them as promotional activity. Similar issues about ambiguity arise where there is promotion that is likely non-commerical (e.g. promoting charities).

2. Looking at the mismatching classifications, in almost all cases where there is no ambiguity, GPT-4 is correct and the human labelers wrong, according to my personal judgement. The reasoning GPT-4 applies looks mostly robust, concise and accurate.

## Discussion
This report brings two learnings: Firstly GPT-4 is more performant (and faster and cheaper) than human lablers _even if they're 'experts'_ as the law students are. Secondly, most mismatches occur because of unclear instructions for edge cases. We need to make decisions of what excatly we want to be classified as positive and what not and add this to the context based on which the NLP model makes classifications. Given the massively increased possible context length in the new GPT-4 (up to 32.000 tokens), we can add multiple pages of defintions and legal explanations to obtain precise, reliable and explainable classifications for any written input (and at soon also images). On a final note, the API usage of GPT-4 is relatively expensive, the 527 experiments costed ~8 Euros, so in order to expand our research we need to find a source of funding for the API usage.

## Future Experiments
1. Outline definition of what ought to classified as ad and what not.
2. Create ground truth for conference papers
3. Vet public available human expert labeled data sets against GPT-4 performance
4. Use images
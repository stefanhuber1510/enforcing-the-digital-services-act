# Overview
As a first Series of Experiments, I asses the few-shot performance without fine-tuning of the GPT-3 models on a random subset your dataset. I set the hyperparameter Temperature to 0, making the model deterministic and thus the result reproducible.

## Set-up
1. I sample 50 ads, and 50 non ads
2. I let the models [text-ada-001, text-babbage-001, text-curie-001, text-davinci-002] classify them using the following prompt with 0 Temperature. Note: I the API reuqests to text-davinci-003 didn't work. But it shouldn't make a difference performance wise anyways.
3. I use the following prompt:
"""
f"Judge whether it is likely that the following caption comes from a post that has been sponsored. Try to aim for a 50:50 distribution between True and False.\n\n Post: 'aaaa meu look de hoje é da @cea_brasil ❤️ patrocinadora e dona do look oficial do Rock in Rio! Aproveitem pra acompanhar o perfil da C&A pra ver todos os lookinhos maravilhosos! Amo muito! ❤️'\n Sponsored (True/False): True\n\n Post: 'side by side ~ sisters ❤️'\n Sponsored (True/False): True\n\n Post:{txt}\n Sponsored (True/False):"
"""
4. I repeat the Experiment with new samples 2 more times

## Results
The obtained confusion matrices are at the end of the document. It is important to note that in the confusion matrices True and False are flipped, i.e. a non-Ad post (is_ad=False) that is correctly predicted as such is reflected in the left upper number.
The smaller models Ada & Babbage classified substantially more items as sponsored, than not. Ada was ~90% accurate with its label "sponsored", but only 60% correct with the "no-ad" label, remarkably consistent for all three experiements. The larger models davinci and curie exhibited a similar bias in favor of classifying posts as ads, with davinci scoring in all experiments 90%+ on accuracy on the non-ads and around 50% on the ads.

## Discussion
Even without any fine-tuning, the GPT-3 models achieve substantial (basically zero-shot) performance. It is hard to directly compare the performance of different models as sensitivity and specifity vary and can not easily be set as parameter. However we can use the prior knowledge that curie and davinci are much more capable than ada and babbage to conclude that the better performance on the non-ads implies it is easier to correctly classify the ads, than the non-ads. This seems intuitively reasonable as ads often have clear hints that they are ads.

I have no theory the explain why the smaller models are so biased towards negative labels and the larger ones towards positive ones. Additionally the extreme similarity between the scores of different random samples seems odd to me. At a later point I will investigate on whether there is a faulty randomization process.

Moreover, qualitatively I found that some of the training data seem to be misclassified. For example I found an entry, that clearly sounded like an ad and even contained #Werbung (german: advertisment), but was not an ad according to training data. I found similar cases also for english posts.

## Confusion matrices
of the three randomized experiments of different models (order: [ada,babbage,curie,davinci]):
Subset 1:
[[19, 31],  
  [2, 48]],  
[[20, 30],  
 [12, 38]],  
[[48,  2],  
 [40, 10]],  
[[47,  3],  
 [23, 27]]  

Subset 2:
[[16, 34],  
  [2, 48]],  
[[18, 32],  
 [15, 35]],  
[[49,  1],  
 [46,  4]],  
[[46,  4],  
 [26, 24]]  

Subset 3:

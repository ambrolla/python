This is the repository for small tasks associated with Python that I either did for fun or done for a job interview.

## First File

hugging_face_assignment was the task for the internship.

### Assignment:

We're going to use the wikitext [link](https://huggingface.co/datasets/wikitext) dataset with the distilbert-base-cased [link](https://huggingface.co/distilbert-base-cased) model checkpoint.

Start by loading the wikitext-2-raw-v1 version of that dataset, and take the 11th example (index 10) of the train split.
We'll tokenize this using the appropriate tokenizer, and we'll mask the sixth token (index 5) the sequence.

When using the distilbert-base-cased checkpoint to unmask that (sixth token, index 5) token, what is the most probable predicted token (please provide the decoded token, and not the ID)?

Tips:

- You might find the transformers docs [link](https://huggingface.co/docs/transformers/index) useful.
- You might find the datasets docs [link](https://huggingface.co/docs/datasets/index) useful.
- You might also be interested in the Hugging Face course [link](https://huggingface.co/course/chapter1/1).

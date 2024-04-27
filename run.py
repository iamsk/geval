import json
import tqdm
import jsonlines
from dotenv import load_dotenv

load_dotenv()
from deepeval.test_case import LLMTestCase
from deepeval.metrics import SummarizationMetric
from dify import dify


def run(input, output):
    test_case = LLMTestCase(
        input=input,
        actual_output=output
    )
    summarization_metric = SummarizationMetric(include_reason=False)
    summarization_metric.measure(test_case)
    return summarization_metric.score_breakdown


summeval_fp = 'data/summeval.json'
summeval = json.load(open(summeval_fp))
count = len(summeval)
summeval_sample = [summeval[int(i * count / 10)] for i in range(10)]
with jsonlines.open(f'results/{dify.name}.jsonl', mode='w') as writer:
    count = 1
    for instance in tqdm.tqdm(summeval_sample):
        input = instance['source']
        output = dify.chat(input)
        answer = run(input, output)
        print(answer)
        writer.write(answer)
        count += 1

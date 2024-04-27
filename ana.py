import os
import jsonlines
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
dify_model = os.getenv('DIFY_MODELS').split(',')


def ana():
    ret = []
    for model in dify_model:
        with jsonlines.open(f'results/{model}.jsonl') as reader:
            score = 0
            for obj in reader:
                score += (obj['Alignment'] + obj['Coverage']) / 2
        ret.append(round(score, 2))
    dic = {
        'name': dify_model,
        'score': ret
    }
    df = pd.DataFrame(dic)
    df.to_csv('results/final.csv')


if __name__ == '__main__':
    ana()

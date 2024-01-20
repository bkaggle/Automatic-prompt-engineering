from flask import Flask, render_template, request
from evaluator import Evaluator
from knowledge_retrieval import KnowledgeRetrieval
from knowledge_integrator import KnowledgeIntegrator
import config
import pickle
import config_secret

app = Flask(__name__)

knowledge_retriever = KnowledgeRetrieval(config.knowledge)
knowledge_integrator = KnowledgeIntegrator(model_name='gpt-3.5-turbo-0613', temperature=0)
evaluator = Evaluator(model_name='gpt-3.5-turbo-0613', temperature=0)
answers = []
metrics = {}

@app.route('/')
def index():
    return render_template('index.html', answers=answers, metrics=metrics)

@app.route('/ask', methods=['POST'])
def ask():
    if request.method == 'POST':
        question = request.form['question']
        knowledge = knowledge_retriever.retrieve(question)
        answer = knowledge_integrator.get_answer(config.PROMPT_TEMPLATE, {'question': question, 'knowledge': knowledge})[0]['text']

        # Evaluate the answer
        evaluation, _ = evaluator.get_evaluation(config.EVALUATION_PROMPT_TEMPLATE,
                                                {'question': question, 'knowledge': knowledge, 'answer': answer})
        evaluation_text = evaluation['text'].split('\n')
        for row in evaluation_text:
            metric_name = row.split(':')[0].strip()
            value = int(row.split(':')[1].strip())
            if metric_name not in metrics:
                metrics[metric_name] = []
            metrics[metric_name].append(value)

        return render_template('index.html', answers=[{'question': question, 'knowledge': knowledge, 'answer': answer}], metrics=metrics)

if __name__ == '__main__':
    app.run(debug=True)

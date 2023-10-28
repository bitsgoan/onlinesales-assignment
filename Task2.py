import requests
import threading
from multiprocessing import Process, Lock, Manager
from multiprocessing import freeze_support
import time

api_url = "https://evaluate-expression.p.rapidapi.com/"
api_headers = {
    "X-RapidAPI-Key": "d60f493d36msh838c6f47858c398p1b5daejsnccf927f1b251",
    "X-RapidAPI-Host": "evaluate-expression.p.rapidapi.com"
}

max_requests = 50
max_instances = 10

def evaluate_expression_api(expressions):
    results = []
    for expression in expressions:            
        if expression == "end":
            break
        else:
            try:
                response = requests.get(api_url, headers=api_headers, params={'expression': expression})
                if response.status_code == 200:
                    result = response.text
                    results.append(f"{expression} => {result}")
            except requests.RequestException as e:
                results.append(f"{expression} => Error: {str(e)}")
    return results

def evaluate_lot(expression_queue, queue_lock):
    while True:
        queue_lock.acquire()
        if expression_queue.empty():
            queue_lock.release()
            return
        batch = expression_queue.get()
        queue_lock.release()
        results = evaluate_expression_api(batch)
        for result in results:
            print(result)
        time.sleep(1/(2*max_instances))

def process_function(expression_queue, queue_lock):
    threads = []
    for _ in range(max_requests):
        t = threading.Thread(target=evaluate_lot, args=(expression_queue, queue_lock))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def evaluate_expression(expressions, expression_queue, queue_lock):
    expression_batches = [expressions[i:i+max_requests] for i in range(0, len(expressions), max_requests)]
    for batch in expression_batches:
        expression_queue.put(batch)
    processes = []
    for _ in range(len(expression_batches)):
        p = Process(target=process_function, args=(expression_queue, queue_lock))
        processes.append(p)
        print('a')
        p.start()
    for p in processes:
        p.join()

if __name__ == '__main__':
    
    freeze_support()

    manager = Manager()
    expression_queue = manager.Queue()
    queue_lock = Lock()

    expressions = [
        "2 * 4 * 4",
        "5 / (7 - 5)",
        "sqrt(5^2 - 4^2)",
        "sqrt(-3^2 - 4^2)",
        "2 * 8 * 4",
        "5 / (8 - 5)",
        "sqrt(8^2 - 4^2)",
        "sqrt(-8^2 - 6^2)",
        "end",
    ]

    total_request_handle_capacity = max_instances * max_requests 
    expressions = expressions[:total_request_handle_capacity]

    evaluate_expression(expressions, expression_queue, queue_lock)

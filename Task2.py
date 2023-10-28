#Step 1 - variable 'expressions' is passed
#Step 2 - We calculate the max requests we can take and alter the requests to take the first 'max requests' expressions 
#Step 3 - We break this expressions into chunks of 50
#Step 4 - We initiate as many processes as these chunks
#Step 5 - We take each process which will have max 50 expressions, and create max 50 threads to make sure these expressions are called parallelly

import requests
import threading
from multiprocessing import Process, Manager
from multiprocessing import freeze_support

api_url = "https://evaluate-expression.p.rapidapi.com/"
api_headers = {
    "X-RapidAPI-Key": "d60f493d36msh838c6f47858c398p1b5daejsnccf927f1b251",
    "X-RapidAPI-Host": "evaluate-expression.p.rapidapi.com"
}

max_threads_per_process = 50
max_processes = 10
max_requests = 50

def evaluate_expression_api(expression):
    try:
        response = requests.get(api_url, headers=api_headers, params={'expression': expression})
        if response.status_code == 200:
            result = response.text
            print(f"{expression} => {result}")
        else:
            print(f"{expression} => Error: HTTP {response.status_code}")
    except requests.RequestException as e:
        print(f"{expression} => Error: {str(e)}")

def thread_function(expression_queue):
    expression = expression_queue.get()
    evaluate_expression_api(expression)

def process_function(expression_queue):
    threads = []
    for _ in range(max_threads_per_process):
        t = threading.Thread(target=thread_function, args=(expression_queue,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    freeze_support()

    manager = Manager()
    expression_queue = manager.Queue()

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

    total_request_handle_capacity = max_processes * max_requests 
    expressions = expressions[:total_request_handle_capacity]

    for expression in expressions:
        expression_queue.put(expression)

    processes = []
    for _ in range(max_processes):
        p = Process(target=process_function, args=(expression_queue,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

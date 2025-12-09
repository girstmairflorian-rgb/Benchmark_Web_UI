from flask import Flask, request, render_template
from time import perf_counter
from benchmarks import multiprocessing_functions, test_algorithms
app = Flask(__name__)

ALGORITHMS = {
    "primeChecker": test_algorithms.check_if_prime,
    "fibonacci": test_algorithms.fibonacci,
}

MP_FUNCTIONS = {
    "poolApply": multiprocessing_functions.pool_apply,
    "poolApplyAsync": multiprocessing_functions.pool_apply_async,
    "poolApplyAsyncChunked": multiprocessing_functions.pool_apply_async_chunked,
    "poolMap": multiprocessing_functions.pool_map,
    "singleProcessLoop": multiprocessing_functions.single_process_loop,
}

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    algorithm = request.form["algorithm"]
    benchmark = request.form["benchmark"]
    upper_limit = int(request.form["upperLimit"])
    num_processes = int(request.form["numProcesses"])

    fun_algorithm = ALGORITHMS[algorithm]
    fun_benchmark = MP_FUNCTIONS[benchmark]
    numbers: list[int] = list(range(1, upper_limit + 1))

    start = perf_counter()
    result = fun_benchmark(numbers, fun_algorithm, num_processes)
    end = perf_counter()

    elapsed_time = round((end - start), 5)

    return render_template(
        "results.html",
        algorithm=algorithm,
        benchmark=benchmark,
        upper_limit=upper_limit,
        num_processes=num_processes,
        elapsed_time=elapsed_time,
    )

if __name__ == "__main__":
    app.run(debug=True)
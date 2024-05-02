def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])  # Sort jobs by finish time
    result = []
    last_finish_time = 0
    total_profit = 0

    for job in jobs:
        start_time, finish_time, profit = job
        if start_time >= last_finish_time:
            result.append(job)
            last_finish_time = finish_time
            total_profit += profit

    return result, total_profit

# Example jobs: (start_time, finish_time, profit)
jobs = [(1, 4, 20), (2, 5, 50), (6, 7, 30), (5, 9, 25), (7, 9, 35)]
result, total_profit = job_scheduling(jobs)
print("Selected jobs:", result)
print("Maximum profit:", total_profit)

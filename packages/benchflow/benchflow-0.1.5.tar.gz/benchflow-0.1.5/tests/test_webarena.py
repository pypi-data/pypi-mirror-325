import os

from webarena_openai import WebarenaAgent

from benchflow import load_benchmark

bench = load_benchmark(benchmark_name="webarena")

your_agents = WebarenaAgent()

run_ids = bench.run(
    task_ids=[0,1],
    agents=your_agents,
    api={"OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")},
    requirements_dir="webarena_requirements.txt",
    params={}
)

results = bench.get_results(run_ids)
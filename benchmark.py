from ultralytics.yolo.utils.benchmarks import benchmark

# Benchmark
benchmark(model='yolo-model/anpr_v8.pt', imgsz=640, half=False, device=0)

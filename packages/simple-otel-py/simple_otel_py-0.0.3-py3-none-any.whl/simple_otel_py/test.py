from simple_otel import OtelSetup # user local module instead pip for testing
import time
import requests

otel = OtelSetup(name="my_service", otlp_collector_endpoint="http://k8s-dev1.irix.intra:32307")
logger = otel.get_logger()
[trace, tracer] = otel.init_tracing()
meter = otel.init_metrics()
method_counter = meter.create_counter("my_counter")


@tracer.start_as_current_span("add")
def add(a: int, b: int):
  method_counter.add(8)
  logger.info("Adding numbers") 
  return a + b


@tracer.start_as_current_span("fact")
def get_fact():
  method_counter.add(1)
  try:
    start_time = time.time()
    url = "https://api.chucknorris.io/jokes/random/"
    response = requests.get(url)
    response.raise_for_status()
    logger.info("call worked")
    fact_data = response.json()
    fact = fact_data.get("value", "No joke found!")
    
    # custom tracing
    duration = round((time.time() - start_time), 2)
    current_span = trace.get_current_span()
    current_span.set_attribute("request.duration", f"{duration} seconds")
    return fact
  except requests.exceptions.RequestException as e:
    logger.error(f"An error occurred during request: {e}")

if __name__ == '__main__':
  logger.info("started")
  result = add(2, 5)
  fact = get_fact()
  logger.info(fact)
  logger.info(f"the result is {result}")
  logger.info("done")
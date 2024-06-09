from langchain.callbacks.tracers import LangChainTracer
from langchain_core.tracers.context import tracing_v2_enabled

# Define a mock chain for demonstration purposes
class MockChain:
    def invoke(self, input_data, config=None):
        print(f"Invoked with input: {input_data} and config: {config}")
        return {"result": "success"}

# Instantiate the mock chain
chain = MockChain()

# Create the LangChainTracer instance
tracer = LangChainTracer()

# Trace using a callback
try:
    chain.invoke({"question": "Am I using a callback?", "context": "I'm using a callback"}, config={"callbacks": [tracer]})
except Exception as e:
    print(f"Error during callback tracing: {e}")

# Trace using a context manager
try:
    with tracing_v2_enabled():
        chain.invoke({"question": "Am I using a context manager?", "context": "I'm using a context manager"})
except Exception as e:
    print(f"Error during context manager tracing: {e}")

# This will NOT be traced (assuming LANGCHAIN_TRACING_V2 is not set)
try:
    chain.invoke({"question": "Am I being traced?", "context": "I'm not being traced"})
except Exception as e:
    print(f"Error during normal invocation: {e}")

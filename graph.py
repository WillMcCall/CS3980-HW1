import pandas as pd
import fib
import plotly.express as px

fib.fib(100)

df = pd.DataFrame({
    "iterations": list(fib.execution_times.keys()),
    "times": list(fib.execution_times.values())
})

fig = px.line(df, x="iterations", y="times", title="Fibonacci Execution Time")
fig.show()

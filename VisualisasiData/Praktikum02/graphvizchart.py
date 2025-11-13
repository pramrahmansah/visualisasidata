import streamlit as st
import graphviz as graphviz

st.title('Graphviz')

graph = graphviz.Digraph()
graph.edge('Training Data', 'ML Algorithm')
graph.edge('ML Algorithm', 'Model')
graph.edge('Model', 'Result Forecasting')
graph.edge('New Data', 'Model')

st.graphviz_chart(graph)
# st.graphviz_chart('''
# digraph {
#     "Training Data" -> "ML Algorithm"
#     "ML Algorithm" -> "Model"
#     "Model" -> "Result Forecasting"
#     "New Data" -> "Model"
# }
# ''')
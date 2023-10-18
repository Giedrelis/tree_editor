import streamlit as st

# Embed the D3.js visualization
with open("d3.min.js", "r") as f:
    d3_script = f.read()

with open("tree_editor.js", "r") as f:
    tree_editor_script = f.read()

st.components.v1.html(
    f"""
    <script>{d3_script}</script>
    <div id="d3-container"></div>
    <script>{tree_editor_script}</script>
    """,
    height=600
)

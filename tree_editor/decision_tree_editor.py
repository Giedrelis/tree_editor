import streamlit as st
import json

# Load the decision tree data
with open("decision_tree.json", "r") as file:
    DECISION_TREE = json.load(file)

# Embed the D3.js visualization
with open("d3.min.js", "r") as f:
    d3_script = f.read()

with open("tree_editor.js", "r") as f:
    tree_editor_script = f.read().format(tree_data=json.dumps(DECISION_TREE))



st.components.v1.html(
    f"""
    <script>{d3_script}</script>
    <div id="d3-container"></div>
    <script>{tree_editor_script}</script>
    """,
    height=650
)

# Allow users to edit the JSON directly
edited_tree = st.text_area("Edit Decision Tree JSON:", value=json.dumps(DECISION_TREE, indent=4))
if st.button("Update Tree"):
    try:
        DECISION_TREE = json.loads(edited_tree)
        with open("decision_tree.json", "w") as file:
            json.dump(DECISION_TREE, file, indent=4)
        st.success("Decision tree updated!")
    except json.JSONDecodeError:
        st.error("Invalid JSON format. Please check and try again.")

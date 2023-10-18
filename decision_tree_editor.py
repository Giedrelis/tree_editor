
import streamlit as st
import streamlit.components.v1 as components

# Load the custom component
tree_editor = components.declare_component("tree_editor", url="http://localhost:3001")

def main():
    st.title("Graphical Tree Editor")

    # Sample tree data (this will be dynamic in the final version)
    tree_data = {
        "name": "Root",
        "children": [
            {"name": "Child 1"},
            {"name": "Child 2", "children": [{"name": "Grandchild"}]}
        ]
    }

    # Render the tree editor component
    updated_tree_data = tree_editor(tree_data=tree_data)

    # Display the updated tree data (for debugging purposes)
    st.json(updated_tree_data)

if __name__ == "__main__":
    main()

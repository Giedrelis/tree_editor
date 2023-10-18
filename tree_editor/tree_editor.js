// Load the decision tree data from Streamlit
let treeData = {{tree_data}};  // Streamlit will replace {{tree_data}} with actual data

const width = 1000;
const height = 600;

const svg = d3.select("#d3-container")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

const root = d3.hierarchy(treeData);
const treeLayout = d3.tree().size([width, height]);
treeLayout(root);

const g = svg.append('g');

// Draw links
g.selectAll('path')
    .data(root.links())
    .enter()
    .append('path')
    .attr('d', d3.linkVertical().x(d => d.x).y(d => d.y));

// Draw nodes
g.selectAll('circle')
    .data(root.descendants())
    .enter()
    .append('circle')
    .attr('cx', d => d.x)
    .attr('cy', d => d.y)
    .attr('r', 5);

// Add labels
g.selectAll('text')
    .data(root.descendants())
    .enter()
    .append('text')
    .attr('x', d => d.x)
    .attr('y', d => d.y)
    .attr('dy', -10)
    .attr('text-anchor', 'middle')
    .text(d => d.data.question || d.data.text || d.data.action);

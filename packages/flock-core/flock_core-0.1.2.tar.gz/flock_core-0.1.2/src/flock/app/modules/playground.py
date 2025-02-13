from fasthtml.common import *
from fasthtml.svg import *
from monsterui.all import *

CODE = """
var pixelSize = 16
import 'https://cdn.interactjs.io/v1.9.20/auto-start/index.js'
import 'https://cdn.interactjs.io/v1.9.20/actions/drag/index.js'
import 'https://cdn.interactjs.io/v1.9.20/actions/resize/index.js'
import 'https://cdn.interactjs.io/v1.9.20/modifiers/index.js'
import 'https://cdn.interactjs.io/v1.9.20/dev-tools/index.js'
import interact from 'https://cdn.interactjs.io/v1.9.20/interactjs/index.js'

interact('.rainbow-pixel-canvas')
  .draggable({
    max: Infinity,
    maxPerElement: Infinity,
    origin: 'self',
    modifiers: [
      interact.modifiers.snap({
        // snap to the corners of a grid
        targets: [
          interact.snappers.grid({ x: pixelSize, y: pixelSize })
        ]
      })
    ],
    listeners: {
      // draw colored squares on move
      move: function (event) {
        var context = event.target.getContext('2d')
        // calculate the angle of the drag direction
        var dragAngle = 180 * Math.atan2(event.dx, event.dy) / Math.PI

        // set color based on drag angle and speed
        context.fillStyle =
          'hsl(' +
          dragAngle +
          ', 86%, ' +
          (30 + Math.min(event.speed / 1000, 1) * 50) +
          '%)'

        // draw squares
        context.fillRect(
          event.pageX - pixelSize / 2,
          event.pageY - pixelSize / 2,
          pixelSize,
          pixelSize
        )
      }
    }
  })
  // clear the canvas on doubletap
  .on('doubletap', function (event) {
    var context = event.target.getContext('2d')

    context.clearRect(0, 0, context.canvas.width, context.canvas.height)
    resizeCanvases()
  })

function resizeCanvases () {
  [].forEach.call(document.querySelectorAll('.rainbow-pixel-canvas'), function (
    canvas
  ) {
    delete canvas.width
    delete canvas.height

    var rect = canvas.getBoundingClientRect()

    canvas.width = rect.width
    canvas.height = rect.height
  })
}

resizeCanvases()

// interact.js can also add DOM event listeners
interact(window).on('resize', resizeCanvases)
"""

CODE2 = """
import 'https://cdn.interactjs.io/v1.9.20/auto-start/index.js'
import 'https://cdn.interactjs.io/v1.9.20/actions/drag/index.js'
import 'https://cdn.interactjs.io/v1.9.20/actions/resize/index.js'
import 'https://cdn.interactjs.io/v1.9.20/modifiers/index.js'
import 'https://cdn.interactjs.io/v1.9.20/dev-tools/index.js'
import interact from 'https://cdn.interactjs.io/v1.9.20/interactjs/index.js'
const svg = document.getElementById('connections');

    // Function to draw an SVG line between two points
    function createConnectionLine(x1, y1, x2, y2) {
      const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
      line.setAttribute("x1", x1);
      line.setAttribute("y1", y1);
      line.setAttribute("x2", x2);
      line.setAttribute("y2", y2);
      line.setAttribute("stroke", "red");
      line.setAttribute("stroke-width", "1");
      return line;
    }

    // Function to update connection lines
    function updateConnections() {
      // Clear existing connections
      svg.innerHTML = '';

      // Get the positions of the nodes
      const node1 = document.getElementById('node1');
      const node2 = document.getElementById('node2');
      const rect1 = node1.getBoundingClientRect();
      const rect2 = node2.getBoundingClientRect();

      // Calculate the centers of the nodes
      const x1 = rect1.left + rect1.width / 2;
      const y1 = rect1.top + rect1.height / 2;
      const x2 = rect2.left + rect2.width / 2;
      const y2 = rect2.top + rect2.height / 2;

      // Create and append a connection line
      const line = createConnectionLine(x1, y1, x2, y2);
      svg.appendChild(line);
    }

    // Initialize Interact.js
    interact('.node').draggable({
      listeners: {
        move(event) {
          // Move the dragged node
          const target = event.target;
          const x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx;
          const y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;

          target.style.transform = `translate(${x}px, ${y}px)`;
          target.setAttribute('data-x', x);
          target.setAttribute('data-y', y);

          // Update the connections
          updateConnections();
        }
      }
    });

    // Draw initial connections
    updateConnections();
"""

CODE3 = """
// Initial data
        let data = {
            nodes: [
                {id: 1, name: "Node 1"},
                {id: 2, name: "Node 2"},
                {id: 3, name: "Node 3"}
            ],
            links: [
                {source: 0, target: 1},
                {source: 1, target: 2}
            ]
        };

        // Create SVG container
        const svg = d3.select("svg");
        const width = +svg.attr("width");
        const height = +svg.attr("height");

        // Create force simulation
        const simulation = d3.forceSimulation(data.nodes)
            .force("link", d3.forceLink(data.links).id(d => d.id))
            .force("charge", d3.forceManyBody().strength(-300))
            .force("center", d3.forceCenter(width / 2, height / 2));

        // Create the links
        const link = svg.append("g")
            .selectAll("line")
            .data(data.links)
            .join("line")
            .attr("class", "link");

        // Create the nodes
        const node = svg.append("g")
            .selectAll("g")
            .data(data.nodes)
            .join("g")
            .attr("class", "node");

        // Add circles to nodes
        node.append("circle")
            .attr("r", 10)
            .style("fill", (d, i) => d3.schemeCategory10[i % 10]);

        // Add labels to nodes
        node.append("text")
            .attr("dx", 12)
            .attr("dy", ".35em")
            .text(d => d.name);

        // Add drag behavior
        node.call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended));

        // Double click on background to add node
        svg.on("dblclick", function(event) {
            const coords = d3.pointer(event);
            const newNode = {
                id: data.nodes.length + 1,
                name: `Node ${data.nodes.length + 1}`,
                x: coords[0],
                y: coords[1]
            };
            data.nodes.push(newNode);
            
            // Add link to nearest node
            if (data.nodes.length > 1) {
                const lastNode = data.nodes[data.nodes.length - 2];
                data.links.push({
                    source: lastNode,
                    target: newNode
                });
            }
            
            updateGraph();
        });

        // Update function to refresh the graph
        function updateGraph() {
            // Update links
            const link = svg.selectAll(".link")
                .data(data.links)
                .join("line")
                .attr("class", "link");

            // Update nodes
            const node = svg.selectAll(".node")
                .data(data.nodes)
                .join(
                    enter => {
                        const nodeEnter = enter.append("g")
                            .attr("class", "node")
                            .call(d3.drag()
                                .on("start", dragstarted)
                                .on("drag", dragged)
                                .on("end", dragended));

                        nodeEnter.append("circle")
                            .attr("r", 10)
                            .style("fill", (d, i) => d3.schemeCategory10[i % 10]);

                        nodeEnter.append("text")
                            .attr("dx", 12)
                            .attr("dy", ".35em")
                            .text(d => d.name);

                        return nodeEnter;
                    }
                );

            // Update simulation
            simulation.nodes(data.nodes);
            simulation.force("link").links(data.links);
            simulation.alpha(1).restart();
        }

        // Simulation tick function
        simulation.on("tick", () => {
            link
                .attr("x1", d => d.source.x)
                .attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x)
                .attr("y2", d => d.target.y);

            node
                .attr("transform", d => `translate(${d.x},${d.y})`);
        });

        // Drag functions
        function dragstarted(event, d) {
            if (!event.active) simulation.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }

        function dragged(event, d) {
            d.fx = event.x;
            d.fy = event.y;
        }

        function dragended(event, d) {
            if (!event.active) simulation.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }
"""


def get_playground():
    return Container(
        Canvas(cls="rainbow-pixel-canvas w-full h-full"),
        P("Drag to draw. Double tap to clear."),
        Script(code=CODE, type="module"),
        cls="w-full h-full",
    )


def get_playground2():
    return Container(
        Svg(
            width="800",
            height="600",
        ),
        Script(code=CODE3),
    )


def Playground():
    return Div(cls="flex flex-col w-full")(
        Div(cls="px-4 py-2 ")(
            H3("interact.js demo"),
            P("Rainbows!", cls=TextFont.muted_sm),
        ),
        get_playground2(),
    )

var graph = {
    "nodes":[
        {"label":"1","contents":""},
        {"label":"2","contents":""},
        {"label":"3","contents":""},
        {"label":"4","contents":""},
        {"label":"5","contents":""},
        {"label":"6","contents":""},
        {"label":"7",contents:""},
        {"label":"8","contents":""},
        {"label":"9","contents":""},
        {"label":"10","contents":""},
        {"label":"11","contents":""},
        {"label":"12","contents":""},
        {"label":"13","contents":""},
        {"label":"14","contents":""},
        {"label":"15","contents":""},
        {"label":"16","contents":""},
        {"label":"17","contents":""},
        {"label":"18","contents":""},
        {"label":"19","contents":""},
        {"label":"20","contents":""}
  ],
  "links":[
      {"source":"1","target":"2"},
      {"source":"1","target":"5"},
      {"source":"1","target":"6"},
      {"source":"2","target":"3"},
      {"source":"2","target":"8"},
      {"source":"3","target":"10"},
      {"source":"3","target":"4"},
      {"source":"4","target":"12"},
      {"source":"4","target":"5"},
      {"source":"5","target":"14"},
      {"source":"6","target":"7"},
      {"source":"6","target":"15"},
      {"source":"7","target":"8"},
      {"source":"7","target":"16"},
      {"source":"8","target":"9"},
      {"source":"9","target":"17"},
      {"source":"9","target":"10"},
      {"source":"10","target":"11"},
      {"source":"11","target":"12"},
      {"source":"11","target":"18"},
      {"source":"12","target":"13"},
      {"source":"13","target":"19"},
      {"source":"13","target":"14"},
      {"source":"14","target":"15"},
      {"source":"15","target":"20"},
      {"source":"16","target":"20"},
      {"source":"16","target":"17"},
      {"source":"17","target":"18"},
      {"source":"18","target":"19"},
      {"source":"19","target":"20"}
  ]
};




//below is almost entirely the basic code for a d3 force graph. change it after wumpus itself works.

var width = 960,
    height = 500;

var color = d3.scale.category20();

var force = d3.layout.force()
    .charge(-120)
    .linkDistance(50)
    .size([width, height]);

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

var nodeMap = {};
    graph.nodes.forEach(function(x) { nodeMap[x.label] = x; });
    graph.links = graph.links.map(function(x) {
      return {
        source: nodeMap[x.source],
        target: nodeMap[x.target],
        value: x.value
      };
    });
    

var drawGraph = function(graph) {
  force
      .nodes(graph.nodes)
      .links(graph.links)
      .start();

  var link = svg.selectAll(".link")
      .data(graph.links)
    .enter().append("line")
      .attr("class", "link")
      .style("stroke-width", function(d) { return Math.sqrt(d.value); });

  var gnodes = svg.selectAll('g.gnode')
     .data(graph.nodes)
     .enter()
     .append('g')
     .classed('gnode', true);
    
  var node = gnodes.append("circle")
      .attr("class", "node")
      .attr("r", 5)
      .style("fill", function(d) { return color(d.group); })
      .call(force.drag);

  var labels = gnodes.append("text")
      .text(function(d) { return d.label; });

    
  force.on("tick", function() {
    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    gnodes.attr("transform", function(d) { 
        return 'translate(' + [d.x, d.y] + ')'; 
    });
      
    
      
  });
};

drawGraph(graph);
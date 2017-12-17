// Get the data
var margin = {
    top: 30,
    right: 80,
    bottom: 80,
    left: 50
  };
  
// Set svg size:
var width = 1000 - margin.left - margin.right;
var height = 1000 - margin.top - margin.bottom;

// Set the ranges of the xaxis and yaxis:
var x = d3.scale.linear()
    .range([0, width]);

var y = d3.scale.linear()
    .range([height, 0]);

// Make variable colour:
var color = d3.scale.category10()

// Define xaxis:
var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

// Define yaxis:
var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");
    
var line = d3.svg.line()
    .x(function (d) { return x(d.x); })
    .y(function (d) { return y(d.y); });

// Append svg: 
var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");   


    
    
var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return "station = " + d.station + "</span>";
  })

svg.call(tip)
  
d3.json("jason.json", function(error, data) {
    data.forEach(function(d) {
        console.log(data)
        d.station = d.station;
        d.x = +d.x;
        d.y = +d.y; 
        d.kritiek = d.kritiek;

        
    });
  
    // Set domain, and use data.map to set xaxis:
    x.domain(d3.extent(data, function(d) { return d.y; })).nice();
    y.domain(d3.extent(data, function(d) { return d.x; })).nice();
    
    
    // Call xAsis, add text on axis:
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
      .selectAll("text")
        .style("text-anchor", "end")
        .attr("dy", "-3em")
        .attr("dx", "-2.5em")
        .attr("transform", "rotate(-60)" );
    
    
    // Use text to define the yAxis:
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
       .append("text")
        .attr("class", "label")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .text("x coördinates")  
    
    // Sppend text of Y-Axis:
    svg.append("g")
        .append("text")
        .attr("transform", "rotate(0)")
        .attr("y", 490)
        .attr("x", 850)
        .attr("dy", "30em")
        .style("text-anchor", "end")
        .text("y-coördinate");    
    
    // Select dot to make dots on the scatterplot, set radius on 10:   
    svg.selectAll(".dot")
        .data(data)
       .enter().append("circle")
        .attr("class", "dot")
        .attr("r", 10)
        .attr("cx", function(d) { return x(d.y); })
        .attr("cy", function(d) { return y(d.x); })
        .style("fill", function(d) { return color(d.kritiek); })
        .on('mouseover', tip.show)
        .on('mouseout', tip.hide);
        
    //Draw the line
 var circle = svg.append("line")
                         .attr("x1", 542.407550366666)
                         .attr("y1", 33.16993658333135)
                         .attr("x2", 521.7315102666663)
                         .attr("y2", 268.6470636666673)
                         .attr("stroke-width", 3)
                         .attr("stroke", "red");
            svg.append("line")
                         .attr("x1", 521.7315102666663)
                         .attr("y1", 268.6470636666673)
                         .attr("x2", 443.32425473333325)
                         .attr("y2", 336.8400874166672)
                         .attr("stroke-width", 3)
                         .attr("stroke", "red");             
            svg.append("line")
                         .attr("x1", 443.32425473333325)
                         .attr("y1", 336.8400874166672)
                         .attr("x2", 441.44453079999954)
                         .attr("y2", 386.9033809999998)
                         .attr("stroke-width", 3)
                         .attr("stroke", "red");             
            svg.append("line")
                         .attr("x1", 441.44453079999954)
                         .attr("y1", 386.9033809999998)
                         .attr("x2", 423.72221029999986)
                         .attr("y2", 454.0637303333346)
                         .attr("stroke-width", 3)
                         .attr("stroke", "red");   
            svg.append("line")
                         .attr("x1", 423.72221029999986)
                         .attr("y1", 454.0637303333346)
                         .attr("x2", 393.11101283333323)
                         .attr("y2", 475.28581741666926)
                         .attr("stroke-width", 3)
                         .attr("stroke", "red");                          
      
    // Select .legend to set colours to death-rate:
    var legend = svg.selectAll(".legend")
        .data(color.domain())
       .enter().append("g")
        .attr("class", "legend")
        .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });      

    // Make rectangles to define the colours in:     
    legend.append("rect")
        .attr("x", 750)
        .attr("y", 115) 
        .attr("width", 40)
        .attr("height", 18)
        .style("fill", color) 
     
    svg.append("g")
        .append("text")
        .attr("transform", "rotate(0)")
        .attr("x", 810)
        .attr("dy", "100")
        .style("text-anchor", "end")
        .text("Legenda: ");
        
     svg.append("g")
        .append("text")
        .attr("transform", "rotate(0)")
        .attr("x", 873)
        .attr("dy", "130")
        .style("text-anchor", "end")
        .text("= kritiek ");
        
    svg.append("g")
        .append("text")
        .attr("transform", "rotate(0)")
        .attr("x", 910)
        .attr("dy", "150")
        .style("text-anchor", "end")
        .text("= niet - kritiek ");
    
    
    
    
});
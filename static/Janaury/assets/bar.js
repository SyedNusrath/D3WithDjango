window.onload = function () {

    function riskbasecTargets() {
        var barchartArray = [
            ["", 57, "#a0c334", "CREDENTIAL MANAGEMENT(57%)"],
            ["", 36, "#3e64ff", "SESSION ISOLATION(36%)"],
            ["", 10, "#f58b54", "LEAST PRIVILGE(10%)"],
            ["", 15, "#ffd369", "EMBEDDED CREDENTIALS(15%)"],
            ["", 25, "#003f5c", "BEHAVIORAL ANALYTICS(25%)"],
        ];
        var tr = "";
        for (i = 0; i < barchartArray.length; i++) {

            var color = barchartArray[i][2];
            var percentage = barchartArray[i][1] + "%";
            var percentageMinus = 100 - barchartArray[i][1] + "%";
            tr = tr + '<tr><td class="percent" style="text-align: center;background-size: ' + percentage + ' 100%; background-repeat: no-repeat;background-image: linear-gradient(to right,' + color + ', ' + color + ')">' + barchartArray[i][3] + '</td></tr>';

        }

        document.getElementById('chartContainer').innerHTML = tr;
    }
    function BulidBarchart(data, divId, header, width, height) {

        var margin = { top: 50, right: 50, bottom: 50, left: 50 },
            width = width - margin.left - margin.right,
            height = height - margin.top - margin.bottom;


        var x = d3.scale.ordinal()
            .rangeRoundBands([0, width], .3, .3);

        var y = d3.scale.linear()
            .range([height, 0]);

        var xAxis = d3.svg.axis()
            .scale(x)
            .orient("bottom");

        var yAxis = d3.svg.axis()
            .scale(y)
            .orient("left")
            .ticks(8);

        var svg = d3.select("#" + divId).append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        x.domain(data.map(function (d) { return d.name; }));
        y.domain([0, d3.max(data, function (d) { return d.value; })]);

        svg.append("text")
            .attr("class", "title")
            .attr("x", x(data[0].name))
            .attr("y", -26)
            .text(header);

        svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis)
            .selectAll(".tick text")
            .call(wrap, x.rangeBand());

        svg.selectAll(".bar")
            .data(data)
            .enter().append("rect")
            .attr("class", "bar")
            .attr("x", function (d) {

                return x(d.name);
            })
            .attr("width", x.rangeBand())
            .attr("y", function (d) {

                return y(d.value);
            })
            .attr("height", function (d) { return height - y(d.value); })
            .attr("fill", function (d) { return d.color; })
            ;

        // Controls the text labels at the top of each bar. Partially repeated in the resize() function below for responsiveness.
        svg.selectAll(".text")
            .data(data)
            .enter()
            .append("text")
            .attr("class", "label")
            .attr("x", (function (d) { return x(d.name) + x.rangeBand() / 4 }))
            .attr("y", function (d) { return y(d.value) + 1; })
            .attr("dy", "-.75em")
            .text(function (d) { return d.label; })

        function isFloat(n) {
            return Number(n) === n && n % 1 !== 0;
        }
        function wrap(text, width) {
            text.each(function () {
                var text = d3.select(this),
                    words = text.text().split(/\s+/).reverse(),
                    word,
                    line = [],
                    lineNumber = 0,
                    lineHeight = 1.1, // ems
                    y = text.attr("y"),
                    dy = parseFloat(text.attr("dy")),
                    tspan = text.text(null).append("tspan").attr("x", 0).attr("y", y).attr("dy", dy + "em");
                while (word = words.pop()) {
                    line.push(word);
                    tspan.text(line.join(" "));
                    if (tspan.node().getComputedTextLength() > width) {
                        line.pop();
                        tspan.text(line.join(" "));
                        line = [word];
                        tspan = text.append("tspan").attr("x", 0).attr("y", y).attr("dy", ++lineNumber * lineHeight + dy + "em").text(word);
                    }
                }
            });
        }

        function type(d) {
            d.value = +d.value;
            return d;
        }
    }


    //var license = [{ "name": "# Licenses", "value": 2200 }, { "name": "Licensed", "value": 2135 }, { "name": "#People who have access to Vault", "value": 4120 }, { "name": "# Sales", "value": 3540 }];

    var achivementsByPlatformData = [{ "name": "Windows Domain Admins", "value": 100, "color": "#003f5c", "label": "100%" },
    { "name": "Windows Local Admins", "value": 25, "color": "#003f5c", "label": "25%" },
    { "name": "Unix Root", "value": 65, "color": "#003f5c", "label": "65%" },
    { "name": "DBA", "value": 43, "color": "#003f5c", "label": "43%" },
    { "name": "Mainframe", "value": 12, "color": "#003f5c", "label": "12%" }
    ];
    riskbasecTargets();
    BulidBarchart(achivementsByPlatformData, "AchivementsByPlatform", " ", 500, 300)
}

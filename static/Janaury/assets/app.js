

window.onload = function () {

    google.load("visualization", "1", {packages:["corechart"]});
    google.setOnLoadCallback(drawChart);
    google.setOnLoadCallback(drawColumnChart);
    function drawChart() {
        var data = google.visualization.arrayToDataTable([
            ["Element", "Density", { role: "style" }, { role: 'annotation' }],
            ["", 57, "color: #a0c334", "CREDENTIAL MANAGEMENT(57%)"],
            ["", 36, "color: #3e64ff", "SESSION ISOLATION(36%)"],
            ["", 10, "color: #f58b54", "LEAST PRIVILGE(10%)"],
            ["", 15, "color: #ffd369", "EMBEDDED CREDENTIALS(15%)"],
            ["", 25, "color: #003f5c", "BEHAVIORAL ANALYTICS(25%)"],
        ]);

        var view = new google.visualization.DataView(data);
        view.setColumns([0, 1,
            {
                calc: "stringify",
                sourceColumn: 3,
                type: "string",
                role: "annotation"
            },
            2]);

        var options = {
            title: "",
            fill: 100,
            height: 400,
            allowHtml: true,
            chartArea: { left: 20, top: 10, bottom: 20, width: '80%', height: '80%' },
            bar: { groupWidth: "85%" },
            legend: { position: "none" },
            annotations: {
                textStyle: {
                    fontName: 'Times-Roman',
                    fontSize: 14,
                    bold: true
                }
            },
            hAxis: {
                textStyle: "#FFFFFF"
            }
        };
        var chart = new google.visualization.BarChart(document.getElementById("barchart_values"));
        chart.draw(view, options);
    }



    function drawColumnChart() {
        var data = google.visualization.arrayToDataTable([
            ["Element", "Density", { role: "style" }, { role: 'annotation' }],
            ["Windows Domain Admins", 100, "color: #003f5c", "100%"],
            ["Windows Local Admins", 25, "color: #003f5c", "25%"],
            ["Unix Root", 65, "color: #003f5c", "65%"],
            ["DBA", 43, "color: #003f5c", "43%"],
            ["Mainframe", 12, "color: #003f5c", "12%"]
        ]);

        var view = new google.visualization.DataView(data);
        view.setColumns([0, 1,
            {
                calc: "stringify",
                sourceColumn: 3,
                type: "string",
                role: "annotation"
            },
            2]);

        var options = {
            title: "",
            height: 400,
            bar: { groupWidth: "85%" },
            chartArea: { left: 20, top: 10, width: '80%'},
            legend: { position: "none" },
            annotations: {
                textStyle: {
                    fontName: 'Times-Roman',
                    fontSize: 14,
                    bold: true
                }
            },
        };
        var chart = new google.visualization.ColumnChart(document.getElementById("columnchart_values"));
        chart.draw(view, options);
    }

}
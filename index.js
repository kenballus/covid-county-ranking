$(document).ready(() => {
    $('select').formSelect();

    renderData(table_data);
    $('select').on("change", (e) => {
        table_data.sort((a, b) => {
            if (typeof(a[e.target.value]) == "string") {
              if (typeof(b[e.target.value]) == "string") {
                return 0;
              }
              return  1;
            }
            if (typeof(b[e.target.value]) == "string") {
              return -1;
            }

            if (a[e.target.value] < b[e.target.value]) return  1;
            if (a[e.target.value] > b[e.target.value]) return -1;
            return 0
        })
        renderData(table_data);
    })

});

function renderData(data) {
    $("#main_body").html("")
    for (var i = 0; i < data.length; i++) {
        $("#main_body").append("<tr><td>" + (i + 1) + "</td>" +
                               "<td>" + data[i][0] +      // County
                               "</td><td>" + data[i][1] + // State
                               "</td><td>" + data[i][2] + // Population
                               "</td><td>" + data[i][3] + // Cases
                               "</td><td>" + data[i][4] + // Deaths
                               "</td><td>" + Number(data[i][5].toFixed(3)) + // Cases per thousand
                               "</td><td>" + Number(data[i][6].toFixed(3)) + // Deaths per thousand
                               "</td><td>" + Number(data[i][7].toFixed(3)) + // Death rate
                               "</td></tr>");
    }
}
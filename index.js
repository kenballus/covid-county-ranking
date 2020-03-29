$(document).ready(() => {
    $('select').formSelect();

    renderData(table_data);
    $('select').on("change", (e) => {
        table_data.sort((a, b) => {
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
                               "</td><td>" + String(data[i][5]).slice(0, 5) + // Cases per thousand
                               "</td><td>" + String(data[i][6]).slice(0, 5) + // Deaths per thousand
                               "</td><td>" + String(data[i][7]).slice(0, 5) + // Death rate
                               "</td></tr>");
    }
}
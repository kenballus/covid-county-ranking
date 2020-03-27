
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
        $("#main_body").append("<tr><td>"+ (i + 1) + "</td>" +
                               "<td>" + data[i][1] + 
                               "</td><td>" + data[i][2] + 
                               "</td><td>" + data[i][2] + 
                               "</td><td>" + data[i][3] + 
                               "</td><td>" + data[i][4] + 
                               "</td></tr>");
    }
}
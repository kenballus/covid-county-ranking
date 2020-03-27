
$(document).ready(() => {
    $('select').formSelect();
    var instance = M.FormSelect.getInstance($('select').get(0))

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
        row = data[i];
        $("#main_body").append("<tr><td>"+ (i + 1) + "</td>" +
                               "<td>" + row[0] + 
                               "</td><td>" + row[1] + 
                               "</td><td>" + row[2] + 
                               "</td><td>" + row[3] + 
                               "</td></tr>");
    }
}
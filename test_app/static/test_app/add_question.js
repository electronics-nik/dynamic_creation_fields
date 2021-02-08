$(document).ready(function () {
    $("#add-answer").click(function (e) {
        $("#answers").append('<div class="form-group row">' +
            '                <div class="form-check form-check-inline" style="float: left;">' +
            '                    <input class="form-check-input" type="checkbox" value="option1">' +
            '                </div>' +
            '                <div style="float: left; width: 80%; margin-right: 2%;">' +
            '                    <input class="form-control" type="search" value="Answer">' +
            '                </div>' +
            '                <div style="float: left; width: 100px; margin-right: 2%;">' +
            '                    <input type="button" id="delete" value="remove">' +
            '                </div>' +
            '            </div>')
    });
    $("body").on('click', '#delete', function (e) {
        $(this).parent("div").parent("div").remove();
    });
});

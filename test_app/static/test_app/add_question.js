
let answer_count = Number($("[name=answer_block_count]").val());
let answer_list = [];
// alert(bin_icon);
// let bin_icon = '/static/test_app/bin.png';

$("#add-answer").click(function () {
// new form
    let row = $('<div class="form-row border" style="padding: 10px 0px 10px 5px; margin-bottom: 5px;"></div>');

    // text box
    let element = $('<input type="text" class="form-control" placeholder="Answer">');
    element.attr('name', 'answer_text_' + answer_count);
    element = $('<div class="col-9" style="margin-top: 10px; margin-bottom: 10px;"></div>').append(element);
    row.append(element);

    // check boxes
    let block1 = $('<div class="form-check"></div>');
    element = $('<input class="form-check-input" type="checkbox" checked>');
    element.attr('name', 'answer_is_active_' + answer_count);
    block1.append(element);
    block1.append($('<label class="form-check-label" for="answer_is_active">is active</label>'));

    let block2 = $('<div class="form-check"></div>');
    element = $('<input class="form-check-input" type="checkbox">');
    element.attr('name', 'answer_is_correct_' + answer_count);
    block2.append(element);
    block2.append($('<label class="form-check-label" for="answer_is_correct">is correct</label>'));

    row.append($('<div class="col-2"></div>').append(block1).append(block2));

    // button 'remove'
    element = $('<img src=' + bin_icon + ' width="30" height="30" id="remove">');
    element.attr('name', answer_count);
    row.append($('<div class="col" style="margin: 10px 0px 10px 0px; padding-top: 5px;"></div>').append(element));

    answer_list.push(answer_count);
    $("#answers").append(row);
    answer_count ++;
    $("[name=answer_block_count]").val(answer_count);
    $("[name=answer_list]").val(answer_list);
});

$("body").on('click', '#remove', function (e) {
    let pos = answer_list.indexOf(Number(this.name));
    // alert(pos);
    answer_list.splice(pos, 1);
    $("[name=answer_list]").val(answer_list);
    $(this).parent("div").parent('div').remove();
});

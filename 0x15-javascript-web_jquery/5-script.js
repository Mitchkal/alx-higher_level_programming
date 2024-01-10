$(document).ready(function () {
  $('#add_item').on('click', function () {
    const newItem = $('<li>Item</li>');
    $('UL.my_list').append(newItem);
  });
});

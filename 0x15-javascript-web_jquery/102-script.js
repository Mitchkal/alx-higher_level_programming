$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    const languageCode = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/', {
      lang: languageCode
    }).done(function (response) {
      $('#hello').text(response.hello);
    });
  });
});

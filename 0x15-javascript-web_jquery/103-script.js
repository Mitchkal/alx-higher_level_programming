$(document).ready(function () {
  const fetchTranslation = function () {
    const languageCode = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/', {
      lang: languageCode
    }).done(function (response) {
      $('#hello').text(response.hello);
    });
  };
  $('#language_code').on('keypress', function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
  $('#btn_translate').on('click', fetchTranslation);
});

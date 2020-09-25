$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const lan = $('INPUT#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${lan}`, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });

  $('INPUT#language_code').keypress((event) => {
    if (event.which === 13) {
      const lan = $('INPUT#language_code').val();
      $.get(`https://www.fourtonfish.com/hellosalut/?lang=${lan}`, (data) => {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});

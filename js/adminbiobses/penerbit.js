function showForm (actionselect, data) {
  //reset form
  $('form')[0].reset();

  if (actionselect == 0) {
    $('#modal-default').find('.modal-title').text('Tambah Penerbit')
    $("form :input").prop("disabled", false);
    $('#btnsave').text('Save').show()
    $('#btnsave').val('new')
    $("form").attr('action', '/adminbiobses/penerbit/');
  }
  $('#modal-default').modal('toggle');
}

$(function(){
  var table = $('#example1').DataTable({
    select: true,
  });

  $('#example1 tbody').on( 'click', 'tr', function () {
        $(this).toggleClass('selected');
  });

  var actionselect = 0;

    $("#actionmenu li a").each(function(){
        $(this).click(function(e){
            actionselect = $(this).parent().index();

            var jumlah = table.rows( { selected: true } ).count()
            var data = table.rows('.selected').data()[0];

            if (actionselect != 0 && jumlah != 1) {
                alert("you must select only one row")
            } else {
                showForm(actionselect, data)
            }
            e.preventDefault();
        });
    });

})

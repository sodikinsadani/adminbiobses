function setForm(data){
  $("#id_nama_sub_kategori").val(data[2])
}

function showForm (actionselect, data) {
  //reset form
  $('form')[1].reset();
  if (actionselect == 0) {
    $('#modal-default').find('.modal-title').text('Tambah Sub Kategori')
    $("form .box-body :input").prop("disabled", false);
    $('#btnsave').text('Save')
    $('#btnsave').show()
    $('#btnreset').show()
    $("form").attr('action', '/adminbiobses/subkategori/');
  } else if (actionselect == 1) {
    $('#modal-default').find('.modal-title').text('Edit Sub Kategori')
    $("form .box-body :input").prop("disabled", false)
    setForm(data)
    $('#btnsave').text('Update')
    $('#btnsave').show()
    $('#btnreset').show()
    $("form").attr('action', '/adminbiobses/subkategori/'+data[1]+'/edit/');
  } else if (actionselect == 2) {
    $('#modal-default').find('.modal-title').text('Hapus Sub Kategori')
    $("form .box-body :input").prop("disabled", true)
    setForm(data)
    $('#btnsave').text('Delete')
    $('#btnsave').show()
    $('#btnreset').hide()
    $("form").attr('action', '/adminbiobses/subkategori/'+data[1]+'/delete/');
  } else if (actionselect == 4) {
    $('#modal-default').find('.modal-title').text('Data Sub Kategori')
    $("form .box-body :input").prop("disabled", true)
    setForm(data)
    $('#btnsave').hide()
    $('#btnreset').hide()
    $("form").attr('action', '/adminbiobses/subkategori/'+data[1]+'/delete/');
  }

  $('#modal-default').modal('toggle');
}

$(function(){
  var table = $('#example1').DataTable({
    "columnDefs":[
      {"targets":[1],
    "visible":false}
  ],
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

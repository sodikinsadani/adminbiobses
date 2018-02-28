function setForm(data){
  $("#id_nama_buku").val(data[2])
  /*$("#id_pengarang").val(data[3])
  $("#id_penerbit").val(data[4])
  $("#id_subkategori").val(data[5])
  $("#id_harga").val(data[6])
  $("#id_berat").val(data[7])
  $("#id_diskon").val(data[8])
  $("#id_image1").val(data[9])
  $("#id_image2").val(data[10])
  $("#id_image3").val(data[11])*/
}

function showForm (actionselect, data) {
  //reset form
  $('form')[1].reset();
  if (actionselect == 0) {
    $('#modal-default').find('.modal-title').text('Tambah Buku')
    $("form .box-body :input").prop("disabled", false);
    $('#btnsave').text('Save')
    $('#btnsave').show()
    $('#btnreset').show()
    $("form").attr('action', '/adminbiobses/buku/');
  } else if (actionselect == 1) {
    $('#modal-default').find('.modal-title').text('Edit Buku')
    $("form .box-body :input").prop("disabled", false)
    setForm(data)
    $('#btnsave').text('Update')
    $('#btnsave').show()
    $('#btnreset').show()
    $("form").attr('action', '/adminbiobses/buku/'+data[1]+'/edit/');
  } else if (actionselect == 2) {
    $('#modal-default').find('.modal-title').text('Hapus Buku')
    $("form .box-body :input").prop("disabled", true)
    setForm(data)
    $('#btnsave').text('Delete')
    $('#btnsave').show()
    $('#btnreset').hide()
    $("form").attr('action', '/adminbiobses/buku/'+data[1]+'/delete/');
  } else if (actionselect == 4) {
    $('#modal-default').find('.modal-title').text('Data Buku')
    $("form .box-body :input").prop("disabled", true)
    setForm(data)
    $('#btnsave').hide()
    $('#btnreset').hide()
    $("form").attr('action', '/adminbiobses/buku/'+data[1]+'/delete/');
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
  "scrollX": true,
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

function showImageField(imageField, imageShow, data){
  var input = imageField,
    label = data.split('/')[1];
	input.trigger('fileselect', [label]);
  imageShow.attr("src", "/static/bookimages/"+data);
}

function setForm(data){
  $("#id_nama_buku").val(data[2])
  $("#id_pengarang option").filter(function() {
    return $(this).text().toUpperCase() == data[3].toUpperCase();
  }).prop('selected', true);
  $("#id_penerbit option").filter(function() {
    return $(this).text().toUpperCase() == data[4].toUpperCase();
  }).prop('selected', true);
  $("#id_subkategori option").filter(function() {
    return $(this).text().toUpperCase() == data[5].toUpperCase();
  }).prop('selected', true);
  $("#id_harga").val(data[6])
  $("#id_berat").val(data[7])
  $("#id_diskon").val(data[8])
  showImageField($('#id_image1'), $("#img-upload1"), data[9])
  showImageField($('#id_image2'), $("#img-upload2"), data[10])
  showImageField($('#id_image3'), $("#img-upload3"), data[11])
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

function readURL(input, imgUpload) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            imgUpload.attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
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

  $('form').on('change', '.btn-file :file', function() {
    var input = $(this),
			label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
		input.trigger('fileselect', [label]);
	});

  $('.btn-file :file').on('fileselect', function(event, label) {

    var input = $(this).parents('.input-group').find(':text'),
      log = label;

    if (input.length) {
      input.val(log);
    } else {
      if (log) alert(log);
    }

  });

  $("#id_image1").change(function(){
	    readURL(this, $('#img-upload1'));
	});
  $("#id_image2").change(function(){
	    readURL(this, $('#img-upload2'));
	});
	$("#id_image3").change(function(){
	    readURL(this, $('#img-upload3'));
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

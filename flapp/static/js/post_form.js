var titleInput = $('#id_title')
var contentInput = $('#id_content')
var coverInput = $('#id_cover_image')
var authorInput = $('#id_author')
var editorInput = $('#id_post_editor')

function setContent(value) {
	$('#preview-content').html(value);
}

$('.wmd-preview-title').hide();
$('#id_content_wmd_preview').hide()

contentInput.keyup(function(){
	var newContent = $('#id_content_wmd_preview').html()
	setContent(newContent)
})

function setTitle(value){
	$("#preview-title").text(value)
}

titleInput.keyup(function(){
	var newContent = $(this).val()
	setTitle(newContent)
})

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#preview-cover').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

coverInput.change(function(){
	readURL(this);
})

function setAuthor(value){
	$("#preview-author").text(value)
}

authorInput.change(function(){
	var newContent = $('#id_author option:selected').text()
	setAuthor(newContent)
})

function setEditor(value){
	$("#preview-editor").text(value)
}

editorInput.change(function(){
	var newContent = $('#id_post_editor option:selected').text()
	setEditor(newContent)
})

var d = new Date();
var date = d.getDate();
var month = d.getMonth();
var year = d.getFullYear()
var months    = ['January','February','March','April','May','June','July','August','September','October','November','December'];
var month = months[month]
$("#preview-date").text(date+" "+month+", "+year)

$('#form-head').click(function(){
	$('.post').hide()
	$('.post-form').show()
	$('#form-head').css('background-color', 'lightgreen')
	$('#preview-head').css('background-color', '')
})

$('#preview-head').click(function(){
	$('.post-form').hide()
	$('.post').show()
	$('#preview-head').css('background-color', 'lightgreen')
	$('#form-head').css('background-color', '')
})
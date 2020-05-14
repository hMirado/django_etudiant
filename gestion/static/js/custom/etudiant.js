var $ = jQuery.noConflict();
$(document).ready(function() {
  $('.edit-etudiant').click(function() {
    $('#etudiant-id').val($(this).data('id'));
    $('#etudiant-num').val($(this).data('num'));
    $('#edutiant-identifiant').val($(this).data('identifiant'));
    $('#edutiant-fname').val($(this).data('fname'));
    $('#edutiant-lname').val($(this).data('lname'));
    $('#edutiant-birthday').val($(this).data('birthday'));
    $('#edutiant-adresse').val($(this).data('adresse'));
    $('#contact-phone').val($(this).data('phone'));
    $('#contact-email').val($(this).data('email'));
    $('#parent-pere').val($(this).data('pere'));
    $('#parent-mere').val($(this).data('mere'));
    $('#parent-phone_pere').val($(this).data('phone_pere'));
    $('#parent-phone_mere').val($(this).data('phone_mere'));
    $('#parent-adresse_parent').val($(this).data('adresse_parent'));
  });


  $('.action-detail').click(function() {
    document.getElementById("detail-etudiant-name").innerHTML = $(this).data('name');
    document.getElementById("detail-etudiant-id").innerHTML = $(this).data('identifiant');
    document.getElementById("detail-etudiant-birthday").innerHTML = $(this).data('birthday');
    document.getElementById("detail-etudiant-contact").innerHTML = $(this).data('contact');
    document.getElementById("detail-etudiant-adresse").innerHTML = $(this).data('adresse');
    document.getElementById("detail-etudiant-pere").innerHTML = $(this).data('phone_pere');
    document.getElementById("detail-etudiant-mere").innerHTML = $(this).data('phone_mere');
  });

});

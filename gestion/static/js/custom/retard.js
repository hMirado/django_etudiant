var $ = jQuery.noConflict();
$(document).ready(function() {
  $('.edit-retard').click(function() {
    $('#retard-id').val($(this).data('id'));
    $('#retard-identifiant').val($(this).data('identifiant'));
    $('#retard-niveau').val($(this).data('niveau'));
    $('#retard-matiere').val($(this).data('matiere'));
    $('#retard-semestre').val($(this).data('semestre'));
  });
});

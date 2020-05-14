var $ = jQuery.noConflict();

$(document).ready(function () {
    $('.tableau-scroll').DataTable({
        "language": {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/French.json"
        },
        "scrollX": true,
        responsive: true
    });

    $('.tableau').DataTable({
        "language": {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/French.json"
        },
    });

    $('.cancel').click(function (event) {
		event.preventDefault();
		location.reload(true);
	});
});

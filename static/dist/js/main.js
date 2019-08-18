(function( $ ) {
    
    'use strict';
    
    // Chosen-js
    $('#genres').chosen();
    
    // Datepicker
    $('#publication_date').datepicker({
        header: true,
        footer: true,
        modal: true,
        format: 'dd mmmm yyyy',
    });
    
    // Bootstrap form validation
    window.addEventListener('load', function() {
        var forms = document.getElementsByClassName('needs-validation');
        
        var validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
    
    // Scrollbars
    $('.book-scroller').overlayScrollbars({
       overflowBehavior : {
           x : 'scroll'
       },
    });
    
})( jQuery );
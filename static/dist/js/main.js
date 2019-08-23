(function( $ ) {
    
    'use strict';
    
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
    
    // Chosen-js
    $('#genres').chosen();
    
    // Datepicker
    $('#publication_date').datepicker({
        header: true,
        footer: true,
        modal: true,
        format: 'dd mmmm yyyy',
    });
    
    // Magnific Popup
    $('.image-popup-fit-width').magnificPopup({
       type: 'image',
       closeOnContentClick: true,
       image: {
           verticalFit: false,
       }
    });
    
    // Scrollbars
    $('.book-scroller').overlayScrollbars({
       overflowBehavior : {
           x : 'scroll'
       },
    });
    
    // Toastr
    $('.toastr').each(function() {
        var toastr_category = $(this).attr('data-category');
        var toastr_message = $(this).attr('data-message');
        
        if ( toastr_category == 'success' ) {
            toastr.success(toastr_message);
        } else if ( toastr_category == 'warning' ) {
            toastr.warning(toastr_message);
        } else if ( toastr_category == 'error' ) {
            toastr.error(toastr_message);
        } else if ( toastr_category == 'info' ) {
            toastr.info(toastr_message);
        } else {
            toastr.info(toastr_message);
        }
        
        toastr.options = {
            'progressBar' : true,
            'preventDuplicates' : true,
        }
    });
    
})( jQuery );
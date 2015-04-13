/* Project specific Javascript goes here. */
// Convert errorlist to Bootstrap alerts
jQuery(document).ready(function(){
    jQuery('form ul.errorlist').each(function(){
        var ul = jQuery(this);
        ul.find('li').each(function(){
            var li = jQuery(this);
            ul.after('<div class="alert alert-danger" role="alert">' + li.text() + '</div>');
        });
        ul.remove();
    });
});
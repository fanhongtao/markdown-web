$(document).ready(function() {

  if($('#search-results').length ){
    $('.toggle-context').each(function () {
      var hiddenContext = $(this).parent().next('div.search-context').find('li:hidden');
      if ( !hiddenContext.length ) {
        $(this).toggle();
      } else {
        $(this).click(function () {
          hiddenContext.toggle();
          $(this).toggle();
        });
      }
    });

    var searchQuery = new RegExp(searchTerms.join('|'), 'gi'); //searchTerms provided by the layout template.
    $('div.search-context li span').each(function () {
      var curText = $(this).html().replace(/"/g, '&quot;').replace(/'/g, '&#39;');
      var newText = curText.replace(searchQuery, function (match) {
        return '<span class="bg-green-light">' + match + '</span>';
      });

      $(this).html(newText);
    });
  }

})


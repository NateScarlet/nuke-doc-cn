$('<link>')
	.appendTo($('head'))
	.attr({type: 'text/css', rel: 'stylesheet'})
	.attr('href', 'Content/assets/Stylesheets/toc_separators.css');

//Full Screen Images
$(document).ready(function() {
  $("#topic").attr({ "allowfullscreen": "", "webkitallowfullscreen": "", "mozallowfullscreen": ""});
});
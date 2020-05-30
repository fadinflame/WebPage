/*global $, jQuery, alert*/
$(document).ready(function() {

 
  // ========================================================================= //
  //  Typed Js
  // ========================================================================= //

  var typed = $(".typed");

  $(function() {
    typed.typed({
      strings: ["Albert Berezin.", "fadinflame.","Python Developer."],
      typeSpeed: 60,
      loop: true,
    });
  });



});

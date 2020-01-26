$(document).ready(function() {
  /*-----sticky navigation------*/
  $(".js--section-features").waypoint(
    function(direction) {
      if (direction == "down") {
        $("nav").addClass("sticky");
      } else {
        $("nav").removeClass("sticky");
      }
    },
    {
      offset: "60px"
    }
  );
  /*-----scroll buttons------*/
  $(".js--scrolltoplans").click(function() {
    $("html,body").animate(
      { scrollTop: $(".js--section-plans").offset().top },
      1000
    );
  });
  $(".js--scrolltofea").click(function() {
    $("html,body").animate(
      { scrollTop: $(".js--section-features").offset().top },
      1000
    );
  });
  /*----Navigation scroll-----*/
  $('a[href*="#"]').on("click", function(e) {
    e.preventDefault();

    $("html, body").animate(
      {
        scrollTop: $($(this).attr("href")).offset().top
      },
      500,
      "linear"
    );
  });
  /*----animation-----*/
  $(".ws-wp-1").waypoint(
    function(direction) {
      $(".ws-wp-1").addClass("animated fadeIn");
    },
    {
      offset: "50%"
    }
  );
  $(".ws-wp-2").waypoint(
    function(direction) {
      $(".ws-wp-2").addClass("animated fadeInUp");
    },
    {
      offset: "50%"
    }
  );
  $(".ws-wp-3").waypoint(
    function(direction) {
      $(".ws-wp-3").addClass("animated fadeIn");
    },
    {
      offset: "50%"
    }
  );
  $(".ws-wp-4").waypoint(
    function(direction) {
      $(".ws-wp-4").addClass("animated pulse");
    },
    {
      offset: "50%"
    }
  );
});

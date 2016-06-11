/*
 * Scripts that are executed 
 * when the document is ready
 */
 $(document).ready(function()
 {
  activeNav();

        //Spies the sidebar
        $('body').scrollspy();
        if(document.title=="Home")
        {
          $('#sidebar').affix({
            offset : {
              top : 380
            }
          });
        }
        else
        {
          var height=document.getElementById('section0').offsetHeight;
          $('#sidebar').affix({
            offset : {
              top : height+375
            }
          });
        }

        //On click local link
        $('a').click(function(e)
        {
          var section = $(this).attr('href');
          if(section.indexOf("#") !== -1)
          {
            section = section.replace('#','');
            var sec = document.getElementById(section);
            $('html,body').animate({scrollTop:$(sec).offset().top-50},'slow');
          }
        });

        //On click on sidebar element
        $('ul.nav-list > li>a').click(function(e)
        {
          $('ul.nav-list > li').removeClass('active');
          $(this).addClass('active');
          var section = $(this).children('a').attr('href');
          section = section.replace('#','');
          var sec = document.getElementById(section);

          //Animation for transition
          $('html,body').animate({scrollTop:$(sec).offset().top-50},'slow');
          e.preventDefault();
        });
        
        $(window).scroll(function () {
          var title=document.title.toLowerCase().replace("the ","");
          document.getElementById(title).setAttribute("class", "active");
        });

      });
function activeNav()
{
  var title=document.title.toLowerCase().replace("the ","");
  document.getElementById(title).setAttribute("class", "active");
}
 if( !document.layers && !document.all && !document.getElementById )
   event = "test";

 function showtip( current, e, text ) {

     if( document.all || document.getElementById ) {

         thetitle = text.split('<br>');

         if( thetitle.length > 1 ) {
             thetitles = '';

             for( i = 0; i < thetitle.length; i++ )
                 thetitles += thetitle[i];
             current.title = thetitles;

         } else
             current.title = text;

     } else if( document.layers ) {

         document.tooltip.document.write('<layer bggolor="white" style="border:1px solid black;font-size:12px;">'+text+'</layer>');
         document.tooltip.document.close();
         document.tooltip.left=e.pageX+5;
         document.tooltip.top=e.pageY+5;
         document.tooltip.visibility="show";

     }

 }

 function hidetip() {

     if( document.layers )
         document.tooltip.visibility = "hidden";

 }
 
/*

------------------------------------------

	Flipbox written by CrappoMan

	simonpatterson@dsl.pipex.com

------------------------------------------

*/

function flipBox(who) {

	var tmp;

	if (document.images['b_' + who].src.indexOf('_on') == -1) {

		tmp = document.images['b_' + who].src.replace('_off', '_on');

		document.getElementById('box_' + who).style.display = 'none';

		document.images['b_' + who].src = tmp;

	} else {

		tmp = document.images['b_' + who].src.replace('_on', '_off');

		document.getElementById('box_' + who).style.display = 'block';

		document.images['b_' + who].src = tmp;

	}

}



function addText(elname, wrap1, wrap2) {

	if (document.selection) { // for IE

		var str = document.selection.createRange().text;

		document.forms['inputform'].elements[elname].focus();

		var sel = document.selection.createRange();

		sel.text = wrap1 + str + wrap2;

		return;

	} else if ((typeof document.forms['inputform'].elements[elname].selectionStart) != 'undefined') { // for Mozilla

		var txtarea = document.forms['inputform'].elements[elname];

		var selLength = txtarea.textLength;

		var selStart = txtarea.selectionStart;

		var selEnd = txtarea.selectionEnd;

		var oldScrollTop = txtarea.scrollTop;

		//if (selEnd == 1 || selEnd == 2)

		//selEnd = selLength;

		var s1 = (txtarea.value).substring(0,selStart);

		var s2 = (txtarea.value).substring(selStart, selEnd)

		var s3 = (txtarea.value).substring(selEnd, selLength);

		txtarea.value = s1 + wrap1 + s2 + wrap2 + s3;

		txtarea.selectionStart = s1.length;

		txtarea.selectionEnd = s1.length + s2.length + wrap1.length + wrap2.length;

		txtarea.scrollTop = oldScrollTop;

		txtarea.focus();

		return;

	} else {

		insertText(elname, wrap1 + wrap2);

	}

}



function insertText(elname, what) {

	if (document.forms['inputform'].elements[elname].createTextRange) {

		document.forms['inputform'].elements[elname].focus();

		document.selection.createRange().duplicate().text = what;

	} else if ((typeof document.forms['inputform'].elements[elname].selectionStart) != 'undefined') { // for Mozilla

		var tarea = document.forms['inputform'].elements[elname];

		var selEnd = tarea.selectionEnd;

		var txtLen = tarea.value.length;

		var txtbefore = tarea.value.substring(0,selEnd);

		var txtafter =  tarea.value.substring(selEnd, txtLen);

		var oldScrollTop = tarea.scrollTop;

		tarea.value = txtbefore + what + txtafter;

		tarea.selectionStart = txtbefore.length + what.length;

		tarea.selectionEnd = txtbefore.length + what.length;

		tarea.scrollTop = oldScrollTop;

		tarea.focus();

	} else {

		document.forms['inputform'].elements[elname].value += what;

		document.forms['inputform'].elements[elname].focus();

	}

}

function textCounter(field, countfield, maxlimit) {
if (field.value.length > maxlimit) // if too long...trim it!
field.value = field.value.substring(0, maxlimit);
// otherwise, update 'characters left' counter
else 
countfield.value = maxlimit - field.value.length;
}
     
   
   function insertUN(username) {
	var username = "@" + username + ": ";
	var formname = "chatform";
	var elname = "shout_message";
	if (document.forms[formname].elements[elname].createTextRange) {
		document.forms[formname].elements[elname].focus();
		document.selection.createRange().duplicate().text = username;
	} else if ((typeof document.forms[formname].elements[elname].selectionStart) != 'undefined') { // for Mozilla
		var tarea = document.forms[formname].elements[elname];
		var selEnd = tarea.selectionEnd;
		var txtLen = tarea.value.length;
		var txtbefore = tarea.value.substring(0,selEnd);
		var txtafter = tarea.value.substring(selEnd, txtLen);
		var oldScrollTop = tarea.scrollTop;
		tarea.value = txtbefore + username + txtafter;
		tarea.selectionStart = txtbefore.length + username.length;
		tarea.selectionEnd = txtbefore.length + username.length;
		tarea.scrollTop = oldScrollTop;
		tarea.focus();
	} else {
		document.forms[formname].elements[elname].value += username;
		document.forms[formname].elements[elname].focus();
	}
}

/*function toggleBox( toggle_id )
{
    var toggle = document.getElementById( toggle_id );

    if( toggle.style.display == "none" )
      void( toggle.style.display = "block" );

    else
      void( toggle.style.display = "none" );
}*/

function toggleBox( div )
{
  doc = document.getElementById( div );

  if( doc.style.display == 'none' )
  {
    $(function()
    {
      $( '#' + div ).slideDown( 'slow' );
    });
  }
  else
  {
    $(function()
    {
      $( '#' + div ).slideUp( 'slow' );
    });
  }
}

// From here and further goes AJAX

function newXmlHttpRequest() {
      http_request = false;
      if (window.XMLHttpRequest) { // Mozilla, Safari,...
         http_request = new XMLHttpRequest();
         if (http_request.overrideMimeType) {
         	// set type accordingly to anticipated content type
            //http_request.overrideMimeType('text/xml');
            http_request.overrideMimeType('text/html');
         }
      } else if (window.ActiveXObject) { // IE
         try {
            http_request = new ActiveXObject("Msxml2.XMLHTTP");
         } catch (e) {
            try {
               http_request = new ActiveXObject("Microsoft.XMLHTTP");
            } catch (e) {}
         }
      }
      if (!http_request) {
         alert('Cannot create XMLHTTP instance');
         return false;
      } else {
 return http_request;
	  }
}


function makerequest(serverPage, objID) {
	
	switch(objID){
		
		case 'Shoutbox-results':
			showLoading(objID);
		break;
	}
 
 	var xmlhttp = newXmlHttpRequest();
	var obj = document.getElementById(objID);

	xmlhttp.open("GET", serverPage);
	xmlhttp.onreadystatechange = function() {
		if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
			obj.innerHTML = xmlhttp.responseText;
		}
	}
	xmlhttp.send(null);
}

function showLoading (objID){
	hidden = document.getElementById(objID);
hidden.innerHTML = '<div style="text-align:center;"><img src="/shoutbox/images/ajax/throbber.gif" alt="Loading..." title="Loading..." /></div>';
}

function threadVote(postid, vote) {
	  var vote_request = newXmlHttpRequest();
      var poststr = "postid=" + encodeURI(postid) + "&vote=" + encodeURI(vote);
      vote_request.onreadystatechange = function() {
		if(vote_request.readyState == 4){
			if(vote_request.status == 200){
            result = vote_request.responseText;
            document.getElementById('echovote_' + postid).innerHTML = result;
            }
         } else {
            document.getElementById('echovote_' + postid).innerHTML = "Posting...";
            }
            }
      vote_request.open('POST', "vote.php", true);
      vote_request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      vote_request.setRequestHeader("Content-length", poststr.length);
      vote_request.setRequestHeader("Connection", "close");
      vote_request.send(poststr);
}
   
function reloadShoutbox() {
  	 makerequest('/shoutbox/shoutbox_result.php', 'Shoutbox-results');
  //interval = setInterval('reloadShoutbox()', 10000);
}

function postshout(url) 
{
 var xml = newXmlHttpRequest();
 var form = document.getElementsByTagName( "form" )["chatform"];
 var shout = form.shout_message.value;
 var post = form.post_shout.value;
 var code = form.shout_code.value;
 var poststr = "post_shout=" + encodeURI(post) + "&shout_message=" + encodeURI(shout) + "&shout_code=" + code; 
 //form.post_shout.disabled = 'true';
 xml.onreadystatechange = function()
 {
		//setTimeout("reloadShoutbox()", 2000);
		if(!xml.readyState == 4)
		{
			if(!xml.status == 200)
        alert("Shout failed!");
		}
  };
  xml.open('POST', url, true);
  xml.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xml.setRequestHeader("Content-length", poststr.length);
  xml.setRequestHeader("Connection", "close");
  xml.send(poststr);
  form.reset();
  //form.post_shout.disabled='false';
  reloadShoutbox();
}

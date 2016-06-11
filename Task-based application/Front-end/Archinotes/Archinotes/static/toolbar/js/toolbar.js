(function ($, undefined) {
	var panelId = 0;
	var toolbarInitialized = false;
	
	var shells;
	var originalPadding = 0;
	
	var toolbar;
	var panels = new Array();
	var panelsWrap;
	var activePanel = 0;
	var form;
	
	var events = new Array();
	
	function Form(root) {
		this.el = $(root);
		this.values = new Array();
		this.refresh();
		this.error = '';
	}
	Form.prototype.refresh = function() {
		var root = this;
		events = new Array();
		var i = 0;
		$('#events-table tr').each(function() {
			events[i] = {
				date : $(this).find('.date input').val(),
				title : $(this).find('.title input').val()
			}
			i++;
		});
	}
	Form.prototype.validate = function() {
		var result = true;
		var root = this;
		
		this.el.find('input[type=text]').each(function() {
			if ($(this).val() == '') {
				result = false;
				root.error = 'Please fill all text fields!';
			}
		});
		
		return result;
	}
	
	function Panel(name, width) {
		this.width = width;
		this.name = name;
		this.id = this.name + '-panel';
		this.el = $('#' + this.id);
		this.button = $('#' + this.name);
		
		this.el.css({ "width" : this.width });
	}
	Panel.prototype.show_panel = function() {
		toolbar.css({ "width" : this.width });
		panelsWrap.css({ "width" : this.width });
		shells.css({ "margin-left" : originalPadding + this.width/2 });

		if (activePanel != 0) {
			panels[activePanel].hide_panel();
		}
		this.el.show();
		activePanel = this.name;
		
		$('.toolbar .button.active').removeClass('active');
		this.button.addClass('active');
	}
	Panel.prototype.hide_panel = function() {
		this.el.hide();
		this.button.removeClass('active');
		activePanel = 0;
	}
	
	$(document).ready(function() {
		init();
		$('.toolbar .button').on('click', show_panel);
		$(document).on('click', hide_panels);
		$('#refresh').on('click', refresh);
		$('#add-new-event').on('click', add_event);
	});
	
	function init() {
		shells = $('.pagewrap');
		toolbar = $('.toolbar');
		panelsWrap = $('#panels-wrap');
		panels['settings'] = new Panel('settings', 300);
		panels['video'] = new Panel('video', 760);
		
		form = new Form($('#settings-panel form'));
		
		$('.slider').slider({
			change : update_slider,
			slide : update_slider
		});
		
		init_get_events();
		init_put_events();
		events_table_events();
		$('#my-timeline').timelinexml();
		
	}
	function update_slider() {
		$(this).prev().html($(this).slider("option", "value"));
	}
	function show_panel() {
		panels[$(this).attr('id')].show_panel();
		
		if (!toolbarInitialized) {
			toolbarInitialized = true;
			toolbar.removeClass('init');
		}
	}
	function hide_panels(e) {
		if ($(e.target).closest('.toolbar').length == 0 && !$(e.target).is('input')) {
			toolbar.css({ "width" : 0 });
			shells.css({ "margin-left" : originalPadding });
			$('.button.active').removeClass('active');
		}
	}
	function refresh() {
		$('#result').html('');
		if (form.validate()) {
			form.refresh();
			$('.demo-box').html(generate_html());
			$('#my-timeline').timelinexml();
		} else {
			$('#result').html(form.error);
		}
	}
	function generate_html() {
		var html = '';
		
		html = '<div id="my-timeline">';
		html += '	<div class="timeline-html-wrap">';
		
		var len = events.length, i=0;
		for (i=0; i<len; i++) {
			html += '<div class="timeline-event">';
			
			html += '	<div class="timeline-date">' + events[i].date + '</div>';
			html += '	<div class="timeline-title">' + events[i].title + '</div>';
			html += '	<div class="timeline-content">Aunt Polly placed small trust in such evidence. She went out to see for herself; and she would have been content to find twenty per cent. of Tom\'s statement true. When she found the entire fence whitewashed, and not only whitewashed but elaborately coated and recoated, and even a streak added to the ground, her astonishment was almost unspeakable. She said: "Well, I never! There\'s no getting round it, you can work when you\'re a mind to, Tom." And then she diluted the compliment by adding, "But it\'s powerful seldom you\'re a mind to, I\'m bound to say. Well, go \'long and play; but mind you get back some time in a week, or I\'ll tan you."	She was so overcome by the splendor of his achievement that she took him into the closet and selected a choice apple and delivered it to him, along with an improving lecture upon the added value and flavor a treat took to itself when it came without sin through virtuous effort. And while she closed with a happy Scriptural flourish, he "hooked" a doughnut.	Then he skipped out, and saw Sid just starting up the outside stairway that led to the back rooms on the second floor. Clods were handy and the air was full of them in a twinkling. They raged around Sid like a hail-storm; and before Aunt Polly could collect her surprised faculties and sally to the rescue, six or seven clods had taken personal effect, and Tom was over the fence and gone. There was a gate, but as a general thing he was too crowded for time to make use of it. His soul was at peace, now that he had settled with Sid for calling attention to his black thread and getting him into trouble.</div>';		
			html += '	<div class="timeline-link"><a href="#">Read More</a></div>';
			
			html += '</div>';
		}
		
		html += '	</div>';
		html += '</div>';
		
		return html;
	}

	function init_get_events() {
		var i=0;
		$('.timeline-event').each(function() {
			var the_event = $(this);
			events[i] = {
				date : $(this).find('.timeline-date').html(),
				title : $(this).find('.timeline-title').html()
			}
			i++;
		});
	}
	function init_put_events() {
		var len = events.length;
		var container = $('#events');
		var html = '<table id="events-table">';
		
		for (var i=0; i<len; i++) {
			html += '<tr>';
			html += '<td class="date"><input type="text" value="' + events[i].date + '"></td>';
			html += '<td class="title"><input type="text" value="' + events[i].title + '"></td>';
			html += '<td class="delete"><input type="button" value="x"></td>';
			html += '</tr>';
		}
		
		html += '</table>';
		
		container.html(html);
	}
	function events_table_events() {
		$('#events-table input[type=button]').unbind('.events-table');
		
		$('#events-table input[type=button]').on('click.events-table', function() {
			$(this).closest('tr').remove();
		});
	}
	function add_event() {
		var html = '<tr><td class="date"><input type="text" value="01.01.2012"></td> <td class="title"><input type="text" value="New Event"></td> <td class="delete"><input type="button" value="-"></td></tr>';
		$('#events-table').append(html);
		
		events_table_events();
	}
}(jQuery));

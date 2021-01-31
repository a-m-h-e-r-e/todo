
$('.delete').click(function(){
	var task_id;
	task_id = $(this).attr('data-catid');
	$.ajax({
	  type: 'GET',
	  url: '/todo/delete_task',
	  data: {id: task_id},
	  success: function(data) {location.reload()}
	})
})


$('.checkbox').click(function(){
	var task_id;
	task_id = $(this).attr("data-catid");
	if(!$(this).prop('checked')){
	$.ajax(
	    {
	        type:"GET",
	        url: "/todo/unmark_task_complete",
	        data:{id: task_id},
	        success: function(data){location.reload();}
	     })
	} else {
	$.ajax(
	{
	    type:"GET",
	    url: "/todo/mark_task_complete",
	    data:{id: task_id},
	    success: function(data){location.reload();}
	 })
	}
});


var id;
var updated_task;
// Edit a task
document.querySelectorAll("button[class='edit_task_button'").forEach(editBtn => editBtn.addEventListener("click", editTask));
function editTask() {
	this.parentNode.children[0].checked = false;
	this.parentNode.children[0].disabled = true;;
	this.previousElementSibling.setAttribute('class', 'span_editable');
	this.previousElementSibling.setAttribute('contenteditable', '');
	this.innerHTML = '<i class="fa fa-check" aria-hidden="true"></i>';
	this.style.backgroundColor = "mediumseagreen";
	// alert(event.target.id);
	id = event.target.id;
	this.removeEventListener("click", editTask);
	this.addEventListener("click", validateEditTask);
}

// Validate changes
function validateEditTask() {
	this.parentNode.children[0].disabled = false;;
	this.previousElementSibling.removeAttribute('class', 'span_editable');
	this.previousElementSibling.removeAttribute('contenteditable', '');
	this.innerHTML = '<i class="fa fa-pencil" aria-hidden="true"></i>';
	this.style.backgroundColor = "grey";
	updated_task = this.previousElementSibling.innerHTML;
	this.removeEventListener("click", validateEditTask);
	this.addEventListener("click", editTask);
	$.ajax(
	{
	    type:"GET",
	    url: "/todo/update_task",
	    data:{id: id, updated_task: updated_task},
	    success: function(data){location.reload();}
	 })
}

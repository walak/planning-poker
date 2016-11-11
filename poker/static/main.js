function addTask(){
    task = getTask()
    board_id = getBoardId()
    $.post("board/"+board_id+"/tasks/add",task,function() {
        getTasks()
    })
}

function getTasks() {
    board_id = getBoardId()
    $.get("board/"board_id+"/tasks",function(data) {
        alert(data)
    })
}
function getBoardId() {
    return $("body").attr('id');
}

function getTask() {
    name = $("#task_name").attr("value")
    description = $("#task_desc").html()
    return {
        "name" : name,
        "description" : description
    }
}
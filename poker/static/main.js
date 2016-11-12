function addTask(event){
    task = getTask();
    board_id = getBoardId();
    postJson(board_id+"/tasks/add",task,function(response) {
        size = response.length
        tasks = []
        $("#task_list").empty()
        for (var i = 0;i < size;i++) {
            task_li = document.createElement("li");
            task_li.setAttribute("data-task-id",response[i].id);
            task_li.textContent = response[i].name
            document.getElementById("task_list").appendChild(task_li)
        }
    });
    return false;
};

function postJson(url,entity, clb){
    payload = JSON.stringify(entity)
    $.ajax({
        url: url,
        data : payload,
        type : "POST",
        contentType: 'application/json',
        success: clb
    });
}

function getTasks() {
    board_id = getBoardId();

};
function getBoardId() {
    return $("body").attr('data-board-id');
};

function getTask() {
    task_name = $("#task_name").val();
    task_description = $("#task_desc").val();
    return {
        name : task_name,
        description : task_description
    };
};
function addTask(event){
    task = getTask();
    board_id = getBoardId();
    postJson(board_id+"/tasks/add",task,function() {
        getTasks()
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
    return $("body").attr('id');
};

function getTask() {
    task_name = $("#task_name").val();
    task_description = $("#task_desc").val();
    return {
        name : task_name,
        description : task_description
    };
};